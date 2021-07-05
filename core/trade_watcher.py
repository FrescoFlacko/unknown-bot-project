from util import mongo
from copy import deepcopy 

def getAllWatchers():
    watchers = mongo.retrieveAllFromCollection('watchers')
    return watchers

def updateWatcher(watcher):
    response = mongo.updateDocument('watchers', watcher)
    return response

def createWatcher(ticker, price, stopLoss, takeProfit, confidence, isLong):
    watcher = Watcher(ticker, price, stopLoss, takeProfit, confidence, isLong)
    
    response = mongo.insertDocument('watcher', watcher)
    # Error handle
    # if response did not succed
    #   print reason why
    #   return None 

    return watcher

def closePriceForDay(price, watcher):
    newWatcher = clonedeep(watcher)
    newWatcher.dailyCloses.append(price)

    response = mongo.updateDocument('watcher', newWatcher)
    # If response fails, print reason why and return None

    return newWatcher