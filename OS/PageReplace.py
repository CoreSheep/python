"""
    page replace
"""
import random


class Page:
    """page"""
    def __init__(self, id=0):
        self.id = id
        self.isAccessed = False


class Queue:
    """模拟队列"""
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def add(self, item):
        self.items.append(item)

    def get(self):
        if not self.isEmpty():
            head = self.items[0]
            self.items = self.items[1:]
            return head

    def show(self):
        print('Access_Series: ', end='')
        for item in self.items:
            print(str(item.id) + '\t', end='')
        print()


class Stack:
    """模拟栈"""

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if not self.isEmpty():
            return self.items[len(self.items) - 1]

    def contains(self, item):
        for i in self.items:
            if(item.id == i.id):
                return True
        return False

    def size(self):
        return len(self.items)

    def show(self):
        print('Frame: ', end='')
        for item in self.items:
            print(str(item.id) + '\t', end='')
        print()


Access_Series = Queue()
AccessSize = 10
global hit
global diseffect
global FrameSize
FrameSize = 4
AccessSize = 5


for i in range(AccessSize):
    Access_Series.add(Page(random.randint(1, AccessSize)))

print(Access_Series)

Frame = Stack()

Frame.push(Page(1))
print(Frame.contains(Page(1)))


def FIFO():
    hit = 0
    diseffect = 0
    # read page from Access_Series Queue
    while not Access_Series.isEmpty():
        Access_Series.show()
        Frame.show()
        page = Access_Series.get()
        if Frame.contains(page):
            hit += 1
        else:
            if Frame.size() < FrameSize:      # 有空闲内存块
                Frame.push(page)              # 加入Frame中
                diseffect += 1
            else:
                Frame.pop()
                Frame.push(page)
                diseffect += 1  # 缺页数加一
    return hit, diseffect


def show(hit, diseffect):
    print("hit rate: %{:.2f}".format(100*(hit / AccessSize)))
    print("diseffect rate: %{:.2f}".format(100*(diseffect / AccessSize)))


if __name__ == '__main__':
    result = FIFO()
    show(*result)