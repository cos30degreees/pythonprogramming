import bs4 as bs
import urllib.request
import pandas as pd


source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(source,'lxml')


# # table = soup.table
# table = soup.find('table')


# table_rows = table.find_all('tr')

# for tr in table_rows:
# 	td = tr.find_all('td')
# 	row = [i.text for i in td]
# 	print(row)

# USING PANDAS TO READ TABLES AND PRINT THEM 
# dfs = pd.read_html('https://pythonprogramming.net/parsememcparseface/')

# for df in dfs:
# 	print(df)