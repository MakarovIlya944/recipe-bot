

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print("start running")

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

def main():
    print("привет")
    application = Application.builder().token("").build()
    application.add_handler(CommandHandler(["start", "help"], start))
    application.add_handler(CommandHandler("next"))
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