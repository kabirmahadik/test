

class Person:
    AVG_AGE = 20

    def __init__(self):
        print("Person constructor is called.")
        self.__name = None
        self.__dob = None
        self.__address = None

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_dob(self):
        return self.__dob

    def set_dob(self, dob):
        self.__dob = dob

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address


person = Person()

person.set_name("Kabir Mahadik")
person.set_dob("11-08-2005")
person.set_address("Madhya Pradesh")

print("Name:", person.get_name())
print("Date of Birth:", person.get_dob())
print("Address:", person.get_address())
print("Average Age:", Person.AVG_AGE)