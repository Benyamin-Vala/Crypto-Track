from websocket import create_connection
import json
import sys

# Header For Connect to Binance WebSocket
headers = json.dumps({
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'Upgrade',
    'Pragma': 'no-cache',
    'Upgrade': 'websocket',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
})

# Ethereum Websocket
ws = create_connection('wss://stream.binance.com:9443/ws/ethusdt@trade',headers=headers)
# Bitcoin Websocket
ws2 = create_connection('wss://stream.binance.com:9443/ws/btcusdt@trade',headers=headers)

while True:
    try:
        result = ws.recv()
        result2 = ws2.recv()
        
        data = ("Ethereum : "+str(result).split('p":"')[1].split('"')[0]+" USD"+"   |   "+"Bitcoin : "+str(result2).split('p":"')[1].split('"')[0]+" USD")
        print(data, end='\r')
        sys.stdout.flush()
    except Exception as e:
        print(e)
        break