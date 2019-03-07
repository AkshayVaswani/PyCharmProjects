import turtle
alex=turtle.Turtle()
alex.color("red")
alex.pensize(5)
alex.penup()
wn= turtle.Screen()
wn.bgcolor("Light Blue")

count = 0
color = "#FF0099"
size = 280
for i in range(6):
  if count %2 == 0:
      alex.color("#0000FF")
  if count %2 == 1:
      alex.color("#5500FF")
  alex.dot(size)
  size = size - 50
  count = count+1
wn.exitonclick()
