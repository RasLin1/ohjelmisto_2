import requests
from geopy.geocoders import Nominatim

key = "e660192f564b0a27b33a9b8237f1488f"
geocode = Nominatim(user_agent="weather_app").geocode(input("Kerro paikkakunnan nimi: "))
response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={geocode.latitude}&lon={geocode.longitude}&units=metric&appid={key}").json()
print(f"Lämpö kohteesa on: {response["main"]["temp"]:.2f} °C")