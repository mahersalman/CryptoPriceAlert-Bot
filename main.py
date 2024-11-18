from dotenv import load_dotenv
import os
import logging
from telegram.ext import ApplicationBuilder, CommandHandler, Application
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from commands import Command

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

load_dotenv()
telegram_bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
telegram_bot_username = os.getenv('TELEGRAM_BOT_USERNAME')

def main():
    commands = Command()
    
    app = ApplicationBuilder().token(telegram_bot_token).build()
    app.add_handlers([CommandHandler(name,func) for name,(_,func) in commands.commands_list.items()])
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
