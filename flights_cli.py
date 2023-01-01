# Module datettime untuk mendapatkan informasi tanggal
import datetime

# Dataset penerbangan
list_flights = [
    {
       "id" : "F0001",
       "from" : "Jakarta",
       "to" : "Semarang",
       "price" : 688200,
       "airline" : "Lion Air",
},
    {
        "id" : "F0002",   
        "from" : "Jakarta",
        "to" : "Yogyakarta",
        "price" : 567430,
        "airline" : "Citilink",
},
    {
        "id" : "F0003",
        "from" : "Jakarta",
        "to" : "Denpasar",
        "price" : 733000,
        "airline" : "TransNusa",
},
    {
        "id" : "F0004",
        "from" : "Jakarta",
        "to" : "Surabaya",
        "price" : 784700,
        "airline" : "Batik Air",
},
    {
        "id" : "F0005",
        "from" : "Jakarta",
        "to" : "Makassar",
        "price" : 1400430,
        "airline" : "Sriwijaya Air",
 }
]

nearest = [list_flights[0],list_flights[1]]
popular = [list_flights[2], list_flights[3]]

# NIM
NIM = 21524015

# Untuk mendapat digit terakhir dari NIM
A = NIM%10

# Gunakan fungsi round() untuk membulatkan angka desimal
B = round(A/2)

# Gunakan object dari datetime untuk mendapatkan informasi tanggal
date = datetime.date(2023,B,A*3)

# Mengurutkan daftar penerbangan dari yang termurah sampai termahal
sorted_flights = sorted(list_flights, key=lambda k:k["price"])

print("Selamat datang di Program Penerbangan Sederhana")
print("Pilihlah salah satu dari pilihan berikut")
print("1) List penerbangan")
print("2) Penerbangan terdekat")
print("3) Penerbangan termurah")

options = input("Masukkan opsi angka : ")

if options == "1":
    print("-" * 20)
    print("Daftar Penerbangan")
    print("Tanggal : " + str(date))
    print("-" * 35)
    for data in sorted_flights:
        print(data["from"] + " - " + data["to"] + ": Rp."+ str(data["price"]) + "\n-----------------------------------")
elif options == "2":
    print("-" * 35)
    print("Daftar Penerbangan Terdekat")
    print("Tanggal : " + str(date))
    print("-" * 35)
    for data in nearest:
        print(data["from"] + " - " + data["to"] + ": Rp."+ str(data["price"]) + "\n-----------------------------------")
elif options == "3":
    print("-" * 35)
    print("Berikut rute penerbangan termurah")
    print("Tanggal : " + str(date))
    print("-" * 35)
    print(sorted_flights[0]["from"] + " - " + sorted_flights[0]["to"] + ": Rp." +str(sorted_flights[0]["price"]))
    print("-" * 35)
else:    
    print("Pilihan tidak ditemukan")
    
    


