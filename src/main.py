import animals_scrapper

def main():
    animals = animals_scrapper.AnimalsScrapper().download_data()
    csv_text = "Image,Common Name,Scientific Name,Kingdom,Diet,Life Span,Weight,IUNC,IUNC Description\n"
    for kingdom in animals:
        csv_text += "".join([a.csv() for a in animals[kingdom]])
    
    print(csv_text, file=open("animals.csv", "w"))

if __name__ == "__main__":
    main()