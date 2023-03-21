#Tabungan API
Cara Menjalankan Proyek
Berikut langkah-langkah untuk menjalankan proyek:

Clone repositori ini.

Install semua dependensi dengan menjalankan perintah `pip install -r requirements.txt`.

Jalankan aplikasi dengan menjalankan perintah `uvicorn main:app --reload`.

server berjalan pada http://localhost:8000.

API Endpoint
Berikut adalah daftar API endpoint yang tersedia pada proyek ini:

1. /daftar: API untuk registrasi nasabah baru dengan payload JSON berisi field nama, nik, dan no_hp.
2. /tabung: API untuk nasabah menabung dengan payload JSON berisi field no_rekening dan nominal.
3. /tarik: API untuk nasabah menarik dana dengan payload JSON berisi field no_rekening dan nominal.
4. /saldo/{no_rekening}: API untuk melihat data saldo nasabah dengan path parameter no_rekening.
5. /mutasi/{no_rekening}: API untuk melihat daftar mutasi nasabah dengan path parameter no_rekening.

Untuk dokumentasi lebih lengkap mengenai penggunaan API, dapat dilihat pada file API_Documentation.md.
