import requests

def get_coordinates(place):
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": place,
        "format": "json",
        "limit": 1
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (AI Tourism Student Project)"
    }

    response = requests.get(url, params=params, headers=headers)

    try:
        data = response.json()
    except:
        return None

    if len(data) == 0:
        return None

    return float(data[0]["lat"]), float(data[0]["lon"])


def get_tourist_places(lat, lon, radius=3000):
    overpass_url = "https://overpass-api.de/api/interpreter"

    query = f"""
    [out:json];
    (
      node["tourism"](around:{radius},{lat},{lon});
      way["tourism"](around:{radius},{lat},{lon});
      rel["tourism"](around:{radius},{lat},{lon});
    );
    out center;
    """

    headers = {
        "User-Agent": "Mozilla/5.0 (AI Tourism Student Project)"
    }

    response = requests.post(overpass_url, data=query, headers=headers)

    try:
        data = response.json()
    except:
        return []

    names = []
    for element in data.get("elements", []):
        if "tags" in element and "name" in element["tags"]:
            names.append(element["tags"]["name"])

    return list(dict.fromkeys(names))[:5]  # unique top 5
