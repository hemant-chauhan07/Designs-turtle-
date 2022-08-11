import turtle
import time

t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor('black')
t.width(2)
t.speed(20)

col = ('white' , 'pink' , 'cyan')

for i in range(300):
    t.pencolor(col[i%3])
    t.forward(i*4)
    t.right(121)

time.sleep(5)