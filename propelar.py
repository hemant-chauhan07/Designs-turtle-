import turtle
import time

t = turtle.Turtle()
t.speed(50)
turtle.bgcolor('black')

colors = ('white' , 'pink' , 'magenta' , 'purple' , 'red')

for i in range(100):
    t.pencolor(colors[i%5])
    t.width(i/100+1)
    t.goto(0,0)
    t.pendown
    t.forward(100)
    t.right(59)
    t.forward(200)

time.sleep(5)