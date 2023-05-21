import requests

def get_weather_data(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    return data

def test_get_weather_data():
    api_key = "92ca2f9a961e3bf6464967e5d8ee3106"  
    city = "Nonexistent City"  
 
    data = get_weather_data(api_key, city)

    assert "cod" in data
    assert "message" in data

    
    assert data.get("cod") == "404"  
    assert data.get("message") == "city not found"  

    print("Test get_weather_data_invalid_city passed.")

def test_display_weather():
    data = {
        "name": "Warsaw",
        "main": {
            "temp": 20,
            "feels_like": 18,
            "humidity": 70
        },
        "weather": [
            {
                "description": "Cloudy"
            }
        ],
        "wind": {
            "speed": 5
        },
        "sys": {
            "sunrise": 1621345324,
            "sunset": 1621396958
        }
    }
    unit = "Celsius"

    if "cod" in data and data["cod"] != "404":
        display_weather(data, None, unit)

    print("Test display_weather passed.")


test_get_weather_data()
test_display_weather()
