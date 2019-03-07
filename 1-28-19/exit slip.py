import turtle
import math
alex = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor("white")
alex.color("green")
alex.pensize(3)
size=20
def square(size):
    for i in range(4):
        alex.forward(size)
        alex.left(90)

for i in range(5):
    square(size)
    alex.penup()
    alex.right(135)
    alex.forward(math.sqrt(200))
    alex.left(135)
    alex.pendown()
    size = size + 20


wn.exitonclick()