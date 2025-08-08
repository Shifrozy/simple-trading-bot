import requests
import pandas as pd
import time

def get_price():
    url = "https://api.binance.com/api/v3/klines"
    params = {"symbol": "BTCUSDT", "interval": "1m", "limit": 20}
    data = requests.get(url, params=params).json()
    closes = [float(c[4]) for c in data]  # Closing prices
    return closes

def strategy(prices):
    df = pd.DataFrame(prices, columns=["close"])
    df["SMA"] = df["close"].rolling(5).mean()
    if df["close"].iloc[-1] > df["SMA"].iloc[-1]:
        return "BUY"
    elif df["close"].iloc[-1] < df["SMA"].iloc[-1]:
        return "SELL"
    return "HOLD"

while True:
    prices = get_price()
    signal = strategy(prices)
    print(f"Latest Price: {prices[-1]} | Signal: {signal}")
    time.sleep(60)
