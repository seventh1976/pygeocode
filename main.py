from geopy.geocoders import Nominatim


geolocator = Nominatim(user_agent="geoapiExercises")
location = geolocator.geocode("Perak")
print("Country Name: ", location)
