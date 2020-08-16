import urllib.request, urllib.parse, urllib.error
import ssl
import json
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = 'http://py4e-data.dr-chuck.net/comments_413021.json'
data = urllib.request.urlopen(url).read().decode()

info = json.loads(data)
print('User count:', len(info))
count = 0
print(info.keys())
print(json.dumps(info, indent=4))
for item in info['comments']:
    count += item['count']
print(count)
