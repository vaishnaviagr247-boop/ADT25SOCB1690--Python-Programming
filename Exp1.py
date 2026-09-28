class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True  # Book is available by default

    def __str__(self):
        return f"'{self.title}' by {self.author}"


class Patron:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []  # List to store borrowed Book objects

    def __str__(self):
        return self.name


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added to library: {book}")

    def register_patron(self, patron):
        self.patrons.append(patron)
        print(f"Registered patron: {patron}")

    def borrow_book(self, patron, book):

        # Check whether the book belongs to this library
        if book not in self.books:
            print(f"Error: {book} does not belong to this library.")
            return

        # Check whether the patron is registered
        if patron not in self.patrons:
            print(f"Error: {patron} is not a registered patron.")
            return

        # Check book availability
        if book.available:
            book.available = False
            patron.borrowed_books.append(book)
            print(f"{patron} successfully borrowed {book}.")
        else:
            print(f"Error: {book} is currently not available.")

    def return_book(self, patron, book):

        # Check whether the patron is registered
        if patron not in self.patrons:
            print(f"Error: {patron} is not a registered patron.")
            return

        # Check whether patron has borrowed this book
        if book not in patron.borrowed_books:
            print(f"Error: {patron} has not borrowed {book}.")
            return

        # Return the book
        book.available = True
        patron.borrowed_books.remove(book)
        print(f"{patron} successfully returned {book}.")


# Creating library
library = Library()

# Creating books
book1 = Book("Python Programming", "John Smith")
book2 = Book("Data Structures", "Robert Brown")

# Creating patrons
patron1 = Patron("Harish")
patron2 = Patron("Rahul")

# Adding books
library.add_book(book1)
library.add_book(book2)

# Registering patrons
library.register_patron(patron1)
library.register_patron(patron2)

# Borrowing books
library.borrow_book(patron1, book1)

# Trying to borrow the same book again
library.borrow_book(patron2, book1)

# Returning the book
library.return_book(patron1, book1)

# Borrowing it again
library.borrow_book(patron2, book1)