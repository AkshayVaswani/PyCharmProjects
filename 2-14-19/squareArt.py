import turtle
alex = turtle.Turtle()
wn = turtle.Screen()
wn.screensize(1000, 1000)
wn.bgcolor("white")
alex.color("black")
alex.pensize(3)
alex.speed(12)
def square(sideLength):
    for i in range(4):
      alex.forward(sideLength)
      alex.left(90)

def circleArt(sideLength, quantity):
    angle = 360 / quantity;
    for i in range(quantity):
        square(sideLength)
        alex.right(angle)

circleArt(100, 72)
wn.exitonclick()
