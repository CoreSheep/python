'''
    open file
    -r      read raise error when file not exists
    -w      write with overriding or creating a new file
    -x      write raise error when file exists
    -a      append txt
    -t      txt mode
    -b      binary mode
    -+      add additional operation
'''


def openTxtFile():
    f = open("/Users/sheepcore/Documents/python_fundation/venv/python/"
        "dayEight/Chinese.txt", "rb")  # read with txt form
    # f1 = open("Chinese.txt", "rb") # read with binary form
    print(f.readline())
    f.close()


def openBinaryFile():
    f = open("English.txt", "r")
    print(f.readline())
    f.close()


def traverseFileAtOnce():
    f = open("English.txt")
    print(f.read())
    f.close()


def traverseFileAtTimes():
    f = open("English.txt")
    text = f.read(1)
    while text != "":
        print(text, end="\t")
        text = f.read(1)
    f.close()


def write():
    f = open("f.txt", "w")
    f.write("\nYou know I love you.")
    # print(f.read())  not readable
    f.close()


def writeLines():
    f = open("f.txt", "w+")
    songs = ['Lucky you', '\tsidewalk', '\tsunflower\n']
    f.writelines(songs)
    f.write("I love python.\n")
    f.write("I love Java.\n")
    f.seek(4)       # seek(op) 0: head 1: current 2: EOF
    for line in f:
        print(line, end="")
    f.seek(0)
    print(f.readlines(7))
    f.close()


writeLines()




