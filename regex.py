import os
import re


with open('regex_sum_42sample.txt','r') as file:
    text = file.read()
    print(text)
    numbers = re.findall('[0-9]+',text)

