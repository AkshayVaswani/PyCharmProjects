import turtle
alex = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor("white")
alex.color("green")
alex.pensize(3)



def draw_poly(n, sz):
    angle = 360/n
    for i in range(n):
        alex.forward(sz)
        alex.left(angle)

draw_poly(8,45)



wn.exitonclick()