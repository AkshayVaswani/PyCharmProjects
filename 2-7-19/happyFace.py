import turtle
alex = turtle.Turtle()
wn = turtle.Screen()
wn.screensize(1000, 1000)
wn.bgcolor("white")
alex.color("green")
alex.pensize(3)



def square(square_size):
    for i in range(4):
        alex.forward(square_size)
        alex.left(90)

def penMove(x, y):
    alex.penup()
    alex.setpos(x,y)
    alex.pendown()
def circle(radius):
    alex.dot(radius)

def eyes(radius, spaceBetween, penSize):
    alex.pensize(penSize)
    alex.dot(radius)
    penMove(alex.xcor()+spaceBetween, alex.ycor())
    alex.dot(radius)

def smile(penSize):
    alex.pensize(30)
    penMove(alex.xcor() - 200, alex.ycor() - 60)
    alex.right(90)
    alex.circle(130, 180)
    """
    alex.pensize(penSize)
    tempx = alex.xcor()-50
    tempy = alex.ycor()-30
    penMove(alex.xcor()-90, alex.ycor()-60)
    for i in range(30):
        alex.right(5)
        alex.penup()
        alex.forward(100)
        alex.pendown()
        alex.dot(penSize+10)
        penMove(tempx, tempy)"""

#https://docs.python.org/3.7/library/turtle.html#turtle-state

alex.color("medium purple")
alex.begin_fill()
penMove(-150, -150)
square(400)
penMove(alex.xcor()+200, alex.ycor()+200)
alex.end_fill()
alex.begin_fill()
alex.color("yellow")
circle(350)
alex.end_fill()
alex.color("black")
penMove(alex.xcor()-75, alex.ycor()+60)
eyes(60, 140, 10)
smile(30)

wn.exitonclick()