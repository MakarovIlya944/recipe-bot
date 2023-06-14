
from src.shef import Shef
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("""Ты можешь управлять мной используя следующие команды:

/help – основные команды бота

/certainrecipe *название рецепта* – конкретный рецепт

/ingredients *название* – укажите ингредиенты из которых хотите приготовить блюдо

Идеи для готовки:
/breakfast – завтрак
/lunch – обед
/saladper – ужин
/snacks – закуски 
/salad – салаты
/soup – супы
/hotmeal – горячее 
/dessert – десерт
/baking – выпечка
/drinks – напитки 
/nationalkitchen *название кухни* – национальная кухня
/vegetarian – вегетарианская кухня

Итак, что готовим? """)
    
def generate_html(reciep) -> str:
    ings = []
    for i in reciep['ingredients']:
        m = i[2]
        if abs(int(i[2]) - i[2]) < 1e-3:
            m = int(i[2])
        ings.append(f'{i[0]}:\t\t{m} {i[1]}')
    ings = '\n'.join(ings)
    steps = reciep['steps'].split('\n')
    steps = [f'<b>{i+1}.</b> {v}' for i,v in enumerate(steps)]
    steps = '\n'.join(steps)
    
    return f"""
<b>{reciep['name']}</b>


<b>Описание:</b>
{reciep['desc']}


<b>Игредиенты:</b>
{ings}


<b>Приготовление:</b>
{steps}
                                    """

async def breakfast(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print("завтрак")
    await update.message.reply_html(generate_html(Shef.get("завтрак")))

async def lunch(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print("обед")
    await update.message.reply_html(generate_html(Shef.get("обед")))

async def supper(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print("ужин")
    await update.message.reply_html(generate_html(Shef.get("ужин")))

async def salad(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print("салат")
    await update.message.reply_html(generate_html(Shef.get("салат")))

async def snacks(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print("закуска")
    await update.message.reply_html(generate_html(Shef.get("закуска")))

async def soup(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print("суп")
    await update.message.reply_html(generate_html(Shef.get("суп")))

async def hotmeal(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print("горячее")
    await update.message.reply_html(generate_html(Shef.get("горячее")))

async def dessert(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print("десерт")
    await update.message.reply_html(generate_html(Shef.get("десерт")))

async def baking(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print("выпечка")
    await update.message.reply_html(generate_html(Shef.get("выпечка")))

async def drinks(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print("напитки")
    await update.message.reply_html(generate_html(Shef.get("напитки")))
    
# async def vegetarian(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     print("завтрак")
#     await update.message.reply_html(generate_html("завтрак"))

async def next(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print("next")
    Shef.next()
    await update.message.reply_html(generate_html(Shef.next()))

def main():
    print("привет")
    application = Application.builder().token("").build()
    application.add_handler(CommandHandler(["start", "help"], start))
    application.add_handler(CommandHandler("next",next))
    application.add_handler(CommandHandler("breakfast",breakfast))
    application.add_handler(CommandHandler("lunch",lunch))
    application.add_handler(CommandHandler("salad",salad))
    application.add_handler(CommandHandler("snacks",snacks))
    application.add_handler(CommandHandler("hotmeal",hotmeal))
    application.add_handler(CommandHandler("salad",salad))
    application.add_handler(CommandHandler("soup",soup))
    application.add_handler(CommandHandler("dessert",dessert))
    application.add_handler(CommandHandler("baking",baking))
    application.add_handler(CommandHandler("drinks",drinks))
    
    # Run the bot until the user presses Ctrl-C
    application.run_polling()

"""разбить хэндлеры на отдельные, описать старт  хелп некст"""
if __name__ =="__main__":
    Shef.connect()
    # Shef.scrap(num_pages=10,num_recipes=200)
    main()