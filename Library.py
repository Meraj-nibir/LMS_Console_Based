class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, title, author, quantity):
        if title in self.books:
            self.books[title]['quantity'] += quantity
        else:
            self.books[title] = {'author': author, 'quantity': quantity}

    def remove_book(self, title):
        if title in self.books:
            del self.books[title]
            print(f"{title} has been removed from the library.")
        else:
            print(f"{title} is not in the library.")

    def search_book(self, title):
        if title in self.books:
            book_info = self.books[title]
            print(f"Title: {title}, Author: {book_info['author']}, Quantity: {book_info['quantity']}")
        else:
            print(f"{title} is not in the library.")

    def update_availability(self, title, new_quantity):
        if title in self.books:
            self.books[title]['quantity'] = new_quantity
        else:
            print(f"{title} is not in the library.")

    def issue_book(self, title):
        if title in self.books and self.books[title]['quantity'] > 0:
            self.books[title]['quantity'] -= 1
            print(f"{title} has been issued to you.")
        else:
            print(f"{title} is not available for issue.")

