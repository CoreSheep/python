"""
    subclass constructor
"""


class Father(object):
    def __init__(self, name):
        self.name = name
        print("Hi, I'm a father, named after %s." % self.name)

    def getName(self):
        return 'Father ' + self.name

    def __del__(self):
        print("%s has been released." % self.name)


class Son(Father):
    def __init__(self, name):
        super(Son, self).__init__(name)
        self.name = name
        print("Hi, I'm a son, named after %s." % self.name)

    def getName(self):
        return 'Son ' + self.name


if __name__ == '__main__':
    son = Son('runoob')
    print(son.getName())