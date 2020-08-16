import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

url0 = 'http://py4e-data.dr-chuck.net/comments_42.xml'
url1 = 'http://py4e-data.dr-chuck.net/comments_413020.xml'
url = input('Enter location: ')
print('Retrieving', url)
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = serviceurl + urllib.parse.urlencode(parms)
data = urllib.request.urlopen(url).read()
print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data)
counts = tree.findall('.//count')

count = 0
for item in counts:
    count += int(item.text)

print('Sum:', count)
