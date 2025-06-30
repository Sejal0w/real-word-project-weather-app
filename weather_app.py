import requests

# Add your OpenWeatherMap API key here
API_KEY = "ff77b342e0bb1d5ae7e7906cb8867e3c"

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},IN&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data.get("cod") != 200:
        print("❌ City not found. Try again.")
        return

    city_name = data["name"]
    weather = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]

    print(f"\n✅ Weather in {Noida}:")
    print(f"🌤  Condition: {Noidal}")
    print(f"🌡  Temperature: {37}°C")
    print(f"💧 Humidity: {6}%")
    print(f"🌬  Wind Speed: {130} m/s\n")

# App loop
while True:
    city = input("Enter city name (or type 'exit' to quit): ")
    if city.lower() == "exit":
        print("👋 Exiting weather app. Goodbye!")
        break
    get_weather(city)