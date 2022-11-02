import requests
 
r = requests.get("http://api.coinlayer.com/api/live?access_key=dd61c88c20c658209ab9639b8a5e29a9")
 
responses = r.json()
responses

def show():
    print("Bitcoin: ",responses['rates']['BTC'])
    # Ethereum (ETH to USD):
    print("Ethereum: ",responses['rates']['ETH'])
    # Cardano (ADA to USD):
    print("Cardano: ",responses['rates']['ADA'])
    # Binance Coin (BNB to USD):
    print("Binance: ",responses['rates']['BNB'])
    # Tether (USDT to USD):
    print("Tether: ",responses['rates']['USDT'])
    # Ripple (XRP to USD):
    print("Ripple: ",responses['rates']['XRP'])
    # Dogecoin (DOGE to USD):
    print("Dogecoin: ",responses['rates']['DOGE'])
    # Bitcoin Cash (BCH to USD):
    print("Bitcoin Cash : ",responses['rates']['BCH'])
    # Litecoin (LTC to USD):
    print("Litecoin: ",responses['rates']['LTC'])
    # Chainlink (LINK to USD)
    print("Chainlink: ",responses['rates']['LINK'])

def welcome():
    print("")
    print("Welcome to Real Time Crypto Tracker")
    print("")
    print("All Of the prices are in USD and Soon will be available in INR")
    print("")
    print("Enter 1 to Refresh/Display the Price")
    print("Enter 2 to Quit")
    print("")
    a = int(input())

    if a == 1:
        show()
        print("")
        welcome()
    
    else:
        print("Thanks For Your Time")
        quit()



welcome()