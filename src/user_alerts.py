import requests
import asyncio
from time import sleep


user_alerts ={}

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
        for chat_id,alert in user_alerts.items():
            print(f"Checking {alert['ids']} for {chat_id}")
            current_price = get_crypto_price(alert['ids'])
            if alert['direction'] == 'up' and current_price >= alert['price']:
                await application.bot.send_message(chat_id=chat_id, text=f"🚀 {alert['ids']} has exceeds ${current_price}!")
            elif alert['direction'] == 'down' and current_price <= alert['price']:
                await application.bot.send_message(chat_id=chat_id, text=f"⚠️ {alert['ids']} has drops below ${current_price}!")
    except Exception as e:
        print("Error in check_prices:",e)

async def alerts(application):
    while True:
        await check_prices(application)
        sleep(20)


def thread_run_alert(application):
    asyncio.run(alerts(application)) 


"""
an Optimized version of the user_alerts.py file
 - call api for a list of alerts : then loop and check conditions
"""