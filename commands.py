from telegram import Update
import requests

API_URL = "https://api.coingecko.com/api/v3/simple/price"
user_alerts ={}

class Command():
    def __init__(self):
        self.commands_list = {
            "start"    : ["Start bot", self.start],
            "help"     : ["Get help", self.help],
            "setalert" : ["Set Alerts",self.set_alert]
        }

    async def start(self,update: Update, context):
        await update.message.reply_text("Welcome To Our Bot")

    async def help(self, update: Update, context):
        text = "you can intract with this bot using the following command : \n"
        text = text + "".join(f"/{command} - {description}\n" for command,(description,_) in self.commands_list.items())
        await update.message.reply_text(text)

    async def set_alert(self, update: Update , context):
        chat_id = update.effective_chat.id
        try:
            crypto_id = context.args[0].lower()
            target_price = float(context.args[1])
            user_alerts[chat_id] = {'ids':crypto_id,'price':target_price}
            await update.message.reply_text(f'Alert set for {crypto_id} at {target_price}')
        except(IndexError,ValueError):
            await update.message.reply_text('Usage: /setalert <crypto_id> <price>')


