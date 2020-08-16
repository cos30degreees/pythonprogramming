# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file
import requests
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

webpage_response = requests.get('http://py4e-data.dr-chuck.net/known_by_Tyllor.html')


url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
count = int(input('Enter count: '))
position = int(input('Enter position: '))


names = []

py4e_links = soup.find_all('a')


while count > len(names):
    for tag in py4e_links:
        if tag == py4e_links[position-1]:
            print('Retrieving: {}'.format(tag.get('href')))
            webpage = requests.get(tag.get('href'))
            name = BeautifulSoup(webpage.content, "html.parser")
            py4e_links = name('a')
            names.append(tag.contents[0])
print(names)

# Retrieve all of the anchor tags
