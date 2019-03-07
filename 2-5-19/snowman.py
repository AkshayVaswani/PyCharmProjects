import turtle
alex=turtle.Turtle()
alex.color("red")
alex.pensize(5)
alex.penup()
wn= turtle.Screen()
wn.bgcolor("Light Blue")

def Body(body_color):
  alex.color(body_color)
  alex.dot(200)
  alex.goto(0, 150)
  alex.dot(120)
  alex.goto(0, -200)
  alex.dot(280)
def Eye(eye_color):
  alex.color(eye_color)
  alex.goto(-20, 160)
  alex.dot(15)
  alex.goto(20, 160)
  alex.dot(15)
def Buttons(button_color):
  alex.color(button_color)
  alex.home()
  y = 40
  for i in range(3):
      alex.goto(0,y)
      alex.dot(20)
      y = y-40
def Mouth(mouth_angle):
  alex.goto(5,140)
  for i in range(8):
      alex.right(mouth_angle)
      alex.forward(40)
      alex.dot(10)
      alex.goto(5,140)
  alex.home()

def Nose(nose_color):
  alex.color(nose_color)
  alex.goto(5,140)
  alex.stamp()

def Hat(hat_color):
  alex.color(hat_color)
  alex.goto(-75,200)
  alex.pensize(50)
  alex.pendown()
  alex.forward(150)
  alex.penup()
  alex.goto(0,225)
  alex.pendown()
  alex.pensize(100)
  alex.goto(0,250)
  alex.penup()

def Scarf(scarf_color):
  alex.color(scarf_color)
  alex.goto(-70,90)
  alex.pensize(30)
  alex.pendown()
  alex.goto(100,90)
  alex.goto(40,90)
  alex.left(315)
  alex.forward(90)

def Arms(arm_color):
  alex.penup()
  alex.color(arm_color)
  alex.goto(90,0)
  alex.pendown()
  alex.pensize(15)
  alex.left(100)
  alex.forward(120)
  alex.left(180)
  alex.forward(30)
  alex.left(130)
  alex.forward(30)
  alex.penup()
  alex.goto(-90,0)
  alex.pendown()
  alex.left(115)
  alex.forward(120)
  alex.left(180)
  alex.forward(30)
  alex.right(130)
  alex.forward(30)



Body("#FFFFFF")
Eye("#000000")
Buttons("#000000")
Mouth(20)
Nose("orange")
Hat("#000000")
Scarf("#00FF00")
Arms("brown")


wn.exitonclick()
