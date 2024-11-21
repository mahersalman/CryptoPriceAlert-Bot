import requests
import asyncio
from time import sleep

"""
type of alerts : dictionary
    * key : coin_id(according to coingecko)
    * value : list = [dict1,dict2,dict3]
    (while each dict is = {'chat_id':chat_id,'price':price,'direction':direction})
"""
user_alerts ={}
user_alerts['bitcoin'] = [{'chat_id':1234,'price':50000,'direction':'up'}]
 
API_URL = "https://api.coingecko.com/api/v3/simple/price"
def get_crypto_price(coin_id,currency ='usd'):
    try:
        params = {'ids': coin_id,
                    'vs_currencies': currency
                    }
        response = requests.get(API_URL,params=params)
        data = response.json()
        return data[coin_id][currency]
    except Exception as e:
        print("Error in get_crypto_price:",e)
        return 0


async def check_prices(application):
    try:
        for coin_id,users in user_alerts.items():
            current_price = get_crypto_price(coin_id)
            for user in users:
                if user['direction'] == 'up' and current_price >= user['price']:
                    await application.bot.send_message(chat_id=user['chat_id'], text=f"🚀 {coin_id} has exceeds ${current_price}!")
                elif user['direction'] == 'down' and current_price <= user['price']:
                    await application.bot.send_message(chat_id=user['chat_id'], text=f"⚠️ {coin_id} has drops below ${current_price}!")
    except Exception as e:
        print("Error in check_prices:",e)


async def alerts(application):
    while True:
        await check_prices(application)
        sleep(20)


def thread_run_alert(application):
    asyncio.run(alerts(application)) 
