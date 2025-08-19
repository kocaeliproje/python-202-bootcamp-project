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

def test_add_book_by_isbn_success(temp_library, mocker):
    # Mock httpx.get
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "ISBN:9780141182803": {
            "title": "1984",
            "authors": [{"name": "George Orwell"}]
        }
    }
    mocker.patch('httpx.get', return_value=mock_response)
    book, error = temp_library.add_book_by_isbn("9780141182803")
    assert book is not None
    assert error is None
    assert book.title == "1984"
    assert book.author == "George Orwell"
    assert book.isbn == "9780141182803"
    assert len(temp_library.books) == 1

def test_add_book_by_isbn_not_found(temp_library, mocker):
    # Mock httpx.get
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {}
    mocker.patch('httpx.get', return_value=mock_response)
    book, error = temp_library.add_book_by_isbn("9999999999")
    assert book is None
    assert error == "Kitap bulunamadı."
    assert len(temp_library.books) == 0