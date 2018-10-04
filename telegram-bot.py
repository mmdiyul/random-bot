from telegram.ext import Updater, CommandHandler
from random import randint
import quotes

def start(bot, update):
    update.message.reply_text("Halo, kenalin aku Random Bot. Seneng deh kenalan sama kamu :)\n\nKetik /quote kalo pengen quote dariku :)")

def quote(bot, update):
    i = randint(0, len(quotes.quotes)-1)
    update.message.reply_text(quotes.quotes[i])

def main():
    # Create Updater object and attach dispatcher to it
    updater = Updater('690300824:AAGiU9p5Y11HlXTfJ0ATZELrpHFQSKGB3PI')
    dispatcher = updater.dispatcher
    print("Bot started")

    # Add command handler to dispatcher
    start_handler = CommandHandler('start',start)
    dispatcher.add_handler(start_handler)

    quote_handler = CommandHandler('quote',quote)
    dispatcher.add_handler(quote_handler)

    # Start the bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()