'''
    Hill Climbing search for Eight Queue
'''

import copy
from AI.EightQueue.RandomBoard import *

# 八皇后上的爬山法搜索
class queens:
    # 初始化numruns个随机棋盘，执行numruns次爬山搜索
    def __init__(self, numruns, verbocity):
        self.totalruns = numruns
        self.totalsucc = 0
        self.totalnumsteps = 0
        self.verbocity = verbocity
        # 初始化numruns个随机棋盘，执行numruns次爬山搜索
        for i in range(0, numruns):
            if self.verbocity == True:
                print("====================")
                print("BOARD", i)
                print("====================")
            self.mboard = board()  # 随机初始化棋盘
            self.cost = self.calc_cost(self.mboard)  # 计算当前棋盘的cost代价
            self.hill_solution()  # 执行爬山搜索

    # 爬山搜索算法
    def hill_solution(self):
        while 1:
            currViolations = self.cost  # 当前冲突个数，即启发式代价
            self.getlowercostboard()  # 找到能达到最小代价的一步（移动一个皇后）
            if currViolations == self.cost:  # 如果找不到更好的移动策略了，就退出
                break
            self.totalnumsteps += 1
            if self.verbocity == True:
                print("Board Violations", self.calc_cost(self.mboard))
                print(self.mboard) # 每次移动后都打印一下棋盘)

        if self.cost != 0:  # 如果找到的最佳棋局代价不为0，即还是有冲突
            if self.verbocity == True:
                print("NO SOLUTION FOUND")

        else:  # 如果找到了最佳棋局
            if self.verbocity == True:
                print("SOLUTION FOUND")
            self.totalsucc += 1
        return self.cost

        # 打印统计信息

    def printstats(self):
        print("Total Runs: ", self.totalruns)
        print("Total Success: ", self.totalsucc)
        print("Success Percentage: ", float(self.totalsucc) / float(
            self.totalruns))
        print("Average number of steps: ", float(self.totalnumsteps) / float(
            self.totalruns))

        # 计算当前棋盘的cost代价，有多少个冲突，代价就为多少

    def calc_cost(self, tboard):
        totalhcost = 0  # 记录横、竖冲突的个数
        totaldcost = 0  # 记录斜着冲突的个数
        for i in range(0, 8):
            for j in range(0, 8):
                # 如果发现一个皇后，开始统计冲突个数
                if tboard.board[i][j] == queue:
                    # 先看横、竖冲突个数
                    totalhcost -= 2  # 先把统计横竖冲突时候是从0到8，会记录自己位置也认为冲突，所以先减2排除到

                    for k in range(0, 8):
                        if tboard.board[i][k] == queue:
                            totalhcost += 1
                        if tboard.board[k][j] == queue:
                            totalhcost += 1

                            # 再统计东南、西南、东北、西北方向冲突的个数
                    k, l = i + 1, j + 1
                    while k < 8 and l < 8:
                        if tboard.board[k][l] == queue:
                            totaldcost += 1
                        k += 1
                        l += 1
                    k, l = i + 1, j - 1
                    while k < 8 and l >= 0:
                        if tboard.board[k][l] == queue:
                            totaldcost += 1
                        k += 1
                        l -= 1
                    k, l = i - 1, j + 1
                    while k >= 0 and l < 8:
                        if tboard.board[k][l] == queue:
                            totaldcost += 1
                        k -= 1
                        l += 1
                    k, l = i - 1, j - 1
                    while k >= 0 and l >= 0:
                        if tboard.board[k][l] == queue:
                            totaldcost += 1
                        k -= 1
                        l -= 1
        return ((totaldcost + totalhcost) / 2)

        # 找到能达到最小代价（最少冲突个数）的一步（移动一个皇后）

    def getlowercostboard(self):
        lowcost = self.calc_cost(self.mboard)
        lowestavailable = self.mboard

        # 尝试移动每一个皇后到每一个位置，计算每次移动后的冲突个数（代价），
        for q_row in range(0, 8):
            for q_col in range(0, 8):
                if self.mboard.board[q_row][q_col] == queue:
                    # 如果找到了一个皇后，尝试移动该皇后到每个空位
                    for m_row in range(0, 8):
                        for m_col in range(0, 8):
                            if self.mboard.board[m_row][m_col] != queue:
                                # 想象了一下移动后的棋盘，看看移动后的冲突数是不是减少了
                                tryboard = copy.deepcopy(self.mboard)
                                tryboard.board[q_row][q_col] = 0
                                tryboard.board[m_row][m_col] = queue
                                thiscost = self.calc_cost(tryboard)
                                # 如果是减少了到目前为止的最小代价，那么就用这个移动后的棋盘为最佳棋盘
                                if thiscost < lowcost:
                                    lowcost = thiscost
                                    lowestavailable = tryboard
        self.mboard = lowestavailable
        self.cost = lowcost


# 执行爬山搜索
mboard = queens(3, True)
mboard.printstats()