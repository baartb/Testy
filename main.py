import requests
from datetime import datetime

def get_weather_data(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    forecast_url = "http://api.openweathermap.org/data/2.5/forecast"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    forecast_response = requests.get(forecast_url, params=params)
    data = response.json()
    forecast_data = forecast_response.json()
    return data, forecast_data



def display_weather(data, forecast_data, unit):
    if data["cod"] != "404":
        current_temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]
        sunrise = datetime.fromtimestamp(data["sys"]["sunrise"]).strftime("%H:%M:%S")
        sunset = datetime.fromtimestamp(data["sys"]["sunset"]).strftime("%H:%M:%S")

        print(f"Current Weather in {data['name']}:")
        print(f"Temperature: {current_temperature}°{unit}")
        print(f"Feels Like: {feels_like}°{unit}")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description}")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Sunrise: {sunrise}")
        print(f"Sunset: {sunset}")

        forecast_list = forecast_data["list"]
        print("\nWeather Forecast:")
        for forecast in forecast_list:
            forecast_date = datetime.fromtimestamp(forecast["dt"]).strftime("%Y-%m-%d")
            forecast_time = datetime.fromtimestamp(forecast["dt"]).strftime("%H:%M:%S")
            forecast_temperature = forecast["main"]["temp"]
            forecast_description = forecast["weather"][0]["description"]
            icon_code = forecast["weather"][0]["icon"]
           
            print(f"\nDate: {forecast_date}")
            print(f"Time: {forecast_time}")
            print(f"Temperature: {forecast_temperature}°{unit}")
            print(f"Description: {forecast_description}")
      

    else:
        print("City not found.")

def main():
    api_key = "92ca2f9a961e3bf6464967e5d8ee3106"  
    city = input("Enter city name: ")
    unit = input("Enter unit (Celsius/Fahrenheit): ").lower()
    while unit not in ["celsius", "fahrenheit"]:
        unit = input("Invalid unit. Please enter Celsius or Fahrenheit: ").lower()

    data, forecast_data = get_weather_data(api_key, city)
    if unit == "fahrenheit":
        data["main"]["temp"] = (data["main"]["temp"] * 9/5) + 32
        data["main"]["feels_like"] = (data["main"]["feels_like"] * 9/5) + 32
        forecast_list = forecast_data["list"]
        for forecast in forecast_list:
            forecast["main"]["temp"] = (forecast["main"]["temp"] * 9/5) + 32

    display_weather(data, forecast_data, unit)

if __name__ == "__main__":
    main()
