from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from library import Library
from book import Book

app = FastAPI()

class BookCreate(BaseModel):
    title: str
    author: str
    isbn: str

library = Library()

@app.get("/")
async def root():
    return {"message": "Python 202 Bootcamp API. Try /books endpoint."}

@app.get("/books")
async def list_books():
    books = library.list_books()
    return {"books": books}

@app.post("/books")
async def add_book(book: BookCreate):
    new_book = Book(book.title, book.author, book.isbn)
    library.add_book(new_book)
    return {"message": "Kitap eklendi", "book": str(new_book)}

@app.post("/books/isbn")
async def add_book_by_isbn(isbn: str):
    book, error = library.add_book_by_isbn(isbn)
    if book:
        return {"message": "Kitap eklendi", "book": str(book)}
    raise HTTPException(status_code=404, detail=error)

@app.delete("/books/{isbn}")
async def remove_book(isbn: str):
    if library.remove_book(isbn):
        return {"message": "Kitap silindi"}
    raise HTTPException(status_code=404, detail="Kitap bulunamadı")

@app.get("/books/{isbn}")
async def find_book(isbn: str):
    book = library.find_book(isbn)
    if book:
        return {"book": str(book)}
    raise HTTPException(status_code=404, detail="Kitap bulunamadı")