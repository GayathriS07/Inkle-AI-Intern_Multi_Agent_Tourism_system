import requests

def get_weather(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True
    }

    response = requests.get(url, params=params)

    try:
        data = response.json()
    except:
        return "Weather data unavailable."

    if "current_weather" not in data:
        return "Weather data unavailable."

    w = data["current_weather"]
    return f"It is currently {w['temperature']}°C with windspeed {w['windspeed']} km/h."
