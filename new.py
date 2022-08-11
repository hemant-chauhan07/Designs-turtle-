import turtle
import colorsys
import time


t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('white')
t.speed(0)

n = 200
h = 0

for j in range(150):
    t.begin_fill()
    for i in range(2):
        c = colorsys.hsv_to_rgb(h, 0, 0)
        h+= 1/n
        t.color(c)
        t.left(20)
        t.forward(j-i)
    t.end_fill()
time.sleep(5)