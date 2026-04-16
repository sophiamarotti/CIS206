import json
import xml.etree.ElementTree as ET


def json_library():
    print("\n--- JSON DATA ---")

    with open("books.json", "r") as file:
        data = json.load(file)

    for book in data["books"]:
        print(f'{book["title"]} - {book["author"]} ({book["year"]})')

    while True:
        title = input("\nEnter a book title (or 'q' to quit): ")

        if title.lower() == "q":
            break

        found = False

        for book in data["books"]:
            if book["title"].lower() == title.lower():
                print(f'Found: {book["title"]} - {book["author"]} ({book["year"]})')
                found = True
                break

        if not found:
            print(f'"{title}" not found')


def xml_library():
    print("\n--- XML DATA ---")

    tree = ET.parse("books.xml")
    root = tree.getroot()

    for book in root.findall("book"):
        title = book.find("title").text
        author = book.find("author").text
        year = book.find("year").text
        print(f"{title} - {author} ({year})")

    while True:
        title_input = input("\nEnter a book title (or 'q' to quit): ")

        if title_input.lower() == "q":
            break

        found = False

        for book in root.findall("book"):
            title = book.find("title").text

            if title.lower() == title_input.lower():
                author = book.find("author").text
                year = book.find("year").text
                print(f"Found: {title} - {author} ({year})")
                found = True
                break

        if not found:
            print(f'"{title_input}" not found')


def main():
    json_library()
    xml_library()


if __name__ == "__main__":
    main()
