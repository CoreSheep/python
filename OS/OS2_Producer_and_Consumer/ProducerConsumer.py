"""
    producer and consumer
"""
import random


class Pipe:
    def __init__(self):
        self.pipe = [-1, -1, -1, -1, -1, -1, -1, -1]
        self.wptr = 0
        self.rptr = 0
        self.size = 8
        self.count = (self.wptr + self.size - self.rptr) % self.size

    def isEmpty(self):
        return self.rptr == self.wptr

    def isFull(self):
        return (self.wptr + 1) % self.size == self.rptr

    def updateCount(self):
        self.count = (self.wptr + self.size - self.rptr) % self.size

    def read(self):
        if not self.isEmpty():
            pitem = self.pipe[self.rptr]
            self.rptr = (self.rptr + 1) % self.size
            self.updateCount()
            return True
        else:
            return False

    def write(self, pitem):
        if not self.isFull():
            self.pipe[self.wptr] = pitem
            self.wptr = (self.wptr + 1) % self.size
            self.updateCount()
            return True
        else:
            return False

    def cat(self):
        print("Pipe Status:")
        print("write ptr: {}\tread ptr: {}\t\tpsize: {} \tcount:{}".format(
            self.wptr, self.rptr, self.size, self.count))
        print("pipe items: ", self.pipe)


def produce(p, pitem):
    if p.write(pitem):
        print('produce an item successfully...')
    else:
        print("produce fail...")


def consumer(p):
    if p.read():
        print("consume an item successfully...")
    else:
        print("consume fail...")


def fetch():
    return random.randint(0, 99)


def show(p, pblock, cblock):
    p.cat()
    if len(pblock):
        print("produce block: {}".format(*pblock))
    if len(cblock):
        print("consume block: {}".format(*cblock))


if __name__ == '__main__':
    print("Producer is ready ...")
    print("Consumer is ready ...")
    print("*********************\n")
    print("P for Producer\nC for consumer\nZ for exit")
    processID = 0
    produceBlock = []
    consumeBlock = []
    p = Pipe()
    res = input("enter your choice(p / c / z): ")
    while res != 'z':
        if res == 'p':
            if p.isFull():
                print("pipe is full...")
                produceBlock.append(processID)
            else:
                produce(p, fetch())
        elif res == 'c':
            if p.isEmpty():
                print("pipe is empty...")
                consumeBlock.append(processID)
            else:
                consumer(p)
        show(p, produceBlock, consumeBlock)
        res = input("\n\nenter your choice(p / c / z): ")
        processID += 1

    print("exit...")





