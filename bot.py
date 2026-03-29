import requests
import time

def get_gold_price():
    try:
        # PAX Gold (PAXG) price check kar raha hai jo Gold ko follow karta hai
        url = "https://api.binance.com/api/v3/ticker/price?symbol=PAXGUSDT"
        response = requests.get(url)
        data = response.json()
        return data['price']
    except Exception as e:
        return f"Error: {e}"

print("--- Gold Trading Bot Online ---")

while True:
    price = get_gold_price()
    print(f"Current Gold Price: ${price}")
    
    # Is point par bot sirf price monitor kar raha hai
    # Agle step mein hum ismein 'Buy/Sell' ka logic dalenge
    
    time.sleep(10) # Har 10 second baad check karega
