from datetime import datetime

class Watcher:
    def __init__(self, symbol, entryPrice, stopLoss, takeProfit, confidence, isLong):
        self.creationDate = datetime.now()
        self.dailyCloses = []
        self.symbol = symbol
        self.stopLoss = stopLoss
        self.takeProfit = takeProfit
        self.entryPrice = entryPrice
        self.confidence = confidence
        self.isLong = isLong
    
    def didPricePassStopLoss(self, price):
        if (self.isLong and price <= self.stopLoss):
            return True
        elif (not self.isLong and price >= self.stopLoss):
            return True
        else:
            return False
    
    def didPricePassTakeProfit(self, price):
        if (self.isLong and price >= self.takeProfit):
            return True
        elif (not self.isLong and price <= self.takeProfit):
            return True
        else:
            return False