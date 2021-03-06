import logging

from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters

import config


def start(bot, update):
    update.effective_message.reply_text("Hi {}!".format(update.effective_user.username))
    logger.debug('/start')


def echo(bot, update):
    update.effective_message.reply_text(update.effective_message.text)
    logger.debug('/echo')


def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG, filename='bot.log')
    logger = logging.getLogger(__name__)

    updater = Updater(config.token)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.text, echo))
    dispatcher.add_error_handler(error)

     updater.start_webhook(listen="0.0.0.0", port=int(config.port), url_path=config.token)
     updater.bot.setWebhook("https://{}.herokuapp.com/{}".format(config.name, config.token))
    # updater.start_polling()

    updater.idle()
