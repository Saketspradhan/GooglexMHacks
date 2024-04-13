import googlemaps

api_key = "AIzaSyB_mFu6xlXLPLAXXeJ9NXv3j9OYsKUeboc"

def location_to_coordinates(location):
    gmaps = googlemaps.Client(key=api_key)
    geocode_result = gmaps.geocode(location)

    # Access latitude and longitude from the first result
    latitude = geocode_result[0]["geometry"]["location"]["lat"]
    longitude = geocode_result[0]["geometry"]["location"]["lng"]

    return str(latitude), str(longitude)