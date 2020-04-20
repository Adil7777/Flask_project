import requests
from bs4 import BeautifulSoup


class Currency:
    DOLLAR_TO_KZ = 'https://mig.kz/'
    NAZBANK = 'https://nationalbank.kz/?furl=cursFull&switch=rus'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    }

    def __init__(self):
        self.current_buy_price = float(self.get_currency_price()[0])
        # self.current_buy_price = 460
        self.old_currents = self.first_time()
        self.difference = 4
        self.up = False
        self.down = False

    def nazbank(self):
        nazbank = []
        a = True
        next = False
        page = requests.get(self.NAZBANK, self.headers)
        soup_2 = BeautifulSoup(page.content, 'html.parser')
        course = soup_2.findAll('td', {'class': 'gen7'})
        for i in course:
            if 'GBP' in i.text:
                next = True
            elif 'RUB' in i.text:
                next = True
            elif 'KGS' in i.text:
                next = True
            elif 'EUR' in i.text:
                next = True
            elif 'USD' in i.text:
                next = True
            elif next:
                index = course.index(i)
                text = course[index - 1].text
                nazbank.append('{} {}'.format(text, i.text))
                next = False
            # print(i.text)
            # print('---------')
        return nazbank

    def first_time(self):
        full_page = requests.get(self.DOLLAR_TO_KZ, self.headers)

        soup = BeautifulSoup(full_page.content, 'html.parser')

        buy = soup.findAll('td', {'class': 'buy delta-neutral'})
        sell = soup.findAll('td', {'class': 'sell delta-neutral'})
        dol_buy = buy[0].text
        dol_sell = sell[0].text
        eur_buy = buy[1].text
        eur_sell = sell[1].text
        rub_buy = buy[2].text
        rub_sell = sell[2].text
        kgs_buy = buy[3].text
        kgs_sell = sell[3].text
        fnt_buy = buy[4].text
        fnt_sell = sell[4].text
        old_currents = [dol_buy, dol_sell, eur_buy,
                        eur_sell, rub_buy, rub_sell, kgs_buy, kgs_sell, fnt_buy, fnt_sell]
        return old_currents

    def sort_valuta(self, buy, sell):
        self.dol_buy = buy[0].text
        self.dol_sell = sell[0].text
        self.eur_buy = buy[1].text
        self.eur_sell = sell[1].text
        self.rub_buy = buy[2].text
        self.rub_sell = sell[2].text
        self.kgs_buy = buy[3].text
        self.kgs_sell = sell[3].text
        self.fnt_buy = buy[4].text
        self.fnt_sell = sell[4].text
        self.new_currents = [self.dol_buy, self.dol_sell, self.eur_buy,
                             self.eur_sell, self.rub_buy, self.rub_sell,
                             self.kgs_buy, self.kgs_sell, self.fnt_buy, self.fnt_sell]

    def get_currency_price(self):
        full_page = requests.get(self.DOLLAR_TO_KZ, self.headers)

        soup = BeautifulSoup(full_page.content, 'html.parser')

        buy = soup.findAll('td', {'class': 'buy delta-neutral'})
        sell = soup.findAll('td', {'class': 'sell delta-neutral'})
        self.sort_valuta(buy, sell)
        return buy[0].text, sell[0].text

    def check_currency(self):
        currency_buy = float(self.get_currency_price()[0])
        currency_sell = float(self.get_currency_price()[1])
        if currency_buy > self.current_buy_price:
            self.up = True
        elif currency_buy < self.current_buy_price:
            self.down = True
        else:
            self.up = False
            self.down = False
        return self.new_currents, self.old_currents


a = Currency()
a.check_currency()
a.nazbank()
