import turtle
import time

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('white')

t.pencolor('green')
t.speed(11)

for i in range(55):
    t.circle(190-1 , 90)
    t.lt(98)
    t.circle(190-1 , 90)
    t.lt(18)

time.sleep(5)