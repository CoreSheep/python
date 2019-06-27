import turtle as t

# 1.canvas
# screensize(canvwidth=None, canvheight=None, bg=None)
t.screensize(800, 100, 'purple')
t.setup(800, 600, 200, 200)

# 2. pen
"""
2.1 pen attribute
"""
t.pensize(10)   # alias width()
t.pencolor("red")
t.pencolor((1.0, 0.0, 0.0)) # print in red

t.speed(10)     # limit from 1 to 10

'''
2.2 pen movement
'''
t.penup()       # alias pu() and up()
t.pendown()     # alias pd() and down()
t.forward(10)   # alias fd()
t.backward(10)  # alias bd()
t.right(10)     # right(radian) alias rt() for right()
t.left(10)      # left(radian)  alias lt() for left()
t.goto(5, 5)    # goto(x, y)    alias setpos() and setposition() for goto()
t.circle(100, 360, 50)      # circle(radius, radian=360, step=0)
# The center is radius units left of the turtle

'''
2.3 pen controller
'''
t.fillcolor('yellow')
t.color('red', 'yellow')    # pencolor() and fillcolor()
t.filling()     # Is current state a filling state?
t.begin_fill()  # begin to fill
t.end_fill()    # end fill
t.hideturtle()  # alias ht() make the arrow of the turtle invisible
t.showturtle()  # alias st() make the arrow of the turtle visible


'''
2.4 global control command
'''
t.clear()       # clear windows but perverse current state of turtle
t.reset()       # clear windows and reset turtle state
t.undo()        # undo last operation
t.isvisible()   # return
# stamp()       # copy current graphics
t.done()        # end turtle
