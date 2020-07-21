cara menggunakan
- pastikan sudah install python
- masuk folder virtualenv kemudian ketik source bin/activate untuk menjalankan virtual environment
- buat file .flaskenv kemudian copy isi .flaskenv.dist .flaskenv
- edit .flaskenv sesuaikan dengan db yang akan digunakan
- ketik pip install -r requirements.txt untuk install apa saja yg di butuhkan di project
- untuk buat migrationsnya bisa ketik flask db init kemudian ketik flask db migrate -m "komentar" dan flask db upgrade untuk migrate (seperti laravel)