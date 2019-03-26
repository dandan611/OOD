#
# オブジェクト指向プログラム実装
#

import player
import referee

JANKENWORD = ['ROCK','PAPER','SCISSORS']

ROCK = 1
PAPER = 2
SCISSORS =3

if __name__ == '__main__':

    # プレイヤーの準備
    murata = player.Murata()
    yamada = player.Yamada()

    # 進行役の準備
    referee = referee.Referee()

    # ジャンケン開始
    print('--- ジャンケン開始 ---\n')

    # ジャンケン実行
    for num in range(1,4):
        print('第{}回目'.format(num))
        referee.executeJanken(murata,yamada)

    # 最終結果の表示
    print('--- ジャンケン終了--- \n')

    print('--- 最終結果--- ')
    print('勝利数：player1:{}回、player2:{}回'.format(murata.win_count,yamada.win_count))

    # 勝敗結果
    referee.judgeFinalResult(murata, yamada)
