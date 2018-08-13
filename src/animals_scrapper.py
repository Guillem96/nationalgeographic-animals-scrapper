# Using selenium becaus national geographic webpage is dinamically generated with JS
from selenium.webdriver import Firefox
from contextlib import closing
from bs4 import BeautifulSoup
from animal import Builder


class AnimalsScrapper(object):
    BASE_URL = "https://www.nationalgeographic.com/animals/"
    ENDPOINTS = [
        "mammals",
        "birds",
        "reptiles",
        "amphibians",
        "invertebrates",
        "fish"
    ]

    NUMBER_EACH_KINGDOM = 6  # MAX 6 species
    METADATA = "Image,Common Name,Scientific Name,Kingdom,Diet,Life Span,Weight,Relative size,IUNC,IUNC Description\n"
    FACTS_KEYS = {
        "Common Name:": lambda animal_builder, value: animal_builder.common_name(value),
        "Scientific Name:": lambda animal_builder, value: animal_builder.scientific_name(value),
        "Type:": lambda animal_builder, value: animal_builder.kingdom(value),
        "Diet:": lambda animal_builder, value: animal_builder.diet(value),
        "Average life span in The Wild:": lambda animal_builder, value: animal_builder.average_life_span(value),
        "Weight:": lambda animal_builder, value: animal_builder.weight(value),
    }

    def download_data(self):
        result = {}
        with closing(Firefox()) as browser:
            for endpoint in AnimalsScrapper.ENDPOINTS:
                print("Loading " + AnimalsScrapper.BASE_URL + endpoint + "...")

                browser.get(AnimalsScrapper.BASE_URL + endpoint)

                print("Parsing " + AnimalsScrapper.BASE_URL + endpoint + "...")
                print("--- " + endpoint.upper() + " ---")

                soup = BeautifulSoup(browser.page_source, 'html.parser')
                result[endpoint] = self.__download_kingdom(browser, soup)

        return result

    def __download_kingdom(self, browser, soup):
        animals = []
        animals_links = [x['href'] for x in soup.select(
            "a.div-link")[:AnimalsScrapper.NUMBER_EACH_KINGDOM]]

        for animal_url in animals_links:
            animals.append(self.__download_animal(browser, animal_url))

        return animals

    def __download_animal(self, browser, url):
        print("Parsing " + url.split("/")[-1] + " ...")

        animal_builder = Builder()

        browser.get(url)
        soup = BeautifulSoup(browser.page_source, 'html.parser')

        # Get animal thumbnail
        bg_style = soup.select_one(
            ".fast-facts__thumbnail-image").select_one(".low-rez-image")["style"]
        animal_builder.image(self.__get_url_from_style(bg_style))

        # Get image that illustrates the relative size of the animal in front of humans size
        relative_size_img = soup.select_one(".fast-facts__relative-size-image")
        if relative_size_img:
            relative_size_style = relative_size_img.select_one(
                ".low-rez-image")["style"]
            animal_builder.size_relative_to_human(
                self.__get_url_from_style(relative_size_style))

        status_container = soup.select_one(".fast-facts__status-value")
        if status_container:
            animal_builder.iunc_red_list(status_container.get_text().strip())

        for fact in soup.select_one(".fast-facts__facts").select("p"):
            key = fact.select_one(".fast-facts__facts__key").get_text().strip()
            fact_value = fact.get_text().replace(key, '').strip()
            if key in AnimalsScrapper.FACTS_KEYS:
                AnimalsScrapper.FACTS_KEYS[key](animal_builder, fact_value)

        print(url.split("/")[-1] + " done!")

        return animal_builder.build()

    def __get_url_from_style(self, style):
        return AnimalsScrapper.BASE_URL.replace("/animals", "") + style.replace('background-image: url("/', '').replace('");', '')
