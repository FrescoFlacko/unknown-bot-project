from datetime import datetime

class Trade:
    def __init__(self, ticker, entryPrice, exitPrice, profit, confidence, entryDate):
        self.ticker = ticker
        self.entryPrice = entryPrice
        self.exitPrice = exitPrice
        self.profit = profit
        self.confidence = confidence
        self.entryDate = entryDate
        self.exitDate = datetime.now()