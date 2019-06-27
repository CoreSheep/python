import turtle as t
import time


def fly(x, y):
    t.up()
    t.goto(x, y)
    t.down()


def init(title, width, height):
    t.title(title)
    t.screensize(width, height)


def interProfileLine():
    fly(0, 200)
    t.seth(-115)
    t.circle(500, 24)
    t.setx(0)
    t.seth(-90)
    t.circle(468, 25.1)


# -110,  90
def eye(x, y, size, color):
    fly(x, y)
    t.dot(size, color)


def mouse(x, y, heading):
    fly(x, y)
    t.seth(heading)
    t.circle(190, 78)


def main():
    init("My Finder", 600, 600)
    t.pencolor("black")
    t.fillcolor("#36AAEE")
    t.speed("normal")
    t.width(2)
    fly(0, 200)
    t.begin_fill()
    t.goto(-200, 200)
    t.goto(-200, -200)
    t.goto(0, -200)
    t.seth(95)
    interProfileLine()
    t.goto(0, -200)
    t.end_fill()

    t.fillcolor("white")
    t.begin_fill()
    interProfileLine()
    t.sety(-200)
    t.goto(200, -200)
    t.goto(200, 200)
    t.goto(0, 200)
    t.end_fill()

    eye(-110, 90, 40, "black")
    fly(0, 200)

    t.pensize(4)
    eye(110, 90, 40, "black")
    mouse(-110, -70, -39)
    t.exitonclick()


