from tools.places_tool import get_coordinates, get_tourist_places

class PlacesAgent:
    def locate_place(self, place):
        return get_coordinates(place)

    def list_places(self, lat, lon):
        return get_tourist_places(lat, lon)
