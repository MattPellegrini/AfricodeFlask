import requests
import json

# Configuration
LONGITUDE = 17.869737068977376
LATITUDE = 59.39684468828176
API_KEY = "143e77f45d1f421ca6a4d703f16da71a"
URL = f'https://api.openweathermap.org/data/2.5/onecall?lat={LATITUDE}&lon={LONGITUDE}&units=metric&appid={API_KEY}'

response = requests.get(URL)
weather_json = response.json()
print(json.dumps(weather_json, sort_keys=True, indent=4))