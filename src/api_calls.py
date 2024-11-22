import requests
import os
from dotenv import load_dotenv

headers = {
    "accept": "application/json",
    "x-cg-demo-api-key": os.getenv('COINGECKO_API_KEY')
}


def get_crypto_price(coins,currency = 'usd'):
    try :
        coins_id = "%2C".join(coins)
        url_coin_price_byID = f"https://api.coingecko.com/api/v3/simple/price?ids={coins_id}&vs_currencies={currency}&include_market_cap=false&include_24hr_vol=false&include_24hr_change=false&include_last_updated_at=false"
        response = requests.get(url_coin_price_byID, headers=headers)
        return response.json()
    except Exception as e:
        print("Error in get_crypto_price:",e)
