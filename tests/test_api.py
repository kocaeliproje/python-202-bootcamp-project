import pytest
import os
from fastapi.testclient import TestClient
from api import app
from library import Library

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def temp_library():
    lib = Library('temp_library.json')
    yield lib
    if os.path.exists('temp_library.json'):
        os.remove('temp_library.json')

def test_list_books(client, temp_library, mocker):
    mocker.patch('api.library', temp_library)  # Global library'yi temp_library ile değiştir
    response = client.get("/books")
    assert response.status_code == 200
    assert response.json() == {"books": []}

def test_add_book(client, temp_library, mocker):
    mocker.patch('api.library', temp_library)
    book_data = {"title": "Test Book", "author": "Test Author", "isbn": "1234567890"}
    response = client.post("/books", json=book_data)
    assert response.status_code == 200
    assert response.json()["message"] == "Kitap eklendi"
    assert response.json()["book"] == "Test Book by Test Author (ISBN: 1234567890)"

def test_add_book_by_isbn_success(client, mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "ISBN:9780141182803": {
            "title": "1984",
            "authors": [{"name": "George Orwell"}]
        }
    }
    mocker.patch('httpx.get', return_value=mock_response)
    response = client.post("/books/isbn?isbn=9780141182803")
    assert response.status_code == 200
    assert response.json()["message"] == "Kitap eklendi"
    assert response.json()["book"] == "1984 by George Orwell (ISBN: 9780141182803)"

def test_add_book_by_isbn_not_found(client, mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {}
    mocker.patch('httpx.get', return_value=mock_response)
    response = client.post("/books/isbn?isbn=9999999999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Kitap bulunamadı"

def test_remove_book(client, temp_library, mocker):
    mocker.patch('api.library', temp_library)
    book = {"title": "Test Book", "author": "Test Author", "isbn": "1234567890"}
    client.post("/books", json=book)
    response = client.delete("/books/1234567890")
    assert response.status_code == 200
    assert response.json()["message"] == "Kitap silindi"

def test_find_book(client, temp_library, mocker):
    mocker.patch('api.library', temp_library)
    book = {"title": "Test Book", "author": "Test Author", "isbn": "1234567890"}
    client.post("/books", json=book)
    response = client.get("/books/1234567890")
    assert response.status_code == 200
    assert response.json()["book"] == "Test Book by Test Author (ISBN: 1234567890)"

def test_find_book_not_found(client, temp_library, mocker):
    mocker.patch('api.library', temp_library)
    response = client.get("/books/9999999999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Kitap bulunamadı"