'''
    implements a priority queue

'''

# 定义优先级队列, 优先级 设为 启发函数 f(n) 值
# 用heapq来实现优先级队列，heapq的用法请参考https://www.cnblogs.com/Joyce-song94/p/7149440.html
import heapq


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        # 获取优先级最大(priority最小)的元素
        return heapq.heappop(self.elements)[1]


priority_queue = PriorityQueue()
priority_queue.put('A', 0)
priority_queue.put('B', 2)
priority_queue.put('C', 3)
priority_queue.put('D', 1)
print(priority_queue.get())
print(priority_queue.get())
print(priority_queue.get())
print(priority_queue.get())