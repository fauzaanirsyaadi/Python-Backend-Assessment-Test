# Python-Backend-Assessment-Test
Tabungan API
Buatlah sebuah HTTP Server menggunakan REST API yang memiliki API minimal
sebagai berikut:
1. /daftar : API untuk registrasi nasabah baru dengan payload JSON berisi field
nama , nik , dan no_hp . API akan memberikan balikan dengan status 200 dan
payload JSON berisi field no_rekening yang berisi data nomor rekening nasabah.
Jika nik atau no_hp sudah digunakan, API akan memberikan balikan status 400
dan payload JSON berisi field remark yang berisi deskripsi kesalahan terkait
data yg dikirim.
2. /tabung : API untuk nasabah menabung dengan payload JSON berisi field
no_rekening , dan nominal . API akan memberikan balikan dengan status 200 dan
payload JSON berisi field saldo yang berisi data saldo nasabah saat ini. Jika
no_rekening tidak dikenali, API akan memberikan balikan status 400 dan payload
JSON berisi field remark yang berisi deskripsi kesalahan terkait data yg dikirim.
3. /tarik : API untuk nasabah menarik dana nasabah dengan payload JSON berisi
field no_rekening dan nominal . API akan memberikan balikan dengan status 200
dan payload JSON berisi field saldo yang berisi data saldo nasabah saat ini.
Jika no_rekening tidak dikenali atau saldo tidak cukup, API akan memberikan
balikan status 400 dan payload JSON berisi field remark yang berisi deskripsi
kesalahan terkait data yg dikirim.
4. /saldo/{no_rekening} : API untuk melihat data saldo nasabah dengan path
parameter bernama no_rekening berisi nomor rekening nasabah. API akan
memberikan balikan dengan status 200 dan payload JSON berisi field saldo
yang berisi data saldo nasabah saat ini. Jika no_rekening tidak dikenali, API akan
memberikan balikan status 400 dan payload JSON berisi field remark yang berisi
deskripsi kesalahan terkait data yg dikirim.

Catatan:

HTTP Server dibuat menggunakan Python micro-framework HTTP
(direkomendasikan menggunakan FastAPI ).
Data disimpan di dalam file JSON atau di dalam database PostgreSQL
menggunakan docker container.
Code disimpan di public repository GitLab atau Github.
API tantangan (tidak wajib dikerjakan):
/mutasi/{no_rekening} : API untuk melihat daftar mutasi nasabah dengan path
parameter bernama no_rekening berisi nomor rekening nasabah. API akan
memberikan balikan dengan status 200 dan payload JSON berisi field mutasi
berupa array yang berisi dictionary data mutasi nasabah dengan field waktu ,
kode_transaksi (C untuk tabung, D untuk tarik), dan nominal . Jika no_rekening
tidak dikenali, API akan memberikan balikan status 400 dan payload JSON
berisi field remark yang berisi deskripsi kesalahan terkait data yg dikirim.

Kriteria Penilaian:
1. Variable naming
2. Data structure
3. Control flow & looping
4. Type annotation
5. Python object
6. Module structure
7. REST API structure
