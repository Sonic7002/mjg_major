# main method contains ui and method calls
from library import Library
from utils import clear_screen, pause

def main():
    obj = Library()
    while True:
        clear_screen()
        print("MENU".center(50, "*"))
        print(
            """1. Add book
2. Edit stock of a book
3. Remove book
4. Issue book
5. Return Book
6. Search for a book
7. Display all books
8. Exit"""
        )
        try:
            choice = int(input("Enter your choice (1 to 8):"))
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
            pause()
            continue
        match choice:
            case 1:
                try:
                    name = input("Enter book name: ")
                    ID = int(input("Enter book ID: "))
                    author = input("Enter author name: ")
                    total = int(input("Enter number of books: "))
                    obj.add_book(name, ID, author, total)
                    print("Entry successful!")
                except ValueError as e:
                    print(e)
                pause()
            case 2:
                try:
                    ID = int(input("Enter book ID: "))
                    added = int(input("Enter number of books added: "))
                    obj.add_stock(ID, added)
                    print("Updated successfully!")
                except ValueError as e:
                    print(e)
                pause()
            case 3:
                try:
                    ID = int(input("Enter ID of book to be removed: "))
                    obj.remove(ID)
                    print("Removed successfully!")
                except ValueError as e:
                    print(e)
                pause()
            case 4:
                try:
                    ID = int(input("Enter ID of book to be issued: "))
                    obj.issue_book(ID)
                    print("Issued successfully!")
                except ValueError as e:
                    print(e)
                pause()
            case 5:
                try:
                    ID = int(input("Enter ID of book to be returned: "))
                    obj.return_book(ID)
                    print("Returned successfully!")
                except ValueError as e:
                    print(e)
                pause()
            case 6:
                key = input("Enter key for searching: ")
                result = obj.search(key)
                if result == []:
                    print("No results found")
                else:
                    for index, item in enumerate(result, start=1):
                        print(
                            f"{index}. ID({item['ID']}) {item['name']} by {item['author']}"
                        )
                pause()
            case 7:
                data = obj.list_books()
                if data == []:
                    print("No books available")
                else:
                    for i, item in enumerate(data, start=1):
                        print(f"{i}. Name = {item['name']}")
                        print("ID:", item["ID"])
                        print("Author:", item["author"])
                        print("Available", item["available"])
                        print("Total", item["total"])
                        print("\n")
                pause()
            case 8:
                print("Exiting...")
                break
            case _:
                print("Invalid input. Please enter values given in menu.")
                pause()

if __name__ == "__main__" :
    main()