import turtle
import random
alex = turtle.Turtle()
alex.color("red")
alex.pensize(5)
alex.penup()
wn = turtle.Screen()
turtle.setup(800, 500)
wn.bgcolor("Light Blue")
alex.speed(10)

def moveTo(x, y):
    alex.penup()
    alex.goto(x, y)
    alex.pendown()

#Trees

def trunk():
    alex.color("brown")
    alex.pensize(40)
    alex.left(90)
    alex.forward(100)
def leaves():
    alex.color("green")
    moveTo(alex.xcor(), alex.ycor()+50)
    alex.dot(100)
    alex.left(115)
    alex.forward(40)
    alex.dot(100)
    alex.right(205)
    alex.forward(80)
    alex.dot(100)
def tree(x, y):
    moveTo(x, y)
    trunk()
    leaves()

#Bushes

def bushes(x, y, dotSize):
    alex.color("green")
    moveTo(x, y)
    alex.dot(dotSize)
    moveTo(alex.xcor()+20, alex.ycor())
    alex.dot(dotSize-10)
    moveTo(alex.xcor() - 40, alex.ycor()-10)
    alex.dot(dotSize-10)
    moveTo(alex.xcor(), alex.ycor()+10)
    alex.dot(dotSize-5)

#Flowers

def stems(x, y):
    moveTo(x, y)
    alex.setheading(90)
    alex.pensize(5)
    alex.color("light green")
    alex.forward(25)
def bud():
    alex.color("yellow")
    alex.dot(12)
def petals(color):
    alex.shape("circle")
    alex.turtlesize(0.6, 0.6, 0.6)
    alex.color(color)
    for i in range(5):
        alex.penup()
        alex.forward(7)
        alex.pendown()
        alex.stamp()
        alex.penup()
        alex.right(180)
        alex.forward(7)
        alex.pendown()
        alex.right((360/5)+180)
def flower(x, y, color):
    stems(x, y)
    petals(color)
    bud()

#grass
def blade(x, y, length):
    r = lambda: random.randint(0, 255)
    color = '#%02X%02X%02X' % (0, r(), 0)
    alex.color(color)
    moveTo(x, y)
    alex.pensize(3)
    alex.setheading(90)
    alex.forward(length-2)
    for i in range(10):
        alex.forward(2)
        alex.right(1)
def field(maxYCoor, number):
    for i in range(number):
        blade(random.randint(-400,400), random.randint(-250, maxYCoor), random.randint(3, 13))

#Clouds - Aryaman Tiwari
"""def cloud():
    alex.color("white")
    alex.penup()
    alex.goto(100, 100)
    alex.pendown()
    alex.setheading(0)
    alex.begin_fill()
    for x in range(2):
        alex.forward(60)
        alex.left(90)
        alex.forward(30)
        alex.left(90)
    alex.end_fill()"""
#^original code

def cloud(x, y, length, width):
    alex.color("white")
    alex.penup()
    alex.goto(x, y)
    alex.pendown()
    alex.setheading(0)
    alex.begin_fill()
    for x in range(2):
        alex.forward(length)
        alex.left(90)
        alex.forward(width)
        alex.left(90)
    alex.end_fill()
def clouds(number):
    for i in range(number):
        cloud(random.randint(-400, 400), random.randint(50, 220), random.randint(30, 70), random.randint(20, 40))

#scene

tree(300, -50)
field(-100, 10)
bushes(-200, -50, 30)
flower(100, -80, "white")
flower(-200, -100, "white")
clouds(3)


wn.exitonclick()


