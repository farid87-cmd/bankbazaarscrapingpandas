#import librares

import pandas as pd
import requests
from bs4 import BeautifulSoup

#send request

url = 'https://www.bankbazaar.com/reviews.html'
datas = []
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')

#read review text html
items = soup.findAll('li', 'review-box')
for item in items:
    desc = item.find('div', 'text_here review-desc-more').text
    author_name = item.find('span', 'js-author-name').text
    bank_name = item.find('div', 'review-bank-title').find('img').get('alt')
    print('Description     : ', desc)
    print('User Name     : ', author_name)
    print('Bank   : ', bank_name, '\n')
    datas.append([desc, author_name, bank_name])
    #create dataframe
