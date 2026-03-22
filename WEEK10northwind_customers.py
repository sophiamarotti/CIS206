"""
"""
Northwind Customers Program
Author: Sophia Marotti
Course: CIS 206 - Applied Programming

Description:
This program reads the Northwind customers CSV file and stores each
customer as a dictionary inside a list.

The program allows the user to:
1. Display customers sorted by company name
2. Display customers sorted by contact name
3. Search by company name (full or partial)
4. Search by contact name (full or partial)
"""

The program avoids global variables by passing data through functions.
It includes input validation, parameter validation, and function documentation.
"""

import csv


def load_customers(filename):
    """
    Read customer data from a CSV file and return a list of dictionaries.

    Parameters:
        filename (str): The name of the CSV file to read.

    Returns:
        list: A list of customer dictionaries.

    Raises:
        TypeError: If filename is not a string.
        FileNotFoundError: If the file cannot be found.
        ValueError: If the file is empty or missing required fields.
    """
    if not isinstance(filename, str):
        raise TypeError("filename must be a string")

    customers = []

    required_fields = {"customerID", "companyName", "contactName", "phone"}

    with open(filename, mode="r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)

        if reader.fieldnames is None:
            raise ValueError("The file is empty or does not contain headers.")

        file_fields = set(reader.fieldnames)
        if not required_fields.issubset(file_fields):
            raise ValueError("The CSV file is missing one or more required fields.")

        for row in reader:
            customers.append(dict(row))

    return customers


def sort_customers(customers, key_name):
    """
    Return a new list of customers sorted by the given dictionary key.

    Parameters:
        customers (list): A list of customer dictionaries.
        key_name (str): The dictionary key to sort by.

    Returns:
        list: A sorted list of customer dictionaries.

    Raises:
        TypeError: If customers is not a list or key_name is not a string.
        ValueError: If key_name is empty.
    """
    if not isinstance(customers, list):
        raise TypeError("customers must be a list")
    if not isinstance(key_name, str):
        raise TypeError("key_name must be a string")
    if key_name.strip() == "":
        raise ValueError("key_name cannot be empty")

    return sorted(customers, key=lambda customer: customer.get(key_name, "").lower())


def display_sorted_by_company(customers):
    """
    Display company name, contact name, and phone number for all customers
    sorted by company name.

    Parameters:
        customers (list): A list of customer dictionaries.
    """
    sorted_customers = sort_customers(customers, "companyName")

    print("\nCustomers Sorted by Company Name")
    print("-" * 70)
    for customer in sorted_customers:
        print(
            f"Company: {customer.get('companyName', 'N/A')}\n"
            f"Contact: {customer.get('contactName', 'N/A')}\n"
            f"Phone:   {customer.get('phone', 'N/A')}\n"
        )


def display_sorted_by_contact(customers):
    """
    Display contact name, company name, and phone number for all customers
    sorted by contact name.

    Parameters:
        customers (list): A list of customer dictionaries.
    """
    sorted_customers = sort_customers(customers, "contactName")

    print("\nCustomers Sorted by Contact Name")
    print("-" * 70)
    for customer in sorted_customers:
        print(
            f"Contact: {customer.get('contactName', 'N/A')}\n"
            f"Company: {customer.get('companyName', 'N/A')}\n"
            f"Phone:   {customer.get('phone', 'N/A')}\n"
        )


def search_customers(customers, field_name, search_text):
    """
    Search customers for a partial match in the specified field.

    Parameters:
        customers (list): A list of customer dictionaries.
        field_name (str): The field to search, such as 'companyName' or 'contactName'.
        search_text (str): The text to search for.

    Returns:
        list: A list of matching customer dictionaries.

    Raises:
        TypeError: If parameters are of invalid types.
        ValueError: If field_name or search_text is empty.
    """
    if not isinstance(customers, list):
        raise TypeError("customers must be a list")
    if not isinstance(field_name, str):
        raise TypeError("field_name must be a string")
    if not isinstance(search_text, str):
        raise TypeError("search_text must be a string")
    if field_name.strip() == "":
        raise ValueError("field_name cannot be empty")
    if search_text.strip() == "":
        raise ValueError("search_text cannot be empty")

    matches = []
    search_text = search_text.lower()

    for customer in customers:
        value = customer.get(field_name, "")
        if search_text in value.lower():
            matches.append(customer)

    return matches


def display_labeled_records(matches):
    """
    Display matching customer records with labeled fields.

    Parameters:
        matches (list): A list of matching customer dictionaries.
    """
    if not matches:
        print("\nNo matching records found.")
        return

    print(f"\nFound {len(matches)} matching record(s):")
    print("-" * 70)

    for customer in matches:
        print(f"Customer ID:  {customer.get('customerID', 'N/A')}")
        print(f"Company Name: {customer.get('companyName', 'N/A')}")
        print(f"Contact Name: {customer.get('contactName', 'N/A')}")
        print(f"Contact Title:{customer.get('contactTitle', 'N/A')}")
        print(f"Address:      {customer.get('address', 'N/A')}")
        print(f"City:         {customer.get('city', 'N/A')}")
        print(f"Region:       {customer.get('region', 'N/A')}")
        print(f"Postal Code:  {customer.get('postalCode', 'N/A')}")
        print(f"Country:      {customer.get('country', 'N/A')}")
        print(f"Phone:        {customer.get('phone', 'N/A')}")
        print(f"Fax:          {customer.get('fax', 'N/A')}")
        print("-" * 70)


def get_menu_choice():
    """
    Prompt the user for a menu choice and validate the input.

    Returns:
        str: A validated menu choice from 1 to 5.
    """
    valid_choices = {"1", "2", "3", "4", "5"}

    while True:
        print("\nNorthwind Customers Menu")
        print("1. Display all customers sorted by company name")
        print("2. Display all customers sorted by contact name")
        print("3. Search by company name")
        print("4. Search by contact name")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice in valid_choices:
            return choice

        print("Invalid choice. Please enter a number from 1 to 5.")


def get_nonempty_input(prompt):
    """
    Prompt the user until a non-empty string is entered.

    Parameters:
        prompt (str): The prompt message.

    Returns:
        str: A non-empty user input string.

    Raises:
        TypeError: If prompt is not a string.
    """
    if not isinstance(prompt, str):
        raise TypeError("prompt must be a string")

    while True:
        value = input(prompt).strip()
        if value != "":
            return value
        print("Input cannot be empty. Please try again.")


def run_program(customers):
    """
    Run the menu-driven customer interface.

    Parameters:
        customers (list): A list of customer dictionaries.
    """
    if not isinstance(customers, list):
        raise TypeError("customers must be a list")

    while True:
        choice = get_menu_choice()

        if choice == "1":
            display_sorted_by_company(customers)

        elif choice == "2":
            display_sorted_by_contact(customers)

        elif choice == "3":
            search_text = get_nonempty_input("Enter company name or part of name: ")
            matches = search_customers(customers, "companyName", search_text)
            display_labeled_records(matches)

        elif choice == "4":
            search_text = get_nonempty_input("Enter contact name or part of name: ")
            matches = search_customers(customers, "contactName", search_text)
            display_labeled_records(matches)

        elif choice == "5":
            print("Goodbye!")
            break


def main():
    """
    Main function for the Northwind Customers program.
    """
    filename = "customers.csv"

    try:
        customers = load_customers(filename)
        run_program(customers)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except ValueError as error:
        print(f"Data error: {error}")
    except TypeError as error:
        print(f"Type error: {error}")


if __name__ == "__main__":
    main()
