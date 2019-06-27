'''
    producer and consumer
'''


class Process:
    def __init__(self, pcb):
        self.pid = pcb[0]
        self.pname = pcb[1]
        self.ptime = pcb[2]
        self.priority = pcb[3]

    def showProcess(self):
        print("Id:{:>10}".format(self.pid))
        print("Name:{:>10}".format(self.pname))
        print("Time:{:>10}".format(self.ptime))
        print("Priority:{:>10}".format(self.priority))


class Queue:
    def __init__(self):
        self.queue = []

    def get(self):
        if not len(self.queue):
            print("Empty queue.")
        else:
            head = self.queue[0]
            self.queue.reverse()
            self.queue.pop()
            self.queue.reverse()

    def showQueue(self):
        for q in self.queue:
            print("{}, ".format(q), end='')


class Semaphore:
    def __init__(self, count):
        self.count = count
        self.queue = Queue()


def P(s):
    s.count -= 1
    if s.count < 0:
        s.queue.append()




