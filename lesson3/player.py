import random

class Player:
    """janken player class"""
    win_count = 0
    name = ''

    def __init__(self, name=None):
        self.name = name

    def setJanken(self):
        return random.randint(1, 3)

    def checkJankenWinResult(self, result):
        if result :
            self.win_count += 1 
        else:
            pass

class Murata(Player):
    name = ''

    def __init__(self):
        self.name = 'murata'

    def setJanken(self):
        # ROCK 戦略
        return 1

class Yamada(Player):
    name = ''

    def __init__(self):
        self.name = 'yamada'

    def setJanken(self):
        # PAPER 戦略
        return 2
