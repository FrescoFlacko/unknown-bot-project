from imports import *
from time import sleep
from sys import exit
import threading

def active_trade_watcher(mutex, coinsList):
    btc_trade = Watcher('btc', 33600, 33400, 33650, 0.55, True)
    eth_trade = Watcher('eth', 2149.73, 2100, 2160, 0.6, True)
    xrp_trade = Watcher('xrp', 0.653339, 0.653, 0.654, 0.6, True)

    trades = [btc_trade, eth_trade, xrp_trade]

    coinsList = retrieveCryptoList()
    while True:
        prices = retrievePrices(idList)

        for trade in trades:
            coin_id = coinsList[trade.symbol]
            price = prices[coin_id]['usd']

            if (trade.didPricePassStopLoss(price) == True):
                print("Stop loss hit")
                trades[:] = [x for x in trades if x != trade]
                # Convert Watcher to Result trade and upload it to the server
            elif (trade.didPricePassTakeProfit(price) == True):
                print("Take profit hit")
                trades[:] = [x for x in trades if x != trade]
        
        sleep(5)

def discord_listener(mutex, coinsList):
    mutex.acquire()
    idList = ','.join(buildIdList(['xrp', 'btc', 'eth'], coinsList))
    mutex.release()

if __name__ == "__main__":
    # TODO: Find place to place API key. Preferrably to be entered in command line but for now keep in code
    # api_key = "pk_fc3ff7ca62524c4e9a45b434780efec1"
    # initializeEnvironment(api_key)

    # stock_tickers = ["AAPL", "BB", "FB", "MSFT"]
    # stock_prices = getPricesForTickers(stock_tickers)
    # print(stock_prices)
    response = initializeMongoDBService()
    if (response == False):
        exit()
    
    mutex = threading.Lock()
    coinsList = retrieveCryptoList()

    # Trade watcher thread: Read 
    # Discord watcher thread: Write
    global idList

    # Trade watcher thread: Read & Write
    # Discord watcher thread: Write
    global trades

    # watcher_thread = threading.Thread(target=active_trade_watcher, args=(mutex, coinsList), daemon=True)
    discord_thread = threading.Thread(target=discord_listener, args=(mutex, coinsList), daemon=True)

    # watcher_thread.start()
    discord_thread.start()

    # watcher_thread.join()
    discord_thread.join()