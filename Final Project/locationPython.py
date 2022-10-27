from geopy.geocoders import Nominatim
 
loc = Nominatim(user_agent="GetLoc")
 
placename = input("Enter the place you wish to see location details: ")
getLoc = loc.geocode(placename)
 
print(getLoc.address)
 
print("Latitude = ", getLoc.latitude, "\n")
print("Longitude = ", getLoc.longitude)