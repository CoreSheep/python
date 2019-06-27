'''
    draw calender
'''

import turtle as t
from python.dayTwo.TurtleFinder import fly, init

t.setup(600, 600)
t.color("#FFFFFF", "#FC5A5A")
t.begin_fill()
fly(-100, 50)
t.goto(-100, 100)
t.goto(100, 100)
t.setpos(100, 50)
t.setpos(-100, 50)
t.end_fill()
t.write(arg="MAY", move=False, align="center", font=("Arial", 100,
                                                       "normal"))
print(t.isvisible())
t.done()
