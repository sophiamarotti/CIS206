import csv


def load_customers(filename):
    customers = []

    with open(filename, "r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        for row in reader:
            customers.append(row)

    return customers


def display_by_company(customers):

    sorted_list = sorted(customers, key=lambda c: c["companyName"].lower())

    print("\nCustomers sorted by Company Name\n")

    for c in sorted_list:
        print("Company:", c["companyName"])
        print("Contact:", c["contactName"])
        print("Phone:", c["phone"])
        print()


def display_by_contact(customers):

    sorted_list = sorted(customers, key=lambda c: c["contactName"].lower())

    print("\nCustomers sorted by Contact Name\n")

    for c in sorted_list:
        print("Contact:", c["contactName"])
        print("Company:", c["companyName"])
        print("Phone:", c["phone"])
        print()


def search_company(customers, text):

    matches = []

    for c in customers:
        if text.lower() in c["companyName"].lower():
            matches.append(c)

    return matches


def search_contact(customers, text):

    matches = []

    for c in customers:
        if text.lower() in c["contactName"].lower():
            matches.append(c)

    return matches


def display_matches(matches):

    if len(matches) == 0:
        print("\nNo matching records found\n")
        return

    for c in matches:
        print("Customer ID:", c["customerID"])
        print("Company:", c["companyName"])
        print("Contact:", c["contactName"])
        print("Phone:", c["phone"])
        print()


def menu():

    print("\nNorthwind Customers Menu")
    print("1 Display company name sorted list")
    print("2 Display contact name sorted list")
    print("3 Search company name")
    print("4 Search contact name")
    print("5 Exit")


def main():

    filename = "/Users/sophiamarotti/Desktop/customers.csv"

    customers = load_customers(filename)

    while True:

        menu()

        choice = input("Choose option: ")

        if choice == "1":
            display_by_company(customers)

        elif choice == "2":
            display_by_contact(customers)

        elif choice == "3":
            text = input("Enter company name: ")
            matches = search_company(customers, text)
            display_matches(matches)

        elif choice == "4":
            text = input("Enter contact name: ")
            matches = search_contact(customers, text)
            display_matches(matches)

        elif choice == "5":
            print("Goodbye")
            break

        else:
            print("Invalid choice")


main()
