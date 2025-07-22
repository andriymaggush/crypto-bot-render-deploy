import os
import time
import requests
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()

# Ключі
binance_api_key = os.getenv("R0qfijbzNfcUo0suhuqx2SWNa7AABCklkiLmuyBmCpGD7nAIYLYX8SNLjEHW2tnj")
binance_api_secret = os.getenv("lKMdfEzBUKzYr6oOhUgnSnFXct1cyJ1o0tUcBgVxeYriCyr3JXRt4FQcSyVaWuNm")
telegram_token = os.getenv("7982045049:AAHTvi57gvmATZ5hgMp4xqK1wx0-D0aXf_g")
telegram_chat_id = os.getenv("+420728756415")

# Telegram повідомлення
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{telegram_token}/sendMessage"
    data = {"chat_id": telegram_chat_id, "text": message}
    requests.post(url, data=data)

# Binance
client = Client(api_key=binance_api_key, api_secret=binance_api_secret)

# Отримання ціни
def get_price():
    try:
        ticker = client.get_symbol_ticker(symbol="BTCUSDT")
        return float(ticker["price"])
    except:
        return None

# Основний цикл
prev_price = get_price()
while True:
    time.sleep(10)
    price = get_price()
    if price and prev_price and price != prev_price:
        send_telegram_message(f"Ціна BTC змінилася: {prev_price} → {price}")
        prev_price = price
