'''
    simple graph
'''

import collections


class Queue:
    def __init__(self):
        # built-in collections.deque class.
        # Feel free to use deque directly in your own code.
        self.elements = collections.deque()

    def empty(self):
        return len(self.elements) == 0

    def put(self, x):
        self.elements.append(x)

    def get(self):
        return self.elements.popleft()


class SquareGrid:
    def __init__(self, width, height):
        # define grid

        self.width = width
        self.height = height
        self.walls = []

    # Whether the node is in bounds of grid panel
    def in_bounds(self, location):
        (x, y) = location
        return 0 <= x < self.width and 0 <= y < self.height

    def passable(self, location):
        return location not in self.walls

    def neighbors(self, location):
        (x, y) = location
        # 定义移动方向

        # right, down, left, up
        directions = [(x + 1, y), (x, y - 1), (x - 1, y), (x, y + 1)]
        if (x + y) % 2 == 0: directions.reverse()      # aesthetics
        directions = filter(self.in_bounds, directions)
        # filter(func, sequence)
        directions = filter(self.passable, directions)
        return directions


# 根据 location 和 width 计算出 网格中的位置 (width,height)
# 这里 location 是节点的编号（0 ~ 30 * 15)
def from_loc_width(location, width):
    return location % width, location // width


# 绘制 单个网格
def draw_tile(graph, location, style, width):
    r = "."
    if 'number' in style and location in style['number']:
        r = "%d" % style['number'][location]

    if 'point_to' in style and style['point_to'].get(location, None) is not None:
        (x1, y1) = location
        (x2, y2) = style['point_to'][location]
        if x2 == x1 + 1: r = "→"
        if x2 == x1 - 1: r = "←"
        if y2 == y1 + 1: r = "↓"
        if y2 == y1 - 1: r = "↑"

    if 'start' in style and location == style['start']:
        r = "\033[1;32m◎\033[0m "
    if 'goal' in style and location == style['goal']:
        r = "\033[1;31m◉\033[0m "
    if 'path' in style and location in style['path']: r = "@"
    if location in graph.walls: r = "✖" * width
    return r


# 绘制 图 对象
def draw_grid(graph, width=2, **style):
    for y in range(graph.height):
        for x in range(graph.width):
            print("%%-%ds" % width % draw_tile(graph, (x, y), style, width),
                  end="")
        print()


# 定义Wall locations

DIAGRAM1_WALLS = [(1, 5), (2, 5), (3, 5), (3, 6), (3, 7)
                  ,(1, 4), (2, 4), (3, 4), (4, 4), (4, 5)
                  ,(4, 6), (4, 7), (4, 8), (3, 8), (2, 8)
                  ,(1, 8)
                  ,(1, 7), (2, 7)
                  ,(24, 0), (24, 1), (24, 2), (24, 3), (24, 4), (24, 5)
                  ,(24, 6), (24, 7), (24, 8), (24, 9), (24, 10), (24, 11)
                  ,(24, 12), (24, 14)
                  
                  ,(22, 0), (22, 1), (22, 2), (22, 3), (22, 5)
                  ,(22, 6), (22, 7), (22, 8), (22, 9), (22, 10), (22, 11)
                  ,(22, 12), (22, 13), (22, 14)
                  
                  ,(20, 0), (20, 1), (20, 3), (20, 4), (20, 5)
                  ,(20, 6), (20, 7), (20, 8), (20, 9), (20, 10), (20, 11)
                  ,(20, 12), (20, 13), (20, 14)

                  ,(18, 0), (18, 1), (18, 2), (18, 3), (18, 4), (18, 5)
                  ,(18, 6), (18, 7), (18, 8), (18, 9), (18, 10), (18, 11)
                  ,(18, 12), (18, 13)

                  , (16, 0), (16, 1), (16, 2), (16, 3), (16, 4), (16, 5)
                  , (16, 6), (16, 8), (16, 9), (16, 10), (16, 11)
                  , (16, 12), (16, 13), (16, 14)
                  
                  ,(10, 0), (10, 1), (10, 2), (10, 3), (10, 4), (10, 5)
                  ,(10, 6), (10, 7), (10, 8), (10, 9), (10, 10), (10, 11)
                  ,(10, 12), (10, 13)

                  , (9, 0), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5)
                  , (9, 6), (9, 8), (9, 9), (9, 10), (9, 11)
                  , (9, 12), (9, 13)

                  , (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5)
                  , (8, 6), (8, 7), (8, 8), (8, 9), (8, 10), (8, 11)
                  , (8, 12), (8, 13)


                  ]


# 增加起点和终点，用于特定路径的查询，当遍历到 goal 终点时则停止遍历.
def breadth_first_search(graph, start, goal):
    frontier = Queue()
    frontier.put(start)
    came_from = dict()
    came_from[start] = None

    while not frontier.empty():
        current = frontier.get()
        if current == goal:
            break
        for next in graph.neighbors(current):
            if next not in came_from:
                frontier.put(next)
                came_from[next] = current
    return came_from


def main():
    begin = (2, 6)
    end = (25, 12)
    g = SquareGrid(30, 15)
    g.walls = DIAGRAM1_WALLS
    parents = breadth_first_search(g, begin, end)
    # print(parents)
    draw_grid(g, width=2, point_to=parents, start=begin, goal=end)


main()