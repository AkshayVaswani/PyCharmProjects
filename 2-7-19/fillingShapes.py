import turtle
alex = turtle.Turtle()
wn = turtle.Screen()
wn.screensize(1000, 1000)
wn.bgcolor("white")
alex.color("green")
alex.pensize(3)



def rectangle(length, width, hexColor):
    alex.color(hexColor)
    alex.begin_fill()
    for i in range(2):
        alex.forward(width)
        alex.left(90)
        alex.forward(length)
        alex.left(90)
    alex.end_fill()
def penMove(x, y):
    alex.penup()
    alex.setpos(x,y)
    alex.pendown()

def circle(radius, hexColor):
    alex.color(hexColor)
    alex.begin_fill()
    alex.circle(radius)
    alex.end_fill()

def star(length, hexColor):
    alex.right(72)
    alex.color(hexColor)
    alex.begin_fill()
    for i in range(5):
        alex.forward(length)
        alex.right(144)
    alex.end_fill()
def curve():
    for i in range(200):
        alex.right(1)
        alex.forward(1)

def heart(hexColorFill, hexColorEdges):
    alex.color(hexColorEdges, hexColorFill)
    alex.begin_fill()
    alex.left(140)
    alex.forward(111.65)
    curve()
    alex.left(120)
    curve()
    alex.forward(111.65)
    alex.end_fill()

penMove(-200, 150)
rectangle(50, 20, "#7FFF00")
penMove(200, 150)
circle(50, "#7FFF00")
penMove(-200, -150)
star(50, "#7FFF00")
penMove(200, -150)
alex.left(70)
heart("#7FFF00", "#7FFF00")
wn.exitonclick()