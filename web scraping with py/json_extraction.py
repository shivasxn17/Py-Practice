import json
import urllib.request, urllib.parse, urllib.error

address = input('Enter location: ')

try:
  if len(address) < 1: raise("location invalid")
except Exception as e:
  print("Invalid location")

print('Retrieving', address)
uh = urllib.request.urlopen(address)
data = uh.read()
comments = json.loads(data)
print('Retrieved', len(data), 'characters')
