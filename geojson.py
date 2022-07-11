import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)

# Enter location: Richmond Hill,ON,Canada
# Retrieving http://py4e-data.dr-chuck.net/json?address=Richmond+Hill%2CON%2CCanada&key=42
# Retrieved 1799 characters
# {
#     "results": [
#         {
#             "address_components": [
#                 {
#                     "long_name": "Richmond Hill",
#                     "short_name": "Richmond Hill",
#                     "types": [
#                         "locality",
#                         "political"
#                     ]
#                 },
#                 {
#                     "long_name": "Regional Municipality of York",
#                     "short_name": "Regional Municipality of York",
#                     "types": [
#                         "administrative_area_level_2",
#                         "political"
#                     ]
#                 },
#                 {
#                     "long_name": "Ontario",
#                     "short_name": "ON",
#                     "types": [
#                         "administrative_area_level_1",
#                         "political"
#                     ]
#                 },
#                 {
#                     "long_name": "Canada",
#                     "short_name": "CA",
#                     "types": [
#                         "country",
#                         "political"
#                     ]
#                 }
#             ],
#             "formatted_address": "Richmond Hill, ON, Canada",
#             "geometry": {
#                 "bounds": {
#                     "northeast": {
#                         "lat": 43.9777849,
#                         "lng": -79.37100989999999
#                     },
#                     "southwest": {
#                         "lat": 43.829353,
#                         "lng": -79.485593
#                     }
#                 },
#                 "location": {
#                     "lat": 43.8828401,
#                     "lng": -79.4402808
#                 },
#                 "location_type": "APPROXIMATE",
#                 "viewport": {
#                     "northeast": {
#                         "lat": 43.9777849,
#                         "lng": -79.37100989999999
#                     },
#                     "southwest": {
#                         "lat": 43.829353,
#                         "lng": -79.485593
#                     }
#                 }
#             },
#             "place_id": "ChIJMxcpNkkqK4gR7UKx1gp2AVI",
#             "types": [
#                 "locality",
#                 "political"
#             ]
#         }
#     ],
#     "status": "OK"
# }
# lat 43.8828401 lng -79.4402808
# Richmond Hill, ON, Canada
