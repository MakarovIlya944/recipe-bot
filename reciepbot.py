from src.shef import Shef
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler

keyboard = [
    [
        InlineKeyboardButton("завтрак", callback_data="завтрак"),
        InlineKeyboardButton("обед", callback_data="обед"),
        InlineKeyboardButton("ужин", callback_data="ужин")
    ],
    [
        InlineKeyboardButton("закуски", callback_data="закуски"),
        InlineKeyboardButton("горячее", callback_data="горячее"),
        InlineKeyboardButton("салаты", callback_data="салаты")
    ],
    [
        InlineKeyboardButton("супы", callback_data="супы"),
        InlineKeyboardButton("десерт", callback_data="десерт"),
        InlineKeyboardButton("выпечка", callback_data="выпечка")
    ],
    [
        InlineKeyboardButton("напитки", callback_data="напитки"),
    ],
]

TOKEN=""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global keyboard
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("""Ты можешь управлять мной используя следующие команды:

/help – основные команды бота

Идеи для готовки можете выбарть по клавишам

Так же если вам не понравился предложенный рецепт можно попросить другой с помощью команды
/next

Итак, что готовим? """, reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query:CallbackQuery = update.callback_query
    await query.answer()
    
    if query.data == "start":
        global keyboard
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_reply_markup(reply_markup=reply_markup)
    else:
        keyboard_reciep = [
            [
                InlineKeyboardButton("другой рецепт", callback_data="start"),
                InlineKeyboardButton("следующий рецепт", callback_data="next"),
            ],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard_reciep)
        if query.data == 'next':
            r = Shef.next()
        else:
            r = Shef.get(query.data)
        await query.message.reply_html(generate_html(r),reply_markup=reply_markup)

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

<b>Игредиенты:</b>
{ings}

<b>Приготовление:</b>
{steps}"""

async def next(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print("next")
    await update.message.reply_html(generate_html(Shef.next()))

def main():
    print("hello")
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler(["start", "help"], start))
    application.add_handler(CommandHandler("next",next))
    application.add_handler(CallbackQueryHandler(button))
    
    # Run the bot until the user presses Ctrl-C
    application.run_polling()

if __name__ =="__main__":
    Shef.connect()
    # Shef.scrap(num_pages=10,num_recipes=200)
    main()