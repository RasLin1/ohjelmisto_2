import requests
from geopy.geocoders import Nominatim

key = "e660192f564b0a27b33a9b8237f1488f"
geolocator = Nominatim(user_agent="weather_app")
geocode = geolocator.geocode(input("Kerro paikkakunnan nimi: "))
response = requests.get(f"https://api.openweathermap.org/data/3.0/onecall?lat={geocode[0]}&lon={geocode[1]}&appid={key}")
data = response.json()
temp = data["temp"]
print(f"Lämpö kohteesa on: {temp} kelvin")