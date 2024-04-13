import os
from dotenv import load_dotenv
import googlemaps

load_dotenv()
def location_to_coordinates(location):
    # Get the API key from the environment variable
    gmaps_api_key = os.getenv("GMAPS_API_KEY")
    gmaps = googlemaps.Client(key=gmaps_api_key)
    geocode_result = gmaps.geocode(location)

    # Access latitude and longitude from the first result
    latitude = geocode_result[0]["geometry"]["location"]["lat"]
    longitude = geocode_result[0]["geometry"]["location"]["lng"]

    return str(latitude), str(longitude)

print(location_to_coordinates("Toronto"))