class Person:

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


class Student(Person):

    def __init__(self, name, roll_no):
        super().__init__(name)     # Calls Parent Constructor
        self.__roll_no = roll_no

    def get_roll_no(self):
        return self.__roll_no

    def set_roll_no(self, roll_no):
        self.__roll_no = roll_no

    def display(self):
        print("Name     :", self.get_name())
        print("Roll No  :", self.get_roll_no())


student1 = Student("Kabir", 101)

print("Before Updating")
student1.display()


student1.set_name("Rahul")
student1.set_roll_no(102)

print("\nAfter Updating")
student1.display()