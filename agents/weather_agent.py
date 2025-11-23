from tools.weather_tool import get_weather

class WeatherAgent:
    def fetch_weather(self, lat, lon):
        return get_weather(lat, lon)
