class Car:


    def __init__(self):
        self.__brand = "Toyota"
        self.__model = "Fortuner"
        self.__year = 2024
        self.__color = "Black"


    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_color(self):
        return self.__color


    def set_brand(self, brand):
        self.__brand = brand

    def set_model(self, model):
        self.__model = model

    def set_year(self, year):
        self.__year = year

    def set_color(self, color):
        self.__color = color



car1 = Car()


print("Before Updating")
print("Brand :", car1.get_brand())
print("Model :", car1.get_model())
print("Year  :", car1.get_year())
print("Color :", car1.get_color())


car1.set_brand("Honda")
car1.set_model("City")
car1.set_year(2025)
car1.set_color("White")


print("\nAfter Updating")
print("Brand :", car1.get_brand())
print("Model :", car1.get_model())
print("Year  :", car1.get_year())
print("Color :", car1.get_color())