import requests
from bs4 import BeautifulSoup

DOLLAR_TO_KZ = 'https://mig.kz/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

full_page = requests.get(DOLLAR_TO_KZ, headers)

soup = BeautifulSoup(full_page.content, 'html.parser')

buy = soup.findAll('td', {'class': 'buy delta-neutral'})
sell = soup.findAll('td', {'class': 'sell delta-neutral'})
print(buy[0].text, sell[0].text)
