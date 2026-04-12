# patient_procedure.py

class Patient:
    def __init__(self, first_name, middle_name, last_name, address, city, state,
                 zip_code, phone_number, emergency_contact_name, emergency_contact_phone):
        self.__first_name = first_name
        self.__middle_name = middle_name
        self.__last_name = last_name
        self.__address = address
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code
        self.__phone_number = phone_number
        self.__emergency_contact_name = emergency_contact_name
        self.__emergency_contact_phone = emergency_contact_phone

    # Mutators
    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_middle_name(self, middle_name):
        self.__middle_name = middle_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_address(self, address):
        self.__address = address

    def set_city(self, city):
        self.__city = city

    def set_state(self, state):
        self.__state = state

    def set_zip_code(self, zip_code):
        self.__zip_code = zip_code

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def set_emergency_contact_name(self, emergency_contact_name):
        self.__emergency_contact_name = emergency_contact_name

    def set_emergency_contact_phone(self, emergency_contact_phone):
        self.__emergency_contact_phone = emergency_contact_phone

    # Accessors
    def get_first_name(self):
        return self.__first_name

    def get_middle_name(self):
        return self.__middle_name

    def get_last_name(self):
        return self.__last_name

    def get_address(self):
        return self.__address

    def get_city(self):
        return self.__city

    def get_state(self):
        return self.__state

    def get_zip_code(self):
        return self.__zip_code

    def get_phone_number(self):
        return self.__phone_number

    def get_emergency_contact_name(self):
        return self.__emergency_contact_name

    def get_emergency_contact_phone(self):
        return self.__emergency_contact_phone


class Procedure:
    def __init__(self, procedure_name, procedure_date, practitioner_name, charges):
        self.__procedure_name = procedure_name
        self.__procedure_date = procedure_date
        self.__practitioner_name = practitioner_name
        self.__charges = charges

    # Mutators
    def set_procedure_name(self, procedure_name):
        self.__procedure_name = procedure_name

    def set_procedure_date(self, procedure_date):
        self.__procedure_date = procedure_date

    def set_practitioner_name(self, practitioner_name):
        self.__practitioner_name = practitioner_name

    def set_charges(self, charges):
        self.__charges = charges

    # Accessors
    def get_procedure_name(self):
        return self.__procedure_name

    def get_procedure_date(self):
        return self.__procedure_date

    def get_practitioner_name(self):
        return self.__practitioner_name

    def get_charges(self):
        return self.__charges


def display_patient(patient):
    print("PATIENT INFORMATION")
    print("-------------------")
    print("Name:", patient.get_first_name(), patient.get_middle_name(), patient.get_last_name())
    print("Address:", patient.get_address())
    print("City:", patient.get_city())
    print("State:", patient.get_state())
    print("ZIP Code:", patient.get_zip_code())
    print("Phone:", patient.get_phone_number())
    print("Emergency Contact:", patient.get_emergency_contact_name())
    print("Emergency Contact Phone:", patient.get_emergency_contact_phone())
    print()


def display_procedure(procedure, number):
    print(f"PROCEDURE #{number}")
    print("Procedure Name:", procedure.get_procedure_name())
    print("Date:", procedure.get_procedure_date())
    print("Practitioner:", procedure.get_practitioner_name())
    print("Charge: $", format(procedure.get_charges(), ".2f"), sep="")
    print()


def main():
    patient = Patient(
        "John",
        "A.",
        "Smith",
        "123 Main Street",
        "Champaign",
        "IL",
        "61820",
        "217-555-1234",
        "Jane Smith",
        "217-555-5678"
    )

    procedure1 = Procedure("Physical Exam", "Today's date", "Dr. Irvine", 250.00)
    procedure2 = Procedure("X-ray", "Today's date", "Dr. Jamison", 500.00)
    procedure3 = Procedure("Blood test", "Today's date", "Dr. Smith", 200.00)

    display_patient(patient)
    display_procedure(procedure1, 1)
    display_procedure(procedure2, 2)
    display_procedure(procedure3, 3)

    total_charges = (
        procedure1.get_charges() +
        procedure2.get_charges() +
        procedure3.get_charges()
    )

    print("TOTAL CHARGES")
    print("-------------")
    print("$", format(total_charges, ".2f"), sep="")


if __name__ == "__main__":
    main()
