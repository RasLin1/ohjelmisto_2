import requests
from geopy.geocoders import Nominatim

key = "e660192f564b0a27b33a9b8237f1488f"
geolocator = Nominatim(user_agent="weather_app")
geocode = geolocator.geocode(input("Kerro paikkakunnan nimi: "))
response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={geocode.latitude}&lon={geocode.longitude}&appid={key}")
data = response.json()
temp_celsius = (data["main"]["temp"] -273.15)
print(f"Lämpö kohteesa on: {temp_celsius:.2f} °C")