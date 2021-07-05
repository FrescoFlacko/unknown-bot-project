from util import mongo

def closeTrade(watcher, price):
    '''
        Close the current trade and update the watcher and trades database
        with results.
    '''
    profit = (price - watcher.entryPrice) / abs(watcher.entryPrice)
    result = Trade(watcher.ticker, watcher.entryPrice, price, profit, 
                    watcher.confidence, watcher.creationDate, watcher.isLong)
    
    response = mongo.removeDocument('watcher', watcher)
    # Handle error situations here

    response = mongo.insertDocument('results', result)
    # Handle error situations here

    return response
