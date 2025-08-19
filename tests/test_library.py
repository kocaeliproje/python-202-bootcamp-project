import pytest
import os
from library import Library
from book import Book

@pytest.fixture
def temp_library():
    lib = Library('temp_library.json')
    yield lib
    if os.path.exists('temp_library.json'):
        os.remove('temp_library.json')

def test_add_book(temp_library):
    book = Book("Test Title", "Test Author", "123456")
    temp_library.add_book(book)
    assert len(temp_library.books) == 1
    assert temp_library.books[0].title == "Test Title"

def test_remove_book(temp_library):
    book = Book("Test Title", "Test Author", "123456")
    temp_library.add_book(book)
    assert temp_library.remove_book("123456") == True
    assert len(temp_library.books) == 0