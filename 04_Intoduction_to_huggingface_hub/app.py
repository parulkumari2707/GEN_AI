import streamlit as st
import requests

# Set up API key and base URL
API_KEY = "ce6b189b71e3e5d00019ab59aa6e38fe"  # Replace with your OpenWeatherMap API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Function to fetch weather data
def get_weather_data(city="Chennai"):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()

# Streamlit app
def main():
    st.title("Weather App for Chennai")
    data = get_weather_data()
    if data["cod"] == 200:
        weather = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        st.write(f"Weather in Chennai: {weather}")
        st.write(f"Temperature: {temperature}°C")
        st.write(f"Humidity: {humidity}%")
        st.write(f"Wind Speed: {wind_speed} m/s")
    else:
        st.write("Failed to fetch weather data for Chennai.")

if __name__ == "__main__":
    main()