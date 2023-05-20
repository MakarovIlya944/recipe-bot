import argparse
import json
import time
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

data = []
ingredients = 'Ингредиенты:\n'
steps = 'Приготовление:\n'
lastCommand = ''

#{'title':title, 'ingredients':ingredients, 'tags':tags, 'steps':steps}   
def FormatRecipe(recipe):
    s = recipe['title'] + '\n' + ingredients
    s += '\n'.join([f'{i[0]} {i[1]}' for i in recipe['ingredients']]) + '\n'
    s += steps
    s += '\n'.join([f'{i+1}. {el}' for i,el in enumerate(recipe['steps'])])
    return s

def start(update: Update, context: CallbackContext) -> None:
    with open('text/start.txt', 'r') as f:
        lines = f.readlines()
    update.message.reply_text('\n'.join(lines))

def help_cb(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Help!')

def breakfast(update: Update, context: CallbackContext) -> None:
    breakfasts = [d for d in data if 'завтрак' in d['tags']] # выбираем из всех записей те которые имеют тэг завтрак
    b = breakfasts[int(round(time.time() * 1000)) % len(breakfasts)] # берем случайную запись на основе текущего времени
    update.message.reply_text(FormatRecipe(b)) # отправляем этот рецепт

def LoadData(filename, n=None):
    global data
    if n:
        for i in range(n):
            with open(filename + f'_{n}.json', 'r') as f:
                data.extend(json.load(f))
    else:
        with open(filename, 'r') as f:
            data = json.load(f)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('bot_token', help='Bot token')
    args = parser.parse_args()
    
    LoadData('data/data', 1)

    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(args['bot_token'])

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("breakfast", breakfast))
    dispatcher.add_handler(CommandHandler("help", help_cb))

    # on non command i.e message - echo the message on Telegram
    # dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()
