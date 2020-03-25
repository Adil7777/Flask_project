from telegram import Bot, Update
from telegram.ext import Updater, MessageHandler, Filters
import config
import messages
from parcer import Currency
from time_ import time


class TelegrammBot:
    def __init__(self):
        self.if_hello = False
        self.time_ = time()

    def send_course(self, dollar_buy, dollar_sell, euro_buy, euro_sell, rub_buy, rub_sell):
        pass

    def course_up(self, buy_now, bot: Bot, update: Update):
        print('asdfg')
        send_text = 'Стало: {}'.format(buy_now)
        bot.send_message(chat_id=update.effective_message.chat_id, text=send_text)

    def valuta_sort(self):
        pass

    def message_handler(self, bot: Bot, update: Update):
        user = update.effective_user

        if user:
            name = user.first_name
        else:
            name = 'Аноним'

        text = update.effective_message.text
        print(text)

        for i in messages.HELLO_MESSAGES:
            if i in text.lower():
                self.if_hello = True
                break

        if self.if_hello:
            self.if_hello = False
            self.send_text = 'HEllO, {}!!!'.format(name)

        elif 'курс' in text.lower():
            a = Currency()
            self.new, self.old = a.check_currency()[0], a.check_currency()[1]
            print(self.new, self.old)
            self.valuta_sort()

        else:
            self.send_text = ''

        bot.send_message(chat_id=update.effective_message.chat_id, text=self.send_text)

    def main(self):
        bot = Bot(token=config.TOKEN)
        updater = Updater(bot=bot)
        handler = MessageHandler(Filters.all, self.message_handler)
        updater.dispatcher.add_handler(handler)

        updater.start_polling()
        updater.idle()


a = TelegrammBot()
a.main()
