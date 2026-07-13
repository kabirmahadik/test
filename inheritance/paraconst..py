class Employee:

    def __init__(self, name, emp_id, salary):
        self.__name = name
        self.__emp_id = emp_id
        self.__salary = salary

    def get_name(self):
        return self.__name

    def get_emp_id(self):
        return self.__emp_id

    def get_salary(self):
        return self.__salary


emp1 = Employee("Kabir", 101, 50000)

print("Employee Name :", emp1.get_name())
print("Employee ID   :", emp1.get_emp_id())
print("Salary        :", emp1.get_salary())
