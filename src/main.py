from dotenv import load_dotenv
import os
import logging
from threading import Thread
from telegram.ext import ApplicationBuilder, CommandHandler, Application
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from commands import Command
from user_alerts import thread_run_alert

# Logging setup for better debugging
#logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


load_dotenv()
telegram_bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
telegram_bot_username = os.getenv('TELEGRAM_BOT_USERNAME')



def main():
    # Create the Bot Application instance with handlers
    commands = Command()
    app = ApplicationBuilder().token(telegram_bot_token).build()
    app.add_handlers([CommandHandler(name,func) for name,(_,func) in commands.commands_list.items()])
    
    # Start the alerts thread
    alerts_thread = Thread(target = thread_run_alert,args = (app,), daemon=True)
    alerts_thread.start()
    logger.info("Alerts thread started")

    try:
        # Start the Bot
        logger.info("Starting the bot")
        app.run_polling(allowed_updates=Update.ALL_TYPES)
    except Exception as e:
        logger.error(f"Error bot polling: {e}")

if __name__ == "__main__":
    main()
