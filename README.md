# Submission Project Dicoding Analisis Data dengan Python

## Deskripsi
Project ini bertujuan untuk menganalisis sistem penyewaan sepeda yang otomatis, yang memungkinkan pengguna untuk menyewa sepeda dari satu lokasi dan mengembalikannya di lokasi lain.

## Dataset
Dataset terdiri dari catatan dua tahun dari sistem Capital Bikeshare di Washington D.C. (2011-2012) yang berisi informasi yang berkaitan dengan kondisi lingkungan dan musiman yang mempengaruhi perilaku penyewaan sepeda. Data ini mencakup dua file utama:

 **hour.csv**: Data penyewaan sepeda yang teragregasi secara jam (17.379 catatan).
- **day.csv**: Data penyewaan sepeda yang teragregasi secara harian (731 catatan).

Kedua file tersebut berisi beberapa kolom, termasuk:
- **instant**: indeks catatan.
- **dteday**: tanggal.
- **season**: musim (1: semi, 2: musim panas, 3: gugur, 4: musim dingin).
- **yr**: tahun (0: 2011, 1: 2012).
- **mnth**: bulan (1 hingga 12).
- **hr**: jam (0 hingga 23) - tidak ada di day.csv.
- **holiday**: apakah hari tersebut adalah hari libur atau tidak.
- **weekday**: hari dalam seminggu.
- **workingday**: apakah hari tersebut adalah hari kerja.
- **weathersit**: kondisi cuaca yang berbeda.
- **temp**: suhu terstandardisasi.
- **atemp**: suhu yang dirasakan.
- **hum**: kelembapan terstandardisasi.
- **windspeed**: kecepatan angin terstandardisasi.
- **casual**: jumlah pengguna biasa.
- **registered**: jumlah pengguna terdaftar.
- **cnt**: jumlah total penyewaan sepeda.

## Struktur Direktori
- **dashboard**: berisi `main.py` dan `main_data.csv` untuk membuat dashboard melalui Streamlit
- **data**: berisi data mentah bike share dataset
- **notebook.ipynb**: file notebook analisis

## Instalasi
Clone repository ini ke komputer lokal Anda menggunakan perintah berikut:
```bash
git clone https://github.com/wandadesi/dicoding_submission.git
Instalasi Library
pip install streamlit
pip install -r dashboard/requirements.txt
```

## Penggunaan
Masuk ke direktori proyek (Local):
cd dicoding/dashboard/
streamlit run main.py

## Akses web streamlit
https://dicodingsubmission-bike.streamlit.app/
