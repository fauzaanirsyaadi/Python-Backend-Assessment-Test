##API Documentation

/daftar
Request
POST /daftar
Content-Type: application/json

{
  "nama": "John Doe",
  "nik": "1234567890123456",
  "no_hp": "081234567890"
}

Response
Success:

 
200 OK
Content-Type: application/json

{
  "no_rekening": "1234567890"
}
Error (nik already used):

 
400 Bad Request
Content-Type: application/json

{
  "remark": "NIK already used"
}
Error (no_hp already used):

 
400 Bad Request
Content-Type: application/json

{
  "remark": "No. HP already used"
}
/tabung
Request
 
POST /tabung
Content-Type: application/json

{
  "no_rekening": "1234567890",
  "nominal": 500000
}
Response
Success:

 
200 OK
Content-Type: application/json

{
  "saldo": 500000
}
Error (no_rekening not found):

 
400 Bad Request
Content-Type: application/json

{
  "remark": "No. rekening not found"
}
/tarik
Request
 
POST /tarik
Content-Type: application/json

{
  "no_rekening": "1234567890",
  "nominal": 1000000
}
Response
Success:

 
200 OK
Content-Type: application/json

{
  "saldo": 500000
}
Error (no_rekening not found):

 
400 Bad Request
Content-Type: application/json

{
  "remark": "No. rekening not found"
}
Error (saldo not enough):

 
400 Bad Request
Content-Type: application/json

{
  "remark": "Saldo tidak cukup"
}
/saldo/{no_rekening}
Request
 
GET /saldo/1234567890
Response
Success:

 
200 OK
Content-Type: application/json

{
  "saldo": 500000
}
Error (no_rekening not found):

 
400 Bad Request
Content-Type: application/json

{
  "remark": "No. rekening not found"
}
/mutasi/{no_rekening}
Request
 
GET /mutasi/1234567890
Response
Success:

 
200 OK
Content-Type: application/json

{
  "mutasi": [
    {
      "waktu": "2022-03-15 09:00:00",
      "kode_transaksi": "C",
      "nominal": 1000000
    },
    {
      "waktu": "2022-03-16 10:00:00",
      "kode_transaksi": "D",
      "nominal": 500000
    }
  ]
}
Error (no_rekening not found):

 
400 Bad Request
Content-Type: application/json

{
  "remark": "No. rekening not found"
}