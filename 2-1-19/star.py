import turtle
alex = turtle.Turtle()
wn = turtle.Screen()
turtle.setup(500, 500)

wn.bgcolor("white")
alex.color("green")
alex.pensize(3)
alex.right(72)
def starSide(n):
    for i in range(n):
        alex.forward(100)
        alex.right(144)
starSide(5)

for i in range(5):
    starSide(5)
    alex.forward(250)
    alex.right(144)

wn.exitonclick()