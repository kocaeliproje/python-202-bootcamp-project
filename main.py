from library import Library
from book import Book

def main():
    lib = Library()
    while True:
        print("\n1. Kitap Ekle\n2. Kitap Sil\n3. Kitapları Listele\n4. Kitap Ara\n5. Çıkış")
        choice = input("Seçiminiz: ")
        if choice == '1':
            title = input("Başlık: ")
            author = input("Yazar: ")
            isbn = input("ISBN: ")
            book = Book(title, author, isbn)
            lib.add_book(book)
            print("Kitap eklendi.")
        elif choice == '2':
            isbn = input("Silinecek ISBN: ")
            if lib.remove_book(isbn):
                print("Kitap silindi.")
            else:
                print("Kitap bulunamadı.")
        elif choice == '3':
            books = lib.list_books()
            if books:
                for b in books:
                    print(b)
            else:
                print("Kütüphane boş.")
        elif choice == '4':
            isbn = input("Aranacak ISBN: ")
            book = lib.find_book(isbn)
            if book:
                print(book)
            else:
                print("Kitap bulunamadı.")
        elif choice == '5':
            break
        else:
            print("Geçersiz seçim.")

if __name__ == "__main__":
    main()