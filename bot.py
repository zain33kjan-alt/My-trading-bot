import requests
import time

def get_data():
    try:
        # Gold (PAXG) ka pichla data lene ke liye
        url = "https://api.binance.com/api/v3/klines?symbol=PAXGUSDT&interval=15m&limit=20"
        response = requests.get(url).json()
        prices = [float(candle[4]) for candle in response]
        return prices
    except:
        return []

def simple_signal(prices):
    if not prices: return "Wait..."
    current_price = prices[-1]
    avg_price = sum(prices) / len(prices)
    
    # Strategy: Average se comparison
    if current_price < (avg_price * 0.9995): 
        return "🟢 BUY SIGNAL"
    elif current_price > (avg_price * 1.0005):
        return "🔴 SELL SIGNAL"
    else:
        return "⚪ WAIT"

print("--- Gold Signal Bot v2.0 Online ---")

while True:
    prices = get_data()
    if prices:
        signal = simple_signal(prices)
        print(f"Price: ${prices[-1]} | Advice: {signal}")
    time.sleep(15)
  
