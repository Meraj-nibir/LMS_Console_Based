import Library as library
class User:

    def search_book(self, library, title):
        library.search_book(title)

    def check_availability(self, library, title):
        if title in library.books and library.books[title]['quantity'] > 0:
            print(f"{title} is available.")
        else:
            print(f"{title} is not available.")

    def issue_book(self, library, title):
        library.issue_book(title)