import turtle
alex = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor("white")
alex.color("green")
alex.pensize(3)
def plusSign():
    alex.left(90)
    for i in range(4):
        alex.forward(100)
        alex.left(180)
        alex.forward(100)
        alex.right(90)
def lines():
    for i in range(4):
        alex.forward(75)
        alex.left(90)
        alex.forward(25)
        alex.right(180)
        alex.forward(50)
        alex.left(180)
        alex.forward(25)
        alex.left(90)
        alex.forward(75)
        alex.right(270)





plusSign()
lines()

wn.exitonclick()