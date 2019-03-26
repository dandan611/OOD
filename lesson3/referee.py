import player

JANKENWORD = ['ROCK','PAPER','SCISSORS']

ROCK = 1
PAPER = 2
SCISSORS =3

class Referee:
    """janken referee class"""

    def __init__(self):
        pass

    def executeJanken(self, player1, player2):
        p1_janken = player1.setJanken()
        p2_janken = player2.setJanken()

        print('player1({}) [{}] VS player2({}) [{}]'.format(\
              player1.name,
              JANKENWORD[p1_janken-1],
              player2.name,
              JANKENWORD[p2_janken-1]))

        # 勝敗結果の表示
        if (p1_janken == ROCK and p2_janken == SCISSORS) \
          or (p1_janken == PAPER and p2_janken == ROCK) \
          or (p1_janken == SCISSORS and p2_janken == PAPER ):
            ## player1の勝利
            player1.checkJankenWinResult(True) 
            print('->result:player1({})の勝利\n'.format(player1.name))
        
        elif (p2_janken == ROCK and p1_janken == SCISSORS) \
          or (p2_janken == PAPER and p1_janken == ROCK) \
          or (p2_janken == SCISSORS and p1_janken == PAPER ):
            ## player2の勝利
            player2.checkJankenWinResult(True)
            print('->result:player2({})の勝利\n'.format(player2.name))
        
        else:
            ## 両者引き分け　
            print('->result:両者引き分け\n')

    def judgeFinalResult(self, player1, player2):
        if player1.win_count > player2.win_count :
            ## player1の勝利
            print('player1({})の勝利\n'.format(player1.name))
        elif  player1.win_count < player2.win_count :
            ## player2の勝利
            print('player2({})の勝利\n'.format(player2.name))
        else:
            ## 両者引き分け　
            print('両者引き分け\n')
