# session14.py

class Employee:
    def __init__(self, name="", id_number=0, department="", position=""):
        self.__name = name
        self.__id_number = id_number
        self.__department = department
        self.__position = position

    # Mutators
    def set_name(self, name):
        self.__name = name

    def set_id_number(self, id_number):
        self.__id_number = id_number

    def set_department(self, department):
        self.__department = department

    def set_position(self, position):
        self.__position = position

    # Accessors
    def get_name(self):
        return self.__name

    def get_id_number(self):
        return self.__id_number

    def get_department(self):
        return self.__department

    def get_position(self):
        return self.__position

    def display_info(self):
        print("Name:", self.__name)
        print("ID Number:", self.__id_number)
        print("Department:", self.__department)
        print("Position:", self.__position)


class Manager(Employee):   # Inheritance
    def __init__(self, name="", id_number=0, department="", position="", salary=0):
        super().__init__(name, id_number, department, position)
        self.__salary = salary

    # Mutator
    def set_salary(self, salary):
        self.__salary = salary

    # Accessor
    def get_salary(self):
        return self.__salary

    # New method
    def calculate_bonus(self):
        return self.__salary * 0.10

    # Overridden method
    def display_info(self):
        super().display_info()
        print("Salary: $", format(self.__salary, ",.2f"), sep="")
        print("Bonus: $", format(self.calculate_bonus(), ",.2f"), sep="")


def main():
    manager1 = Manager("Susan Meyers", 47899, "Accounting", "Vice President", 85000)
    manager2 = Manager("Mark Jones", 39119, "IT", "Department Manager", 72000)

    print("MANAGER 1")
    print("---------")
    manager1.display_info()
    print()

    print("MANAGER 2")
    print("---------")
    manager2.display_info()
    print()


if __name__ == "__main__":
    main()
