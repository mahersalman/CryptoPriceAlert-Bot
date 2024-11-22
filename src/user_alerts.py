import requests
import asyncio
from api_calls import get_crypto_price
"""
type of alerts : dictionary
    * key : coin_id(according to coingecko)
    * value : list = [dict1,dict2,dict3]
    (while each dict is = {'chat_id':chat_id,'price':price,'direction':direction})
"""
user_alerts ={}
 
# crypto_id_link - "https://docs.google.com/spreadsheets/d/1wTTuxXt8n9q7C4NDXqQpI3wpKu1_5bGVmP9Xz0XGSyU/edit?gid=0#gid=0"

async def check_prices(application,currency = 'usd'):
    try:
        coins_price = get_crypto_price(list(user_alerts.keys()))
        for coin_id,users in user_alerts.items():
            for user in users:
                current_price = coins_price[coin_id][currency]
                if user['direction'] == 'up' and current_price >= user['price']:
                    await application.bot.send_message(chat_id=user['chat_id'], text=f"🚀 {coin_id} has exceeds ${current_price}!")
                elif user['direction'] == 'down' and current_price <= user['price']:
                    await application.bot.send_message(chat_id=user['chat_id'], text=f"⚠️ {coin_id} has drops below ${current_price}!")
    except Exception as e:
        print("Error in check_prices:",e)


async def alerts(application):
    while True:
        await check_prices(application)
        await asyncio.sleep(60)


def thread_run_alert(application):
    asyncio.run(alerts(application)) 


