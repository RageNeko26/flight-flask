# Module datettime untuk mendapatkan informasi tanggal
import datetime

# Module Dataset penerbangan
import flights

# Import module Flask karena kali program python ini akan diintegrasikan sebagai API
# Pastikan sebelumnya sudah menginstall module Flask dengan perintah "pip install flask"
from flask import Flask, request, render_template
app = Flask(__name__)

# NIM
NIM = 21524015

# Untuk mendapat digit terakhir dari NIM
A = NIM%10

# Gunakan fungsi round() untuk membulatkan angka desimal
B = round(A/2)

# Gunakan object dari datetime untuk mendapatkan informasi tanggal
date = datetime.date(2023,B,A*3)

# Mengurutkan dataset Penerbangan dari yang termurah sampai termahal
sorted_flights = sorted(flights.list_flights, key=lambda k:k["price"])

## Integrasi ke dalam aplikasi web
@app.route('/')
def index():
    flights_popular = flights.popular
    return render_template('index.html',data_popular = flights_popular)

@app.route('/flights')
def flights_view():
    data_date = str(date)
    from_destination = sorted_flights[0]["from"]
    
    return render_template('flights.html', data_date = data_date, from_destination = from_destination)

@app.route('/profile')
def profile():
    return render_template('profile_view.html', data_nim=NIM)

@app.route('/api/flights')
def api_flights():
    return sorted_flights

@app.route('/api/nearest_destination')
def near():
    return flights.nearest

@app.route('/api/popular')
def popular():
    return flights.popular

@app.route('/api/cheapest')
def cheap():
    return sorted_flights[0]

if __name__ == '__main__':
    app.run(debug=True)


# print("List Penerbangan")
# print("Tanggal : " + str(date))
# for data in sorted_flights:
#     print(data["from"] + " - " + data["to"] + "\n----------")