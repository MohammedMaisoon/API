import requests
from datetime import datetime
response = requests.get(url=YOUR END POINT)
response.raise_for_status()
data = response.json()
iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])
my_lat = YOUR LATITUDE
my_long = YOUR LONGITUDE
parameters = {
    "lat":my_lat,
    "lng":my_long,
    "formatted":0,
}
response = requests.get(url=YOUR ENDPOINT,params=parameters)
response.raise_for_status()
data = response.json()
print(data)



