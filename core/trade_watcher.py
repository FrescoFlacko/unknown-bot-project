from util import mongo
from models.Watcher import Watcher
from copy import deepcopy 

WATCHER_COLLECTION_NAME = 'watchers'

def getAllWatchers():
    watchers = mongo.retrieveAllFromCollection(WATCHER_COLLECTION_NAME)
    return watchers

def updateWatcher(watcher):
    response = mongo.updateDocument(WATCHER_COLLECTION_NAME, watcher)
    return response

def createWatcher(ticker, price, stopLoss, takeProfit, confidence, isLong):
    watcher = Watcher(ticker, price, stopLoss, takeProfit, confidence, isLong)
    
    response = mongo.insertDocument(WATCHER_COLLECTION_NAME, watcher)
    # Error handle
    # if response did not succed
    #   print reason why
    #   return None 

    return watcher

def closePriceForDay(price, watcher):
    newWatcher = clonedeep(watcher)
    newWatcher.dailyCloses.append(price)

    response = mongo.updateDocument(WATCHER_COLLECTION_NAME, newWatcher)
    # If response fails, print reason why and return None

    return newWatcher