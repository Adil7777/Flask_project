from telegram import Bot, Update
from telegram.ext import Updater, MessageHandler, Filters
import config


def message_handler(bot: Bot, update: Update):
    user = update.effective_user
    if user:
        name = user.first_name
    else:
        name = 'Аноним'
    text = update.effective_message.text
    if 'курс' in text:
        reply_text = 'course is now'
    else:
        reply_text = ''
    bot.send_message(chat_id=update.effective_message.chat_id, text=reply_text)


def main():
    bot = Bot(token=config.TOKEN)
    updater = Updater(bot=bot)
    handler = MessageHandler(Filters.all, message_handler)
    updater.dispatcher.add_handler(handler)

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
