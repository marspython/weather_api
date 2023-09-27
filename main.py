import requests

api_key = "f7bdd3196704576b38f6127ec6217ff0"
api_url = "https://api.openweathermap.org/data/2.5/weather"

city = input("What city do you want to check the weather in?: ")

response = requests.get(
    url = api_url,
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
)

weather_data = response.json()
print("The temperature in",city, "is", weather_data["main"]["temp"])