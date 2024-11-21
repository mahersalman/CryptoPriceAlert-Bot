from telegram import Update
from user_alerts import user_alerts

class Command():
    def __init__(self):
        self.commands_list = {
            "start"    : ["Start bot", self.start],
            "help"     : ["Get help", self.help],
            "setalert" : ["set alerts",self.set_alert],
        }

    async def start(self,update: Update, context):
        print(f"start command called by {update.effective_user.username} : {update.effective_user.id}")
        await update.message.reply_text("Welcome To Our Bot")

    async def help(self, update: Update, context):
        print(f"help command called by {update.effective_user.username} : {update.effective_user.id}")
        text = "you can intract with this bot using the following command : \n"
        text = text + "".join(f"/{command} - {description}\n" for command,(description,_) in self.commands_list.items())
        await update.message.reply_text(text)

    async def set_alert(self, update: Update , context):
        print(f"set_alert command called by {update.effective_user.username} : {update.effective_user.id}")
        chat_id = update.effective_chat.id
        try:
            coin_id = context.args[0].lower()
            target_price = float(context.args[1])
            direction = context.args[2]
            if coin_id not in user_alerts:
                user_alerts[coin_id] = []
            user_alerts[coin_id].append({'ids':coin_id,'price':target_price , 'direction' : direction})
            if direction == 'up':
                await update.message.reply_text(f'Alert set for {coin_id} if it exceeds {target_price}')
            else:
                await update.message.reply_text(f'Alert set for {coin_id} if it drops below {target_price}')

        except(IndexError,ValueError):
            await update.message.reply_text('Usage: /setalert <crypto_id> <price> <direction>')
