import requests
import time

# --- AAPKI DETAILS ---
TOKEN = "8768449118:AAHhewdXlRfEZP-scSiS5ubasNiYrYCpQKI"
CHAT_ID = "7508343218"

def send_telegram(message):
    try:
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        data = {"chat_id": CHAT_ID, "text": message}
        res = requests.post(url, data=data)
        print(f"Telegram status: {res.status_code}")
    except Exception as e:
        print(f"Error sending message: {e}")

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
    if curr < (avg * 0.9995): return "🟢 BUY SIGNAL"
    if curr > (avg * 1.0005): return "🔴 SELL SIGNAL"
    return None

last_signal = None
print("--- Zain Gold Bot v3.0 Online ---")
# Start pe message jana chahiye
send_telegram("🚀 Zain Gold Bot is now Online and Connected!")

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
    
