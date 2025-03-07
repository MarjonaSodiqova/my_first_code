import requests

def get_weather(city):
    api_key = "4833b659c5084d39f021aec02be5afc4"  
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        print(f"Weather in {city}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Weather: {data['weather'][0]['description']}")
    else:
        print(f"Error fetching weather data. Status code: {response.status_code}")
        print(f"Response: {response.text}")

get_weather("Tashkent")
