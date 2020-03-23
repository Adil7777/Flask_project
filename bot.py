from telegram import Bot, Update
from telegram.ext import Updater, MessageHandler, Filters
import config
import messages
from parcer import Currency


class TelegrammBot:
    def __init__(self):
        self.if_hello = False

    def send_course(self, dollar_buy, dollar_sell, euro_buy, euro_sell, rub_buy, rub_sell):
        pass

    def message_handler(self, bot: Bot, update: Update):
        user = update.effective_user

        if user:
            name = user.first_name
        else:
            name = 'Аноним'

        text = update.effective_message.text

        for i in messages.HELLO_MESSAGES:
            if i in text.lower():
                self.if_hello = True
                break

        if self.if_hello:
            self.send_text = 'HEllO, {}!!!'.format(name)

        elif 'курс' in text:
            a = Currency()
            self.send_text = a.check_currency()

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
