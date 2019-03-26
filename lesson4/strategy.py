import random

class Strategy:
    def __init__(self):
        pass

    def setStrategy(self):
        return None

class RandomStrategy(Strategy):
    def setStrategy(self):
        return random.randint(1, 3)

class InteractionStrategy(Strategy):
    def setStrategy(self):
        pass

class RockStrategy(Strategy):
    def setStrategy(self):
        return 1

class PaperStrategy(Strategy):
    def setStrategy(self):
        return 2
