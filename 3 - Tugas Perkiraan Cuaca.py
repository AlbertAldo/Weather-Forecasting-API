import requests
from bs4 import BeautifulSoup
import json

"""
Tugas
1.
- Menentukan Perkiraan Cuaca

Input :
Masukkan Nama Kota :
Output :
- Nama Kota :
- Suhu : (Celcius)
- Keadaan Cuaca : 
- Koordinat Kota Anda :
    Lat :
    Lng :
- Humidity Level :
- Kecepatan Angin :

Error Handling:
Kota yang anda masukkan tidak terdaftar
Format kota yang anda masukkan salah (jika angka, float atau simbol)
"""

a1 = str(input("Silahkan Masukkan Nama Kota Anda : "))
a = a1.lower()
b = a.replace(" ","+")
c = a.split(" ")

tampung = ""
for i in c:
    tampung += i

try:
    if tampung.isalpha() != True:
        print("Format kota yang anda masukkan salah")
    else:
        url = "https://api.openweathermap.org/data/2.5/weather?q="+b+"&appid=4a77f0a0c6ec180f15c1c406fcb66667"
        data = requests.get(url)
        cuaca = data.json()

        # cuaca = {'coord': {'lon': 106.8451, 'lat': -6.2146},
        # 'weather': [{'id': 721, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '50d'}],
        # 'base': 'stations',
        # 'main': {'temp': 301.72, 'feels_like': 306.3, 'temp_min': 301.15, 'temp_max': 302.15, 'pressure': 1012, 'humidity': 78}, 
        # 'visibility': 5000, 
        # 'wind': {'speed': 2.06, 'deg': 250}, 
        # 'clouds': {'all': 40}, 
        # 'dt': 1615349013, 
        # 'sys': {'type': 1, 'id': 9383, 'country': 'ID', 'sunrise': 1615330674, 'sunset': 1615374493}, 
        # 'timezone': 25200, 
        # 'id': 1642911, 
        # 'name': 'Jakarta', 
        # 'cod': 200}

        # # print(cuaca['name'])
        kota = cuaca['name']
        # # print(cuaca['main']['temp'])
        kelvin = cuaca['main']['temp']
        # # print(fahrenheit)
        suhu = kelvin-273

        # # print(cuaca['weather'][0]['main'])
        # # print(cuaca['weather'][0]['description'])
        keadaan1 = cuaca['weather'][0]['main']
        keadaan2 = cuaca['weather'][0]['description']

        # # print(cuaca['coord']['lon'])
        # # print(cuaca['coord']['lat'])
        lng = cuaca['coord']['lon']
        lat = cuaca['coord']['lat']

        # print(cuaca['main']['humidity'])
        # print(cuaca['wind']['speed'])
        # print(cuaca['wind']['deg'])
        humidity = cuaca['main']['humidity']
        windspeed = cuaca['wind']['speed']
        winddeg = cuaca['wind']['deg']

        print("• Nama Kota :", kota.title())
        print("• Suhu :", round(suhu,2),"°C")
        print("• Keadaan Cuaca :", keadaan1.title(), ", dengan Deskripsi :", keadaan2.title())
        print("• Koordinat Kota Anda :")
        print("  - Lat :", lat)
        print("  - Lng :", lng)
        print("• Humidity Level :", humidity,"%")
        print("• Kecepatan Angin :", windspeed, "km/h, dengan Derajat :", winddeg,"°")
except:
    print("Kota yang anda masukkan tidak terdaftar !")
