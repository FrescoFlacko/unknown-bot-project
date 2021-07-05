# TODO: Have to retrieve list of IDs to be used for API calls rather than symbols
# This can be stored in a database but since this application will be running constantly,
# an initial call in the beginning will suffice
import requests

def retrieveCryptoList():
    response = requests.get('https://api.coingecko.com/api/v3/coins/list')

    if response.status_code != 200:
        print('Error retrieving list of coins from CoinGecko, ', response.json())
        return
    
    coinList = {}

    for coin in response.json():
        coinList[coin['symbol']] = coin['id']
    
    return coinList

def retrievePrices(coins):
    response = requests.get(
        'https://api.coingecko.com/api/v3/simple/price',
        params={ 'ids': coins, 'vs_currencies': 'usd' }
    )

    if response.status_code != 200:
        print('Error retrieving list of prices for coins from CoinGecko, ', response.json())
        return
    
    return response.json()

def buildIdList(symbols, coinList):
    '''
        Convert list of symbols into CoinGecko ID's to be used for API calls.
        Returns list of ID's.
    '''
    idList = [coinList[symbol] for symbol in symbols]
    return idList