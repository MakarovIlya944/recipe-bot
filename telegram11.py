

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
/supper – ужин
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
    

async def zavtrak(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print("get_reciep running")

async def obed(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print("get_reciep running")

async def yjin(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print("get_reciep running")

async def zakyska(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print("get_reciep running")

async def sup(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print("get_reciep running")

async def goryachee(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print("get_reciep running")

async def salat(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print("get_reciep running")

async def desert(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print("get_reciep running")

async def vipechka(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print("get_reciep running")

async def napitki(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print("get_reciep running")

async def next(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print("get_reciep running")

def main():
    print("привет")
    application = Application.builder().token("").build()
    application.add_handler(CommandHandler(["start", "help"], start))
    application.add_handler(CommandHandler("next",next))
    application.add_handler(CommandHandler("zavtrak",zavtrak))
    application.add_handler(CommandHandler("obed",obed))
    application.add_handler(CommandHandler("yjin",yjin))
    application.add_handler(CommandHandler("zakyska",zakyska))
    application.add_handler(CommandHandler("salat",salat))
    application.add_handler(CommandHandler("sup",sup))
    application.add_handler(CommandHandler("goryachee",goryachee))
    application.add_handler(CommandHandler("desert",desert))
    application.add_handler(CommandHandler("vipechka",vipechka))
    application.add_handler(CommandHandler("napitki",napitki))



"""разбить хэндлеры на отдельные, описать старт  хелп некст"""
if __name__ =="__main__":
    main()