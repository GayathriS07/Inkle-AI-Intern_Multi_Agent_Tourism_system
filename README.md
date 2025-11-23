# Inkle-AI-Intern_Multi_Agent_Tourism_system
A multi-agent tourism assistant built in Python. It reads natural language queries, detects the location, and fetches real-time weather and tourist spots using Nominatim, Open-Meteo, and Overpass APIs. The parent agent coordinates child agents to return only the information the user asks for.
This is a small Python project where I built a tourism assistant powered by multiple agents. You can ask it about a place you want to visit, and based on your question, it will fetch:

the current weather, or

tourist attractions, or

both (if you ask for both)

All API data is fetched live — nothing is hard-coded.

What the project does:

When you type something like:

“I’m going to go to Bangalore, what’s the temperature there?”

or

“Plan my trip to Kodaikanal. What places should I visit?”

The system will:

Figure out the place you’re talking about

Convert the place name into latitude/longitude

Depending on what you asked, call the:

Weather Agent → gets weather from Open-Meteo

Places Agent → gets attractions from OpenStreetMap

Return only the information you asked for

If the place doesn’t exist, it politely tells you:

“I don’t know this place exists.”

How it’s designed:

The project follows a simple multi-agent pattern:

Parent Agent (Controller)

Reads the user’s message

Detects the location

Decides which child agents should run (weather or places)

Combines the final answer

Weather Agent

Uses the Open-Meteo API to fetch real weather data.

Places Agent

Uses two APIs:

Nominatim → to get coordinates from the place name

Overpass API → to find nearby tourist attractions

This separation keeps everything clean and modular.

Tech used:

Python

Requests

Simple regex-based intent + location extraction

Open-Meteo API

Nominatim (OpenStreetMap)

Overpass API

No paid APIs, no API keys needed.

📁 Project Structure multi_agent_tourism/ │ ├── main.py ├── requirements.txt ├── README.md │ ├── agents/ │ ├── parent.py │ ├── weather_agent.py │ └── places_agent.py │ └── tools/ ├── weather_tool.py └── places_tool.py

How to run it:

Install the requirements:

pip install -r requirements.txt

Run the project:

python main.py

Start typing messages such as:

I'm going to go to Bangalore, what is the temperature there?

I'm planning a trip to Kodaikanal, show me some places to visit.

Example Output Location detected: Kodaikanal

Weather Info: It is currently 17°C with windspeed 4.8 km/h.

Tourist Places: Coaker's Walk Kodaikanal Lake Pillar Rocks Bryant Park Kurunji Temple
