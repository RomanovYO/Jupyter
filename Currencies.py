import requests
import xmltodict

url = 'http://www.cbr.ru/scripts/XML_daily.asp'
responce = requests.get(url)
# ~ print(responce.content)
data = xmltodict.parse(responce.content)
# ~ print(data)

items = []
for item in data['ValCurs']['Valute']:
  items.append(item)
# ~ print(items)

my_array = []
for item in data['ValCurs']['Valute']:
  my_set = [item['CharCode'], item['NumCode'], item['Nominal'].rjust(5), item['Value'], item['Name']]
  my_array.append(my_set)
  print(sorted(my_set))
# ~ print(my_array)
