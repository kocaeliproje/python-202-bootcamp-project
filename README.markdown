# Python 202 Bootcamp Projesi: Kütüphane Yönetim Sistemi

Bu proje, **Python 202 Bootcamp** kapsamında geliştirilen bir kütüphane yönetim sistemidir. Proje, bir terminal uygulaması ve FastAPI tabanlı bir web API'si ile kitapları yönetmek için kapsamlı bir çözüm sunar. Kullanıcılar, kitapları manuel olarak ekleyebilir, Open Library API üzerinden ISBN ile kitap bilgisi çekebilir, kitapları listeleyebilir, arayabilir ve silebilir. Tüm işlevsellik, birim testleri ile doğrulanmıştır.

## Proje Özellikleri
- **Terminal Uygulaması**: Kullanıcı dostu bir komut satırı arayüzü ile kitap yönetimi.
- **Web API**: FastAPI ile geliştirilmiş, RESTful endpoint'ler sunan bir API.
- **Open Library Entegrasyonu**: ISBN ile kitap bilgilerini otomatik olarak çekme.
- **Kalıcı Veri Depolama**: Kitap bilgileri `library.json` dosyasında saklanır.
- **Kapsamlı Testler**: Hem kütüphane modülü hem de API için birim testleri (`pytest` ile).

## Teknoloji Yığını
- **Python**: 3.12+
- **FastAPI**: Web API'si için.
- **Uvicorn**: ASGI sunucusu.
- **Pydantic**: Veri doğrulama için.
- **Httpx**: Open Library API istekleri için.
- **Pytest**: Birim testleri için.
- **Pytest-mock**: API ve HTTP isteklerini test etmek için.

## Ön Koşullar
- Python 3.12 veya üstü (`python --version`)
- Git (`git --version`)

## Kurulum
1. **Repoyu Klonlayın**:
   ```bash
   git clone https://github.com/kocaeliproje/python-202-bootcamp-project.git
   cd python-202-bootcamp-project
   ```
2. **Sanal Ortam Oluşturun ve Aktive Edin**:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # Windows
   # veya: source venv/bin/activate  # Linux/Mac
   ```
3. **Bağımlılıkları Kurun**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Terminal Uygulamasını Çalıştırın**:
   ```bash
   python main.py
   ```
5. **Web API'sini Çalıştırın**:
   ```bash
   uvicorn api:app --reload
   ```

## Kullanım

### Terminal Uygulaması
`main.py` ile çalışan terminal arayüzü, aşağıdaki işlemleri destekler:
1. **Kitap Ekleme (Manuel)**: Başlık, yazar ve ISBN girerek kitap ekleyin.
2. **Kitap Ekleme (API ile)**: ISBN ile Open Library'den kitap bilgisi çekin.
3. **Kitap Silme**: ISBN ile kitap silin.
4. **Kitapları Listeleme**: Kütüphanedeki tüm kitapları görün.
5. **Kitap Arama**: ISBN ile kitap arayın.
6. **Çıkış**: Uygulamadan çıkın.

### Web API
API, `http://127.0.0.1:8000` adresinde çalışır. Endpoint'ler:
- **GET /**: API hoş geldiniz mesajı (`{"message": "Python 202 Bootcamp API. Try /books endpoint."}`).
- **GET /books**: Tüm kitapları listele (`{"books": [...]}`).
- **POST /books**: Manuel kitap ekle (JSON: `{"title": "Test", "author": "Author", "isbn": "123"}`).
- **POST /books/isbn?isbn=9780141182803**: ISBN ile kitap ekle.
- **DELETE /books/{isbn}**: ISBN ile kitap sil.
- **GET /books/{isbn}**: ISBN ile kitap ara.
- **Swagger UI**: `http://127.0.0.1:8000/docs` adresinde interaktif API dokümantasyonu.

**Örnek ISBN**: `9780141182803` (George Orwell - 1984).

## Testler
Proje, `pytest` ile kapsamlı bir şekilde test edilmiştir. Testleri çalıştırmak için:
```bash
pytest tests/ -v
```
- **Test Kapsamı**:
  - `tests/test_library.py`: Kütüphane modülü için testler (kitap ekleme, silme, ISBN ile ekleme).
  - `tests/test_api.py`: API endpoint'leri için testler (listeleme, ekleme, silme, arama).

Tüm testler (11 test) başarılı bir şekilde geçmiştir.

## Proje Aşamaları
- **Aşama 1**: Terminal tabanlı kütüphane yönetim sistemi (`main.py`, `library.py`, `book.py`).
- **Aşama 2**: Open Library API entegrasyonu ve birim testleri (`test_library.py`).
- **Aşama 3**: FastAPI ile web API'si ve ek testler (`api.py`, `test_api.py`).

## Dosya Yapısı
```
python-202-bootcamp-project/
├── .gitignore
├── requirements.txt
├── LICENSE
├── README.md
├── library.json
├── venv/
├── book.py
├── library.py
├── main.py
├── api.py
├── tests/
│   ├── test_library.py
│   ├── test_api.py
```

## Sorun Giderme
- **API Çalışmıyor**: `uvicorn api:app --reload` komutunu çalıştırın ve logları kontrol edin.
- **Test Hataları**: `pytest tests/ -v` ile testleri çalıştırın, hata mesajlarını inceleyin.
- **Bağımlılıklar**: `pip install -r requirements.txt` ile tüm bağımlılıkları kurun.
- **GitHub**: Proje, `https://github.com/kocaeliproje/python-202-bootcamp-project` adresinde barındırılıyor.

## Gelecek Geliştirmeler
- **SQLite Entegrasyonu**: `library.json` yerine SQLite veritabanı.
- **Docker**: Uygulamanın containerize edilmesi.
- **JWT Kimlik Doğrulama**: API güvenliği için.
- **CI/CD**: GitHub Actions ile otomatik testler.

## Katkılar
Bu proje, Python 202 Bootcamp kapsamında geliştirilmiştir. Sorularınız veya katkılarınız için lütfen GitHub üzerinden iletişime geçin.