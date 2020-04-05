from messages import *
from telegram import Bot, Update
from telegram.ext import Updater, MessageHandler, Filters
import config
from parcer import Currency
from time_ import time
from Currency_converter import currency_converter


class TelegrammBot:
    def __init__(self):
        self.if_hello = False
        self.time_ = time()
        self.dollar = False
        self.euro = False
        self.rub = False
        self.send_text = ''
        self.not_else = True

    def main(self):
        bot = Bot(token=config.TOKEN)
        updater = Updater(bot=bot)
        handler = MessageHandler(Filters.all, self.message_handler)
        updater.dispatcher.add_handler(handler)

        updater.start_polling()
        updater.idle()

    def send_course(self, dollar_buy, dollar_sell, euro_buy, euro_sell, rub_buy, rub_sell):
        self.send_text += 'Курс {}'.format(self.time_)
        self.send_text += "\n----------------"
        if self.dollar is True:
            self.dollar = False
            self.not_else = False
            self.send_text += '\nПокупка доллара: {}'.format(dollar_sell)
            self.send_text += '\nПродажа доллара: {}'.format(dollar_buy)
            self.send_text += '\n----------------'
        if self.euro is True:
            self.euro = False
            self.not_else = False
            self.send_text += '\nПокупка евро: {}'.format(euro_sell)
            self.send_text += '\nПродажа евро: {}'.format(euro_buy)
            self.send_text += '\n----------------'
        if self.rub is True:
            self.rub = False
            self.not_else = False
            self.send_text += '\nПокупка рубля: {}'.format(rub_sell)
            self.send_text += '\nПродажа рубля: {}'.format(rub_buy)
            self.send_text += '\n----------------'
        elif not self.dollar and not self.euro and not self.rub and self.not_else:
            self.send_text += '\nПокупка доллара: {}'.format(dollar_sell)
            self.send_text += '\nПродажа доллара: {}'.format(dollar_buy)
            self.send_text += '\n----------------'
            self.send_text += '\nПокупка евро: {}'.format(euro_sell)
            self.send_text += '\nПродажа евро: {}'.format(euro_buy)
            self.send_text += '\n----------------'
            self.send_text += '\nПокупка рубля: {}'.format(rub_sell)
            self.send_text += '\nПродажа рубля: {}'.format(rub_buy)
            self.send_text += '\n----------------'

    def valuta_sort(self, new, old):
        self.dol_buy_new, self.dol_sell_new = new[0], new[1]
        self.eur_buy_new, self.eur_sell_new = new[2], new[3]
        self.rub_buy_new, self.rub_sell_new = new[4], new[5]
        self.dol_buy_old, self.dol_sell_old = old[0], old[1]
        self.eur_buy_old, self.eur_sell_old = old[2], old[3]
        self.rub_buy_old, self.rub_sell_old = old[4], old[5]

    def message_handler(self, bot: Bot, update: Update):
        user = update.effective_user

        if user:
            name = user.first_name
        else:
            name = 'Аноним'

        text = update.effective_message.text
        # print(text)

        for i in HELLO_MESSAGES:
            if i in text.lower():
                self.if_hello = True
                break

        if self.if_hello:
            self.if_hello = False
            self.send_text = 'HEllO, {}!!!'.format(name)

        elif 'convert' in text.lower():
            a = text.split()
            self.send_text = currency_converter(a[1], a[2], a[3])

        elif 'курс' in text.lower():
            a = Currency()
            self.new, self.old = a.check_currency()[0], a.check_currency()[1]
            self.valuta_sort(self.new, self.old)
            if self.dol_buy_new > self.dol_buy_old:
                pass
            elif self.dol_buy_new < self.dol_buy_old:
                pass
            else:
                for i in DOLLAR:
                    if i in text.lower():
                        self.dollar = True
                        break

                for i in EURO:
                    if i in text.lower():
                        self.euro = True
                        break

                for i in RUB:
                    if i in text.lower():
                        self.rub = True

                self.send_course(self.dol_buy_new, self.dol_sell_new, self.eur_buy_new, self.eur_sell_new,
                                 self.rub_buy_new, self.rub_sell_new)
        else:
            self.send_text = 'В ответах я отраничен'

        bot.send_message(chat_id=update.effective_message.chat_id, text=self.send_text)
        self.send_text = ''


a = TelegrammBot()
a.main()
