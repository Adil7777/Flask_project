import requests
from bs4 import BeautifulSoup


class Currency:
    DOLLAR_TO_KZ = 'https://mig.kz/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

    def __init__(self):
        self.current_buy_price = float(self.get_currency_price()[0])
        self.difference = 4

    def get_currency_price(self):
        full_page = requests.get(self.DOLLAR_TO_KZ, self.headers)

        soup = BeautifulSoup(full_page.content, 'html.parser')

        buy = soup.findAll('td', {'class': 'buy delta-neutral'})
        sell = soup.findAll('td', {'class': 'sell delta-neutral'})
        return buy[0].text, sell[0].text

    def check_currency(self):
        currency = float(self.get_currency_price()[0])
        if currency >= self.current_buy_price + self.difference:
            print("Курс вырос")
        elif currency <= self.current_buy_price - self.difference:
            print("Курс упал")
        return currency


a = Currency()
a.check_currency()
