# employee.py

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


def display_employee(employee):
    print("Name:", employee.get_name())
    print("ID Number:", employee.get_id_number())
    print("Department:", employee.get_department())
    print("Position:", employee.get_position())
    print()


def main():
    # Test cases from assignment
    employee1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
    employee2 = Employee("Mark Jones", 39119, "IT", "Programmer")
    employee3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")

    print("EMPLOYEE INFORMATION")
    print("--------------------")
    display_employee(employee1)
    display_employee(employee2)
    display_employee(employee3)


if __name__ == "__main__":
    main()
