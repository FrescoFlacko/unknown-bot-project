from imports import *
from time import sleep
import threading

def active_trade_watcher():
    btc_trade = Watcher('btc', 33340, 33000, 35000, 0.55)
    
    coinsList = retrieveCryptoList()
    idList = ','.join(buildIdList(['xrp', 'btc', 'ltc'], coinsList))
    counter = 0
    while counter < 10:
        prices = retrievePrices(idList)
        print(prices)

        counter += 1
        sleep(30)

if __name__ == "__main__":
    # TODO: Find place to place API key. Preferrably to be entered in command line but for now keep in code
    # api_key = "pk_fc3ff7ca62524c4e9a45b434780efec1"
    # initializeEnvironment(api_key)

    # stock_tickers = ["AAPL", "BB", "FB", "MSFT"]
    # stock_prices = getPricesForTickers(stock_tickers)
    # print(stock_prices)
    watcher_thread = threading.Thread(target=active_trade_watcher, args=(), daemon=True)
    watcher_thread.start()
    watcher_thread.join()