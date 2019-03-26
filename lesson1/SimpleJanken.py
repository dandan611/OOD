#
# べた書きで実装する
#

import random

if __name__ == '__main__':

    # ジャンケン開始
    print('--- ジャンケン開始 ---\n')

    # ジャンケン実行

    for num in range(1,4):
        player1 = random.uniform(0, 3)
        player2 = random.uniform(0, 3)

        print('第{}回目'.format(num))

        print(player1)
        print(player2)

        print('結果\n')

    # 結果の表示
    print('--- ジャンケン終了--- \n')

