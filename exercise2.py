import json
import urllib.request, urllib.parse, urllib.error

serviceurl = "http://py4e-data.dr-chuck.net/geojson?"

address = input('Enter location: ')
url = serviceurl + urllib.parse.urlencode(
    {'address': address})

print('Retrieving', url)

uh = urllib.request.urlopen(url)

data = uh.read()
info = json.loads(data)
print('Retrieved', len(data), 'characters')

print("Place id " + info['results'][0]['place_id'])
