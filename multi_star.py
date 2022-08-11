import turtle
import random
import time

from numpy import angle

turtle.speed(speed = 'fastest')


def draw(n, x, angle):
    for i in range(n):
        turtle.colormode(255)

        a = random.randint(0, 255)
        b = random.randint(0, 255)
        c = random.randint(0, 255)

        turtle.pencolor(a, b, c)
        turtle.fillcolor(a, b, c)
        turtle.begin_fill()

        for j in range(5):
            turtle.forward(5*n-5*i)
            turtle.right(x)
            turtle.forward(5*n-5*i)
            turtle.right(72-x)

        turtle.end_fill()

        # rt(angle)

n = 30
x = 144
angle = 18

draw(n, x, angle)

time.sleep(5)