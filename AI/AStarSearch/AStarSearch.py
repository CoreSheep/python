'''
    a star search
'''

from AI.AStarSearch.BuildGrid import *
from AI.AStarSearch.PriorityQueue import *

# a_star_search为A*搜索算法，graph为网格图，start起始点，goal目标点
# frontier为按照f(n)估计代价维护的优先级队列，即有优先级支持的探索集（探索边缘）
# came_from[next] = current 记录next顶点是从current顶点走过来的，其实就是记录访问序列
# cost_so_far[v] 记录到达v顶点的路径的代价累积和

# 启发式代价函数为当前位置到目的位置的曼哈顿距离
def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    # 计算曼哈顿距离
    return abs(x1 - x2) + abs(y1 - y2)

def a_star_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()  # 从优先级队列里取估计代价最小的点

        if current == goal:  # 判断是否为目标顶点
            break

        for next in graph.neighbors(current):  # 遍历该点周围的点，越界的和处于墙上的单元格已经排除
            new_cost = cost_so_far[current] + graph.cost(current,
                                                         next)  # 更新到达该邻居的实际代价

            # 如果该邻居没被访问过，或者已访问过但是代价更小，那么到达该点的新路径要更新一下
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost

                # 启发式代价作为优先级 ： f(n) = g(n) + h(n)
                priority = new_cost + heuristic(goal, next)
                frontier.put(next, priority)  # 加入frontier优先级探索集
                came_from[next] = current  # 更新到达该点的源节点，即更新到达该点的新路径

    return came_from, cost_so_far  # 返回记录到达每个点的路径came_from，和到达每个点的cost代价

def main():
    # 定义一个10x10网格图
    grid = GridWithWeights(10, 10)

    # 定义障碍墙
    grid.walls = [(1, 7), (1, 8), (2, 7), (2, 8), (3, 7), (3, 8)]

    # 定义单元格代价，访问这些单元格的代价都是5，所以尽量少访问这些单元格
    grid.weights = {loc: 5 for loc in [(3, 4), (3, 5), (4, 1), (4, 2),
                                       (4, 3), (4, 4), (4, 5), (4, 6),
                                       (4, 7), (4, 8), (5, 1), (5, 2),
                                       (5, 3), (5, 4), (5, 5), (5, 6),
                                       (5, 7), (5, 8), (6, 2), (6, 3),
                                       (6, 4), (6, 5), (6, 6), (6, 7),
                                       (7, 3), (7, 4), (7, 5)]}

    start, goal = (1, 4), (7, 8)

    # 执行A*搜索，返回路径和代价结果
    came_from, cost_so_far = a_star_search(grid, start, goal)

    # 绘制探索路径，> < v ^ 代表搜索路径
    draw_grid(grid, width=3, point_to=came_from, start=start, goal=goal)
    print()

    # 绘制到达的每个点的代价
    draw_grid(grid, width=3, number=cost_so_far, start=start, goal=goal)
    print()
main()