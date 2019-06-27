'''
    a star search

'''


# 绘制网格单元里的内容，一个单元格里可能绘制不同的内容
# graph存储整个网格信息，包括长宽等
# id为该单元格的位置
# style为该单元格的属性，可以代表障碍墙，可以代表起点终点，以及其它需要绘制在单元格中的内容
# width表示绘制的长度
def draw_tile(graph, id, style, width):
    r = "."  # 默认是画“.”
    # 如果是style有number，那么单元格画数字，在本例中将画到达某个点的代价
    if 'number' in style and id in style['number']: r = "%d" % style['number'][
        id]

    # 如果style有point_to，那么单元格画表示方向的图标，代表搜索的方向
    if 'point_to' in style and style['point_to'].get(id, None) is not None:
        (x1, y1) = id
        (x2, y2) = style['point_to'][id]
        if x2 == x1 + 1: r = ">"
        if x2 == x1 - 1: r = "<"
        if y2 == y1 + 1: r = "v"
        if y2 == y1 - 1: r = "^"
    if 'start' in style and id == style['start']: r = "A"  # 起始点画A
    if 'goal' in style and id == style['goal']: r = "Z"  # 目标点画Z
    if id in graph.walls: r = "#" * width  # 如果是墙画#
    return r


# draw_grid是绘制整个网格空间
# width表示绘制的长度
# style为该单元格的属性，可以代表障碍墙，可以代表起点终点，以及其它需要绘制在单元格中的内容
# **style代表可以指定多个style参数，不只是一个，可以是任意多个
def draw_grid(graph, width=2, **style):
    for y in range(graph.height):
        for x in range(graph.width):
            print("%%-%ds" % width % draw_tile(graph, (x, y), style, width),
                  end="")
        print()

    # 定义网格基类


class SquareGrid:
    # 根据宽度和高度初始化
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []

        # 确定某一个id代表的点是否在网格空间内

    def in_bounds(self, id):
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height

        # 返回某一个点是否可以通过，即该点是否为墙

    def passable(self, id):
        return id not in self.walls

        # 返回某一个点的所有邻居，即上下左右4个邻居，注意处于网格边缘的点可能只有2个或3个邻居，墙边缘的点也是

    def neighbors(self, id):
        (x, y) = id
        results = [(x + 1, y), (x, y - 1), (x - 1, y), (x, y + 1)]
        if (x + y) % 2 == 0: results.reverse()  # aesthetics
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        return results

    # 定义带权网格,权重是单元格属性，仅依赖于边终点


class GridWithWeights(SquareGrid):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.weights = {}

        # 返回访问某个单元格的代价，weights是一个字典，需要初始化时候赋值

    def cost(self, from_node, to_node):
        return self.weights.get(to_node, 1)

    # 绘制一个10x10的网格图，每个单元格宽度为3，起点在(1,4)终点在(7,8)



testgrid = GridWithWeights(10, 10)
testgrid.walls = [(5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8)]
start, goal = (1, 4), (7, 8)
draw_grid(testgrid, width=3, start=start, goal=goal)