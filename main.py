import json
import time
from bot.bot import Bot
from bot.filter import Filter
from bot.handler import HelpCommandHandler, UnknownCommandHandler, MessageHandler, FeedbackCommandHandler, \
    CommandHandler, NewChatMembersHandler, LeftChatMembersHandler, PinnedMessageHandler, UnPinnedMessageHandler, \
    EditedMessageHandler, DeletedMessageHandler, StartCommandHandler, BotButtonCommandHandler

TOKEN = "" #your token here
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

def help_cb(bot, event):
    bot.send_text(chat_id=event.data['chat']['chatId'])

def breakfast(bot, event):
    breakfasts = [d for d in data if 'завтрак' in d['tags']] # выбираем из всех записей те которые имеют тэг завтрак
    b = breakfasts[int(round(time.time() * 1000)) % len(breakfasts)] # берем случайную запись на основе текущего времени
    bot.send_text(chat_id=event.data['chat']['chatId'], text=FormatRecipe(b)) # отправляем этот рецепт

def UploadData(filename, n=None):
    global data
    if n:
        for i in range(n):
            with open(filename + f'_{n}.json', 'r') as f:
                data.extend(json.load(f))
    else:
        with open(filename, 'r') as f:
            data = json.load(f)

if __name__ == '__main__':

    UploadData('data/data', 1)

    bot = Bot(token=TOKEN)

    bot.dispatcher.add_handler(CommandHandler(command="next", callback=next))

    bot.dispatcher.add_handler(CommandHandler(command="breakfast", callback=breakfast))
    # bot.dispatcher.add_handler(CommandHandler(command="lunch", callback=lunch))
    # bot.dispatcher.add_handler(CommandHandler(command="supper", callback=supper))

    # bot.dispatcher.add_handler(CommandHandler(command="snacks", callback=snacks))
    # bot.dispatcher.add_handler(CommandHandler(command="salad", callback=salad))
    # bot.dispatcher.add_handler(CommandHandler(command="soup", callback=soup))
    # bot.dispatcher.add_handler(CommandHandler(command="hotmeal", callback=hotmeal))
    # bot.dispatcher.add_handler(CommandHandler(command="dessert", callback=dessert))
    # bot.dispatcher.add_handler(CommandHandler(command="baking", callback=baking))
    # bot.dispatcher.add_handler(CommandHandler(command="drinks", callback=drinks))


    # bot.dispatcher.add_handler(CommandHandler(command="vegetarian", callback=vegetarian))



    # bot.dispatcher.add_handler(MessageHandler(callback=message_cb))
    bot.dispatcher.add_handler(HelpCommandHandler(callback=help_cb))
    bot.start_polling()
    bot.idle()