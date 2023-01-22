import requests
from bs4   import BeautifulSoup
url = 'https://www.chevrolet.com/build-your-own-chevrolet#f=attr-price-min-10000-999999999&attr-passenger_capacity-max-2-999999999'
html = requests.get(url)
s = BeautifulSoup(html.content, 'html.parser')
results = s.find(id= '<div class="q-mod q-mod-vehicle-tile q-vehicle-tile none-margin">')
jt = results.find_all('div', class_='q-vehicle-tile__title')
for i in jt:
    print(i.text)