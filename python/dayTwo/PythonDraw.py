import turtle as t
t.setup(850, 350, 200, 200)  # width, height, startX, startY
t.penup()
t.backward(250)
t.pendown()
t.pencolor("purple")
t.pensize(25)
t.setheading(-40)
for i in range(5):
    t.circle(40, 80)
    t.circle(-40, 80)
t.circle(40, 80/2)
t.forward(40)
t.circle(16, 180)
t.forward(40 * 2 / 3)
t.done()


