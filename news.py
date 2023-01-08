import requests
from bs4 import BeautifulSoup
import csv
import random


# cnbc.com Crawler
html = requests.get('https://www.cnbc.com/')
soup = BeautifulSoup(html.content, 'lxml')
list = []
for row in soup.findAll('div', attrs={'class': 'LatestNews-headlineWrapper'}):
  table = {}  # Dictionary to store all values
  author = 'N/A'
  
  try:
    date = row.find('span', attrs='LatestNews-wrapper').find('time', attrs='LatestNews-timestamp').text.strip().replace(',', '')
  except:
    pass
    
  title = row.find('a', attrs='LatestNews-headline').text.strip().replace(',', '')
  link = row.find('a', attrs='LatestNews-headline')['href']
  
  table['source'] = "cnbc.com"
  table['title'] = title.replace(',', '')
  table['author'] = author.replace(',', '')
  table['date'] = date.strip().replace(',', '')
  table['link'] = link
  
  list.append(table)
  

# Motley Fool Crawler
html = requests.get('https://www.fool.com/investing-news/')
soup = BeautifulSoup(html.content, 'lxml')

for row in soup.findAll('div', attrs={'class': 'flex py-12px text-gray-1100'}):
  table = {}  # Dictionary to store all values
  title = row.find('a', attrs='text-gray-1100').find('h5', attrs='self-center mb-6 font-medium md:text-h5 text-md md:mb-4px').text.replace(',', '')
  author = row.find('div', attrs='text-sm text-gray-800 mb-2px md:mb-8px').find('a', attrs='').text.replace(',', '')
  date = row.find('div', attrs='text-sm text-gray-800 mb-2px md:mb-8px').text.strip().find('2022')
  date = row.find('div', attrs='text-sm text-gray-800 mb-2px md:mb-8px').text.strip()[:date+4].replace(',', '')
  link = 'https://fool.com' + row.find('a', attrs='text-gray-1100')['href']

  table['source'] = "fool.com"
  table['title'] = title.replace(',', '')
  table['author'] = author.replace(',', '')
  table['date'] = date.strip().replace(',', '')
  table['link'] = link
  
  list.append(table)
  

# MarketWatch Crawler
html = requests.get('https://www.marketwatch.com/')
soup = BeautifulSoup(html.content, 'lxml')
for row in soup.findAll('h3', attrs={'class': 'article__headline'}):
  table = {}  # Dictionary to store all values
  try:
    if row.find('a', attrs='link').text.strip()[:5] != 'Picks' or 'Opinion' not in row.find('a', attrs='link').text.strip():
      title = row.find('a', attrs='link').text.strip()
  except:
    pass
  author = 'N/A'
  date = 'Today'
  try:
    link = row.find('a', attrs='link')['href']
  except:
    pass

  table['source'] = "marketwatch.com"
  table['title'] = title.replace(',', '')
  table['author'] = author.replace(',', '')
  table['date'] = date.strip().replace(',', '')
  
  if link[:4] != 'http':
    table['link'] = 'https://www.marketwatch.com' + link
  else:
    table['link'] = link
  
  list.append(table)
  

# Yahoo Finance Crawler
html = requests.get('https://finance.yahoo.com/news/')
soup = BeautifulSoup(html.content, 'lxml')
for row in soup.findAll('h3', attrs={'class': 'Mb(5px)'}):
  table = {}  # Dictionary to store all values
  try:
    title = row.find('a', attrs='js-content-viewer wafer-caas Fw(b) Fz(18px) Lh(23px) LineClamp(2,46px) Fz(17px)--sm1024 Lh(19px)--sm1024 LineClamp(2,38px)--sm1024 mega-item-header-link Td(n) C(#0078ff):h C(#000) LineClamp(2,46px) LineClamp(2,38px)--sm1024 not-isInStreamVideoEnabled').text.strip().replace(',', '')
  except:
    pass
  author = 'N/A'
  date = 'Today'
  try:
    link = row.find('a', attrs='js-content-viewer wafer-caas Fw(b) Fz(18px) Lh(23px) LineClamp(2,46px) Fz(17px)--sm1024 Lh(19px)--sm1024 LineClamp(2,38px)--sm1024 mega-item-header-link Td(n) C(#0078ff):h C(#000) LineClamp(2,46px) LineClamp(2,38px)--sm1024 not-isInStreamVideoEnabled')['href']
  except:
    pass

  table['source'] = "finance.yahoo.com"
  table['title'] = title.replace(',', '')
  table['author'] = author.replace(',', '')
  table['date'] = date.strip().replace(',', '')
  table['link'] = 'https://finance.yahoo.com' + link
  
  list.append(table)
  

