import bs4 as bs
import urllib.request
import pandas as pd


source = urllib.request.urlopen('https://pythonprogramming.net/sitemap.xml').read()
soup = bs.BeautifulSoup(source,'lxml')

print(soup)


for url in soup.find_all('loc'):
	print(url.text)