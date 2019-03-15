import turtle
import array
import random
alex = turtle.Turtle()
wn = turtle.Screen()
wn.screensize(1000, 1000)
wn.bgcolor("white")
alex.color("green")
alex.pensize(3)
alex.speed(12)

"""
class Circles:

    def circleMake(self, size, color):
        alex.color(color)
        alex.dot(size)
    def circleSpam(self, number):
        for i in range(number):
            self.num = number
            self.xCoor = [0]*number
            self.yCoor = [0]*number
            self.size = [0]*number
            x = random.randint(-250, 250)
            y = random.randint(-250, 250)
            r = lambda: random.randint(0, 255)
            col = ('#%02X%02X%02X' % (r(), r(), r()))
            si = random.randint(10, 100)
            alex.penup()
            alex.goto(x, y)
            alex.pendown()
            self.circleMake(si, col)
            self.xCoor[i]
            self.yCoor.append(y)
            self.size.append(si)
    def erase(self):
        for i in range(self.num, self.num*2):
            alex.penup()
            alex.goto(self.xCoor[i], self.yCoor[i])
            print(str(self.xCoor[i])+ " "+ str(self.yCoor[i]))
            alex.pendown()
            #alex.dot(self.size[i])
            self.circleMake(self.size[i], "white")
"""
#s=Circles()
#s.circleSpam(random.randint(0, 100))
#s.circleSpam(10)
#s.erase()
def circlemake(size, color):
    alex.color(color)
    alex.dot(size)
def circlespam(number):
    xcoor = [None] * number
    print(len(xcoor))
    ycoor = [None] * number
    print(len(ycoor))
    size = [None] * number
    print(len(size))
    for i in range(number):
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        n = lambda: random.randint(0, 255)
        col = ('#%02X%02X%02X' % (n(), n(), n()))
        si = random.randint(10, 100)
        alex.penup()
        alex.goto(x, y)
        alex.pendown()
        circlemake(si, col)
        xcoor[i] = x
        ycoor[i] = y
        size[i] = si
    erase(number, xcoor, ycoor, size)


def erase(num, x, y, si):
    for i in range(num):
        alex.penup()
        alex.goto(x[i], y[i])
        print(str(x[i]) + " " + str(y[i]))
        alex.pendown()
        circlemake(si[i], "white")

circlespam(50)



wn.exitonclick()


