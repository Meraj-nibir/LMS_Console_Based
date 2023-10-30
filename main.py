import Library as Library;
import User as User;
def main():
    library = Library.Library()

    while True:
        print("\nLibrary Management System")
        print("Which is your role?")
        print("1. Librarian")
        print("2. Customer")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice=="1":
            while True:
                print("1. Add a book")
                print("2. Remove a book")
                print("3. Search for a book")
                print("4. Update book availability")
                print("5. Check book availability")
                print("5. Issue a book")
                print("6. Exit")

                choice = input("Enter your choice: ")

                if choice == "1" :
                    title = input("Enter book title: ")
                    author = input("Enter author: ")
                    quantity = int(input("Enter quantity: "))
                    library.add_book(title, author, quantity)

                elif choice == "2" :
                    title = input("Enter book title to remove: ")
                    library.remove_book(title)

                elif choice == "3":
                    title = input("Enter book title to search: ")
                    Library.search_book(library, title)

                elif choice == "4":
                    title = input("Enter book title to update availability: ")
                    new_quantity = int(input("Enter new quantity: "))
                    library.update_availability(title, new_quantity)

                elif choice == "6":
                    print("Goodbye!")
                    break

                else:
                    print("Invalid choice. Please try again.")
                continue
        elif choice == "2":
            while True:
                print("1. Search for a book")
                print("2. Check book availability")
                print("3. Issue a book")
                print("4. Exit")

                choice = input("Enter your choice: ")

                if choice == "1":
                    title = input("Enter book title to search: ")
                    Library.search_book(library, title)

                elif choice == "2":
                    title = input("Enter book title to check availability: ")
                    User.check_availability(library, title)

                elif choice == "3":
                    title = input("Enter book title to issue: ")
                    User.issue_book(library, title)

                elif choice == "4":
                    print("Goodbye!")
                    break

                else:
                    print("Invalid choice. Please try again.")
                continue

        elif choice == "3":
                    print("Goodbye!")
                    break
        else:
            print("Invalid choice. Please try again.")
        continue


if __name__ == "__main__":
    main()