# Morningstar Crawler
html = requests.get('https://www.morningstar.com/stocks')
soup = BeautifulSoup(html.content, 'lxml')
for row in soup.findAll('div', attrs={'class': 'mdc-grid-item__content'}):
  table = {}  # Dictionary to store all values
  try:
    title = row.find('a', attrs='mdc-link mdc-grid-item__title mdc-grid-item__title--link').text.strip().replace(',', '')
  except:
    pass
  author = row.find('div', attrs='mdc-grid-item__metadata').text.strip().replace(',', '')
  date = 'Today'
  try:
    link = row.find('a', attrs='mdc-link mdc-grid-item__title mdc-grid-item__title--link')['href']
  except:
    pass

  table['source'] = "morningstar.com"
  table['title'] = title.replace(',', '')
  table['author'] = author.replace(',', '')
  table['date'] = date.strip().replace(',', '')
  table['link'] = 'https://www.morningstar.com' + link
  
  list.append(table)


# world-financial-times Crawler
html = requests.get('https://world-financial-times.com/?cat=4')
soup = BeautifulSoup(html.content, 'lxml')
for row in soup.findAll('div', attrs={'class': 'other-news-post-content'}):
  table = {}  # Dictionary to store all values
  title = row.find('a', attrs='').text.strip().replace(',', '')
  author = 'N/A'
  date = 'Today'
  link = row.find('a', attrs='')['href']

  table['source'] = "world-financial-times.com"
  table['title'] = title.replace(',', '')
  table['author'] = author.replace(',', '')
  table['date'] = date.strip().replace(',', '')
  table['link'] = link
  
  list.append(table)
  

# thestreet.com Crawler
html = requests.get('https://www.thestreet.com/')
soup = BeautifulSoup(html.content, 'lxml')
for row in soup.findAll('phoenix-ellipsis', attrs={'class': 'm-ellipsis m-card--header'}):
  table = {}  # Dictionary to store all values
  title = row.find('a', attrs='').find('h2', attrs='m-ellipsis--text m-card--header-text').text.strip().replace(',', '')
  author = 'N/A'
  date = 'Today'
  if row.find('a', attrs='')['href'][:4] == 'http':
    link = row.find('a', attrs='')['href']
  else:
    link = 'https://www.thestreet.com/' + row.find('a', attrs='')['href']

  table['source'] = "thestreet.com"
  table['title'] = title.replace(',', '')
  table['author'] = author.replace(',', '')
  table['date'] = date.strip().replace(',', '')
  table['link'] = link
  
  list.append(table)
  

# Kiplinger Crawler
html = requests.get('https://www.kiplinger.com/investing')
soup = BeautifulSoup(html.content, 'lxml')
for row in soup.findAll('a', attrs={'class': 'listing__link'}):
  table = {}  # Dictionary to store all values
  try:
    title = row.find('div', attrs='listing__text-wrapper').find('h2', attrs='listing__title').text.strip()
  except:
    title = row.find('h2', attrs='listing__title').text.strip()
  author = 'N/A'
  date = 'Today'
  link = row['href']

  table['source'] = "kiplinger.com"
  table['title'] = title.replace(',', '')
  table['author'] = author.replace(',', '')
  table['date'] = date.strip().replace(',', '')
  table['link'] = link
  
  list.append(table)


# investorplace.com Crawler
html = requests.get('https://investorplace.com/category/stock-picks/stocks-to-buy/')
soup = BeautifulSoup(html.content, 'lxml')

investorplace_authors = []
try:
  for row in soup.findAll('span', attrs={'class': 'entry-meta-author ipm-category-meta-author'}):
    author = row.find('a', attrs='').text.strip().split(',')[0]
    investorplace_authors += [author]
except:
  author = 'N/A'

for count, row in enumerate(soup.findAll('h2', attrs={'class': 'entry-title ipm-category-title'})):
  table = {}  # Dictionary to store all values
  author_count = 0
  try:
    title = row.find('a', attrs='').text.strip()
  except:
    pass
  date = 'Today'
  link = row.find('a', attrs='')['href']

  table['source'] = "investorplace.com"
  table['title'] = title.replace(',', '')
  table['author'] = investorplace_authors[count].replace(',', '')
  table['date'] = date.strip().replace(',', '')
  table['link'] = link
  
  list.append(table)


# seekingalpha.com Crawler
html = requests.get('https://seekingalpha.com/stock-ideas/quick-picks')
soup = BeautifulSoup(html.content, 'lxml')
for row in soup.findAll('a', attrs={'data-test-id': 'post-list-item-title'}):
  table = {}  # Dictionary to store all values
  try:
    title = row.text.strip()
  except:
    pass
  author = 'N/A'
  date = 'Today'
  link = 'https://seekingalpha.com/' + row['href']

  table['source'] = "seekingalpha.com"
  table['title'] = title.replace(',', '')
  table['author'] = author
  table['date'] = date
  table['link'] = link
  
  list.append(table)


# Curation Algorithm
# Trade Scret..


#Remove Duplicate items
list3 = []
all_titles = []
for x in list2:
  if x['title'] not in all_titles:
    list3.append(x)
    all_titles += [x['title']]
      

# Random Shuffle
random.shuffle(list3)
    

# Create a csv file
filename = "db.csv"
with open(filename, 'w', newline='') as f:
  w = csv.DictWriter(f, ['source', 'title', 'author', 'date', 'link'])
  w.writeheader()
  for item in list3:
    w.writerow(item)
