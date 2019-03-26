import strategy

class Player:
    """janken player class"""
    win_count = 0
    name = None
    strategy = None

    def __init__(self, name=None):
        self.name = name
        self.strategy = strategy.RandomStrategy()

    def setJanken(self):
        return self.strategy.setStrategy()

    def checkJankenWinResult(self, result):
        if result :
            self.win_count += 1 
        else:
            pass

class Murata(Player):
    name = None
    strategy = None

    def __init__(self):
        self.name = 'murata'
        self.strategy = strategy.RandomStrategy()

class Yamada(Player):
    name = None
    strategy = None

    def __init__(self):
        self.name = 'yamada'
        self.strategy = strategy.PaperStrategy()
