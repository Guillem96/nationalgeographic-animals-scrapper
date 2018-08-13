class Animal(object):

    __IUNC_RED_LIST = {
        "Least Concern": "At relatively low risk of extinction",
        "Near Threatened": "Likely to become vulnerable in the near future",
        "Vulnerable": "At high risk of extinction in the wild",
        "Endangered": "At very high risk of extinction in the wild",
        "Critically Endangered": "At extremely high risk of extinction in the wild",
        "Extinct in the Wild": "Survives only in captivity",
        "Extinct": "No surviving individuals in the wild or in captivity",
    }

    def __init__(self, img, common_name, scientific_name, kingdom, diet, average_life_span, weight, size_relative_to_human, iunc):
        self.__img = img
        self.__common_name = common_name
        self.__scientific_name = scientific_name
        self.__kingdom = kingdom
        self.__diet = diet
        self.__average_life_span = average_life_span
        self.__weight = weight
        self.__size_relative_to_human = size_relative_to_human
        self.__iunc_red_list = iunc

    def get_image(self):
        return self.__img

    def get_common_name(self):
        return self.__common_name

    def get_scientific_name(self):
        return self.__scientific_name

    def get_kingdom(self):
        return self.__kingdom

    def get_diet(self):
        return self.__diet

    def get_average_life_span(self):
        return self.__average_life_span

    def get_weight(self):
        return self.__weight

    def get_size_relative_to_human(self):
        return self.__size_relative_to_human

    def get_iunc_red_list(self):
        return self.__iunc_red_list

    def csv(self):
        csv_str = (self.get_image() if self.get_image() != "" else "-") + "," + \
            (self.get_common_name() if self.get_common_name() != "" else "-") + "," + \
            (self.get_scientific_name() if self.get_scientific_name() != "" else "-")  + "," + \
            (self.get_kingdom() if self.get_kingdom() != "" else "-")  + "," + \
            (self.get_diet() if self.get_diet() != "" else "-")  + "," + \
            (self.get_average_life_span() if self.get_average_life_span() != "" else "-")  + "," + \
            (self.get_weight() if self.get_weight() != "" else "-")  + "," + \
            (self.get_size_relative_to_human() if self.get_size_relative_to_human() != "" else "-")  + "," + \
            (self.get_iunc_red_list() if self.get_iunc_red_list() != "" else "-") + ","

        if self.get_iunc_red_list() in Animal.__IUNC_RED_LIST:
            csv_str += Animal.__IUNC_RED_LIST[self.get_iunc_red_list()]
        else:
            csv_str += "-"
        return csv_str + "\n"


class Builder(object):
    def __init__(self):
        self.__img = ""
        self.__common_name = ""
        self.__scientific_name = ""
        self.__kingdom = ""
        self.__diet = ""
        self.__average_life_span = ""
        self.__weight = ""
        self.__size_relative_to_human = ""
        self.__iunc_red_list = ""

    def image(self, img):
        self.__img = img
        return self

    def common_name(self, name):
        self.__common_name = name
        return self

    def scientific_name(self, name):
        self.__scientific_name = name
        return self

    def average_life_span(self, average_life_span):
        self.__average_life_span = average_life_span
        return self

    def weight(self, weight):
        self.__weight = weight
        return self

    def kingdom(self, kingdom):
        self.__kingdom = kingdom
        return self

    def diet(self, diet):
        self.__diet = diet
        return self

    def size_relative_to_human(self, size_relative_to_human):
        self.__size_relative_to_human = size_relative_to_human
        return self

    def iunc_red_list(self, iunc_red_list):
        self.__iunc_red_list = iunc_red_list
        return self

    def build(self):
        return Animal(self.__img,
                      self.__common_name,
                      self.__scientific_name,
                      self.__kingdom,
                      self.__diet,
                      self.__average_life_span,
                      self.__weight,
                      self.__size_relative_to_human,
                      self.__iunc_red_list)
