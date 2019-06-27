'''
    process management triple state
    ready, running and blocked
'''
import turtle as t

'''
    i.Format:
    \033[显示方式;前景色;背景色m要打印的字符串\033[0m
    \033[1;32;41m   #---1-高亮显示 32-前景色绿色  40-背景色红色---
    \033[0m         #---采用终端默认设置，即缺省颜色--- 
    
    ii.Text Mode:
        0.default       print("\033[0mText")
        1.bold:         print("\033[1mText")
        2.underline     print("\033[4mText")
        3.block         print("\033[7mText")
        4.blink         print("\033[5mText")
        
    iii.Text Color:         foreground(3x) background(4x)
        0.white         print("\033[30mText mode")
        1.red           print("\033[31mText mode")
        2.light green   print("\033[32mText mode")
        3.yellow        print("\033[33mText mode")
        4.blue          print("\033[34mText mode")
        5.purple        print("\033[35mText mode")
        6.cyan          print("\033[36mText mode")
        7.grey          print("\033[37mText mode")
        8.light grey    print("\033[38mText mode")
        
        
'''



# create three queues
ready = [("b", 2), ("c", 1)]
running = [("a", 1)]
blocked = [("d", 2)]
newblocked = []


def blink(text):
    print("\033[5m" + text + "\033[0m")


def getReady():
    '''
    get the head of ready queue
    :return: head
    '''
    head = ready[0]
    ready.reverse()
    ready.pop()
    ready.reverse()
    return head


def getBlocked():
    '''
    pop the head of blocked queue
    :return: head
    '''
    head = blocked[0]
    blocked.reverse()
    blocked.pop()
    blocked.reverse()
    return head


def show():
    '''
    show process state
    :return: None
    '''
    print("\033[0;33m{0:-<30}".format(""))
    print("\033[1;32mReady:  ", end=" ")
    for i in range(len(ready)):
        name, time = ready[i]
        if i < len(ready) - 1:
            print("({}, {})".format(name, time), end=" -> ")
        else:
            print("({}, {})".format(name, time), end="")
    print("\n\033[1;33mRunning:", end=" ")
    for i in range(len(running)):
        name, time = running[i]
        if i < len(running) - 1:
            print("({}, {})".format(name, time), end=" -> ")
        else:
            print("({}, {})".format(name, time), end="")
    print("\n\033[1;31mBlocked:", end=" ")
    for i in range(len(blocked)):
        name, time = blocked[i]
        if i < len(blocked) - 1:
            print("({}, {})".format(name, time), end=" -> ")
        else:
            print("({}, {})".format(name, time), end="")
    print("\n\033[33m{0:-<30}".format("") + "\033[0m")
    print()


def new():
    if len(ready) >= 5:
        print("Memory is running out.")
        newblocked.append()

    else:
        pname, ptime = input("input new process(name, time): ").split(',')
        ready.append((pname, ptime))
        print("A new process has been created successfully.")


def dispatch():
    if len(ready) == 0:
        blink("No process to dispatch!")
    else:
        if not len(running):
            running.append(getReady())

        else:
            blink("Process " + running[0][0]
                  + " has been swapped out due priority.")
            ready.append(running.pop())
            running.append(getReady())
        blink("Process " + running[0][0] + " is running now.\n")


def timeout():
    if len(running) == 0:
        blink("No process is running.")
    else:
        ready.append(running.pop())
        blink("Process " + ready[-1][0] + " is timeout.")


def eventWait():
    blocked.append(running.pop())
    blink("Process " + blocked[-1][0] + " has been blocked.")
    dispatch()


def eventOccurs():
    if len(blocked):
        ready.append(getBlocked())
        if not len(running):
            dispatch()


def release():
    if len(running):
        blink("Process " + running[-1][0] + " has been released.")
        running.pop()
        dispatch()
    else:
        blink("No process is running.")


def process(state):
    '''
    1: dispatch 2: timeout 3:event wait 4: event occurs
    :param state:
    :return: None
    '''
    if state == 0:
        new()
    if state == 1:
        dispatch()
    elif state == 2:
        timeout()
        dispatch()

    elif state == 3:
        eventWait()
    elif state == 4:
        eventOccurs()
    elif state == 5:
        release()
    else:
        print("StateError: illegal state!")


def stateMap():
    t.setup(850, 400, 200, 200)
    t.fd(100)
    t.done()


def main():
    show()
    while True:
        print("Trigger Event(\033[1;31mnew: 0 \033[2;32mdispatch: 1 \033["
              "1;33mtimeout: 2 \033[1;34msleep: 3 \033[1;35mawait: 4 "
              "\33[1;36mrelease: 5 \033[0;30m): ",
              end=""
              )
        state = input()
        process(eval(state))
        show()
        print()


main()
