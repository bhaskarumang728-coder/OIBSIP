import requests

# --------------- Weather Fetching Function -----------------
def get_weather(city_name):
    API_KEY = "802e7173ad3a4031fa36fa13497438d2"  # Replace with your OpenWeatherMap API key
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"  
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric"  # To get temperature in Celsius
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if response.status_code == 200:
            city = data["name"]
            country = data["sys"]["country"]
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            condition = data["weather"][0]["description"].title()

            print(f"\nWeather in {city}, {country}:")
            print(f"Temperature: {temp}°C")
            print(f"Humidity: {humidity}%")
            print(f"Condition: {condition}")
        else:
            print(f"\n❌ Error: {data.get('message', 'Unable to fetch weather.')}")
    except Exception as e:
        print(f"\n❌ Something went wrong: {e}")

# ------------------- Main Program -------------------------
def main():
    print("=== Weather App ===")
    city = input("Enter city name: ").strip()
    if city:
        get_weather(city)
    else:
        print("❌ Please enter a valid city name.")

if _name_ == "_main_":
    main()