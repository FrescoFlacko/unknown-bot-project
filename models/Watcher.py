from datetime import datetime

class Watcher:
    def __init__(self, ticker, entryPrice, stopLoss, takeProfit, confidence):
        self.creationDate = datetime.now()
        self.dailyCloses = []
        self.ticker = ticker
        self.stopLoss = stopLoss
        self.takeProfit = takeProfit
        self.entryPrice = entryPrice
        self.confidence = confidence