import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

address = input('Enter location')

try:
  if len(address) < 1: raise("location invalid")
except Exception as e:
  print("Invalid location")

print('Retrieving', address)
uh = urllib.request.urlopen(address)
data = uh.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data.decode())
comments = tree.findall('.//comment')
