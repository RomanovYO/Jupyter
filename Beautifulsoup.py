import requests
from bs4 import BeautifulSoup

url = 'http://www.cbr.ru/scripts/XML_daily.asp'
responce = requests.get(url)

soup = BeautifulSoup(responce.content, 'lxml')
print(soup)

lst = soup.find_all('name')

for item in lst:
  print(item)

url = 'https://matplotlib.org/stable/gallery/index.html'
responce = requests.get(url)

soup = BeautifulSoup(responce.content, 'html.parser')
# print(soup)

lst = soup.find_all('h2')

for item in lst:
  print(item)

def clean_item(my_item):
  return my_item[my_item.find('>')+1:my_item.find('<', 2)]

print(clean_item('<h2>Text, labels and annotations<a class="headerlink" href="#text-labels-and-annotations" title="Permalink to this headline">'))

print('')

for item in lst:
  print(clean_item(str(item)))

lst = soup.find_all(class_ = 'std std-ref')

for item in lst:
  print(item)

print('')

for item in lst:
  print(clean_item(str(item)))
