from imports import *

if __name__ == "__main__":
    # TODO: Find place to place API key. Preferrably to be entered in command line but for now keep in code
    api_key = "pk_fc3ff7ca62524c4e9a45b434780efec1"
    initializeEnvironment(api_key)

    stock_tickers = ["AAPL", "BB", "FB", "MSFT"]
    stock_prices = getPricesForTickers(stock_tickers)
    print(stock_prices)