import bs4 as bs
import urllib.request


source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()


soup = bs.BeautifulSoup(source,'lxml')
# print(soup)
# print(soup.title)
# print(soup.find_all('p'))
for paragraph in soup.find_all('p'):
	print(paragraph.text)
# print(soup.get_text())
for url in soup.find_all('a'):
	print(url.get('href'))


# gets all links in navigation bar 
nav = soup.nav
for url in nav.find_all('a'):
	print(url.get('href'))

# print the body of the website
body = soup.body
for paragraph in body.find_all('p'):
	print(paragraph.text)


# print all items in between beautiful soup objects in this case content body
for div in soup.find_all('div',class_='body'):
	print(div.text)

