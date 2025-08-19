import json
import os

from book import Book

class Library:
    def __init__(self, filename='library.json'):
        self.filename = filename
        self.books = []
        self.load_books()

    def load_books(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                data = json.load(f)
                self.books = [Book(b['title'], b['author'], b['isbn']) for b in data]
        else:
            self.books = []

    def save_books(self):
        data = [{'title': b.title, 'author': b.author, 'isbn': b.isbn} for b in self.books]
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=4)

    def add_book(self, book):
        self.books.append(book)
        self.save_books()

    def remove_book(self, isbn):
        book = self.find_book(isbn)
        if book:
            self.books.remove(book)
            self.save_books()
            return True
        return False

    def list_books(self):
        return [str(book) for book in self.books]

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None