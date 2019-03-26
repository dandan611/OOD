#
# べた書きで実装する
#

import random

JANKENWORD = ['ROCK','PAPER','SCISSORS']

ROCK = 1
PAPER = 2
SCISSORS =3

if __name__ == '__main__':

    # ジャンケン開始
    print('--- ジャンケン開始 ---\n')

    player1_win_count = 0
    player2_win_count = 0

    # ジャンケン実行
    for num in range(1,4):
        player1 = random.randint(1, 3)
        player2 = random.randint(1, 3)

        print('第{}回目'.format(num))
        print('player1 [{}] VS player2 [{}]'.format(JANKENWORD[player1-1],JANKENWORD[player2-1]))

        # 勝敗結果の表示
        if (player1 == ROCK and player2 == SCISSORS) \
          or (player1 == PAPER and player2 == ROCK) \
          or (player1 == SCISSORS and player2 == PAPER ):
            ## player1の勝利
            player1_win_count += 1
            print('->result:player1の勝利\n')
        elif (player2 == ROCK and player1 == SCISSORS) \
          or (player2 == PAPER and player1 == ROCK) \
          or (player2 == SCISSORS and player1 == PAPER ):
            ## player2の勝利
            player2_win_count += 1
            print('->result:player2の勝利\n')
        else:
            ## 両者引き分け　
            print('->result:両者引き分け\n')

    # 最終結果の表示
    print('--- ジャンケン終了--- \n')

    print('--- 最終結果--- ')
    print('勝利数：player1:{}回、player2:{}回'.format(player1_win_count,player2_win_count))

    # 勝敗結果
    if player1_win_count > player2_win_count :
        ## player1の勝利
        print('player1の勝利\n')
    elif  player1_win_count < player2_win_count :
        ## player2の勝利
        print('player2の勝利\n')
    else:
        ## 両者引き分け　
        print('両者引き分け\n')
