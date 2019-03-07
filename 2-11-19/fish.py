import turtle
import random
alex=turtle.Turtle()
alex.color("red")
alex.pensize(5)
alex.penup()
wn= turtle.Screen()
turtle.setup(500, 500)
wn.bgcolor("Light Blue")
def drawFish(xpos, ypos, size, color):
    alex.penup()
    alex.setpos(xpos, ypos)
    alex.pensize(20)
    alex.seth(90)
    alex.color(color)
    alex.dot(size)
    alex.left(90)
    alex.pendown()
    alex.forward(30)
    alex.left(30)
    for i in range(3):
        alex.forward(30)
        alex.right(120)
    alex.penup()
def drawStarfish(xpos, ypos, size, color):
    alex.setpos(xpos, ypos)
    alex.pendown()
    alex.color(color)
    alex.pensize(size)
    for i in range(5):
        alex.forward(60)
        alex.right(144)
    alex.penup()
def drawSeagrass(xpos, length, color):
    alex.setpos(xpos, -300)
    alex.seth(0)
    alex.pendown()
    alex.color(color)
    alex.pensize(10)
    alex.left(45)
    for i in range(length):
        alex.circle(60, 90)
        alex.circle(-60, 90)
    alex.penup()

r = lambda: random.randint(0, 255)
n = lambda: random.randint(1, 10)
g = lambda: random.randint(1, 5)
for i in range(n()):
    drawFish(random.randint(-250, 250), random.randint(-250, 250), random.randint(20, 70), '#%02X%02X%02X' % (r(), r(), r()))
for i in range(n()):
    drawStarfish(random.randint(-250, 250), random.randint(-250, 250), random.randint(10, 30), '#%02X%02X%02X' % (r(), r(), r()))
for i in range(n()):
    drawSeagrass(random.randint(-250, 250), g(), '#%02X%02X%02X' % (0, r(), 0))

wn.exitonclick()