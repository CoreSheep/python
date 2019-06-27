'''
    create random eight queue board
'''

import random

queue = "\033[1;35mQ\033[0m"


# 定义棋盘
class board:
    def __init__(self):
        self.board = [[0 for i in range(0, 8)] for j in range(0, 8)]
        # 随机放置8格皇后

        for i in range(0, 8):
            while 1:
                rand_row = random.randint(0, 7)
                rand_col = random.randint(0, 7)
                if self.board[rand_row][rand_col] == 0:
                    self.board[rand_row][rand_col] = queue
                    break

                    # 打印棋盘

    def __repr__(self):
        mstr = ""
        for i in range(0, 8):
            for j in range(0, 8):
                mstr = mstr + str(self.board[i][j]) + " "
            mstr = mstr + "\n"
        return (mstr)

myborad = board()
print(myborad)