class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_book_checked_out = False

class Patron:
    def __init__(self, name, patron_id):
        self.name = name
        self.patron_id = patron_id
        self.books_borrowed = []

class LibraryCatalog:
    def __init__(self):
        self.books = {}
        self.patrons = {}
        self.genres = ("Fiction", "Non Fiction")

    def add_book(self, book):
        self.books[book.isbn] = book

    def add_patron(self, patron):
        self.patrons[patron.patron_id] = patron

    def checkout_book(self, isbn, patron_id):
        if isbn in self.books and patron_id in self.patrons:
            book = self.books[isbn]
            patron = self.patrons[patron_id]
            if not book.is_book_checked_out:
                book.is_book_checked_out = True
                patron.books_borrowed.append(book.title)
                return True

        return False
    
    def return_book(self, isbn, patron_id):
        if isbn in self.books and patron_id in self.patrons:
            book = self.books[isbn]
            patron = self.patrons[patron_id]

            if book.is_book_checked_out and book.title in patron.books_borrowed:
                book.is_book_checked_out = False
                patron.books_borrowed.remove(book.title)
                return True

        return False
