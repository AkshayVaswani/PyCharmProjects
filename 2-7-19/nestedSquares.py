import turtle
alex = turtle.Turtle()
wn = turtle.Screen()
wn.screensize(1000, 1000)
wn.bgcolor("white")
alex.color("green")
alex.pensize(3)

def square(sideLength):
    alex.begin_fill()
    for i in range(4):
        alex.forward(sideLength)
        alex.left(90)
    alex.end_fill()

for p in range(4):
    size = 280
    num = 136
    for j in range(10):
        hexColor = '#%02x%02x%02x' % (num, num, num)
        print(hexColor)
        alex.color(hexColor)
        square(size)
        size = size - 30
        num = num-10
    alex.right(90)


wn.exitonclick()