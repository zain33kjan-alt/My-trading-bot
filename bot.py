import requests
import time

# Aapki Details
TOKEN = "8768449118:AAHhewdXlRfEZP-scSiS5ubasNiYrYCpQKI"
CHAT_ID = "7508343218"

def send_telegram(message):
    try:
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
        requests.get(url)
    except:
        pass

def get_data():
    try:
        url = "https://api.binance.com/api/v3/klines?symbol=PAXGUSDT&interval=15m&limit=20"
        res = requests.get(url).json()
        return [float(c[4]) for c in res]
    except:
        return []

def get_signal(prices):
    if not prices: return None
    curr, avg = prices[-1], sum(prices)/len(prices)
    # Strategy: 0.05% deviation from average
    if curr < (avg * 0.9995): return "🟢 BUY SIGNAL"
    if curr > (avg * 1.0005): return "🔴 SELL SIGNAL"
    return None

last_signal = None
print("--- Gold Telegram Bot v3.0 Online ---")
send_telegram("🚀 Zain Gold Bot is now Online! I will send signals here.")

while True:
    p = get_data()
    if p:
        signal = get_signal(p)
        if signal and signal != last_signal:
            msg = f"⚠️ {signal}\nGold Price: ${p[-1]}"
            send_telegram(msg)
            last_signal = signal
        print(f"Price: ${p[-1]} | Last Signal: {last_signal if last_signal else 'Waiting...'}")
    time.sleep(20)
