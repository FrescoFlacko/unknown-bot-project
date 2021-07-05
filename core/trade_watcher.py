from util.mongo import *

def getAllWatchers():
    watchers = retrieveAllFromCollection('watchers')
    return watchers

def updateWatcher(watcher):
    response = updateDocument('watchers', watcher)
    return response