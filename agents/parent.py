import re
from agents.weather_agent import WeatherAgent
from agents.places_agent import PlacesAgent


class ParentAgent:
    def __init__(self):
        self.weather_agent = WeatherAgent()
        self.places_agent = PlacesAgent()

    def extract_place(self, text):
        if not text or text.strip() == "":
            return None  # Prevent crash!

        # Extract capitalized words (Bangalore, New York)
        match = re.findall(r'[A-Z][a-zA-Z]+', text)
        if match:
            return " ".join(match)

        # fallback: last word if not empty
        words = text.split()
        if len(words) > 0:
            return words[-1]

        return None

    def user_wants_weather(self, text):
        text = text.lower()
        weather_keywords = ["weather", "temperature", "climate", "rain", "hot", "cold"]
        return any(word in text for word in weather_keywords)

    def user_wants_places(self, text):
        text = text.lower()
        place_keywords = ["tour", "trip", "visit", "places", "spots", "travel", "plan"]
        return any(word in text for word in place_keywords)

    def process(self, user_query):
        if not user_query or user_query.strip() == "":
            return "Please type something 🙂"

        place = self.extract_place(user_query)
        if not place:
            return "I couldn't detect any place. Try again."

        coords = self.places_agent.locate_place(place)
        if coords is None:
            return f"I don't know this place exists: {place}"

        lat, lon = coords

        # Build response dynamically
        response = f"**Location detected:** {place}\n\n"

        # Weather only if asked
        if self.user_wants_weather(user_query):
            weather_info = self.weather_agent.fetch_weather(lat, lon)
            response += f"**Weather Info:**\n{weather_info}\n\n"

        # Tourist places only if asked
        if self.user_wants_places(user_query):
            place_list = self.places_agent.list_places(lat, lon)
            places_output = "\n".join(place_list) if place_list else "No attractions found."
            response += f"**Tourist Places:**\n{places_output}\n\n"

        # If user asked neither
        if not self.user_wants_weather(user_query) and not self.user_wants_places(user_query):
            response += "Ask me about weather or tourist places 😊"

        return response.strip()
