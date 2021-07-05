from iexfinance.stocks import Stock
import os

def initializeEnvironment(api_key):
    # TODO: Find a safe way to store API key
    os.environ["IEX_TOKEN"] = api_key

def getPricesForTickers(tickers):
    batch = Stock(tickers)
    return batch.get_price()