from tkinter import *
from tkinter import messagebox

battleship = Tk()
battleship.withdraw

beginning = "opening"

battleship.geometry("525x325")
battleship.title("Battleship")

arrBtn = []
arrStr = []

count = 0
countBtn = 0


initx = -1
inity = -1


def createButton(text, column, row):
    b = Button(text=text)
    b.config(command=lambda: click(column, row))
    b.config(height=2, width=8)
    b.grid(row=row, column=column)
    return b


def createLabels(text, column, row):
    w = Label(text="" + text)
    w.config(height=2, width=8)
    w.grid(row=row, column=column)
    return w


for i in range(1, 8):
    createLabels(str(i), 0, i)
    createLabels(str(i), i, 0)


def position(r, c):
    print("row: " + str(r) + " and column: " + str(c))
    arrBtn[r - 1][c - 1].config(text="X")


def first3(x, y):
    global beginning
    if beginning == "first2":
        bshipcreate(3, x, y, True)
    if "first" in beginning:
        beginning = "first" + str(count)
        bshipcreate(3, x, y, False)

def second2(x, y):
    global beginning
    if beginning == "second1":
        bshipcreate(2, x, y, True)
    if "second" in beginning:
        beginning = "second" + str(count)
        bshipcreate(2, x, y, False)

def third2(x, y):
    global beginning
    if beginning == "third1":
        bshipcreate(2, x, y, True)
    if "third" in beginning:
        beginning = "third" + str(count)
        bshipcreate(2, x, y, False)

def click(x, y):
    if "first" in beginning:
        first3(x, y)
        print("1"+str(count))
    if "second" in beginning:
        second2(x, y)
        print("2"+str(count))
    if "third" in beginning:
        third2(x, y)
        print("3"+str(count))


def bshipcreate(size, x, y, done):
    x -= 1
    y -= 1
    global initx, inity, count, beginning
    if count < size and not done:
        print("test" + str(count))
        if initx > -1 and inity > -1:
            if (x == initx - 1 or x == initx + 1 or x == initx) and (y == inity - 1 or y == inity + 1 or y == inity):
                initx = x
                inity = y
                arrStr[inity][initx] = 'o'
                count += 1
            else:
                initx = -2
                inity = -2
        else:
            initx = x
            inity = y
            arrStr[inity][initx] = 'o'
            print("adding now" + str(count))
            count += 1


    if done:
        if "third" in beginning:
            beginning = "game"
            print(beginning)
            initx = -1
            inity = -1
        if "second" in beginning:
            beginning = "third"
            count = 0
            initx = -1
            inity = -1
        if "first" in beginning:
            beginning = "second"
            count = 0
            initx = -1
            inity = -1



    printmethod()

def printmethod():
    print()
    for arrRow in arrStr:
        print(arrRow)

    """game start"""

beginning = "first"
for i in range(1, 8):
    rowBtn = []
    rowStr = []
    for j in range(1, 8):
        rowBtn.append(createButton("~", i, j))
        rowStr.append('~')
    arrBtn.append(rowBtn)
    arrStr.append(rowStr)

#messagebox.showinfo("Battleship!", "Choose three consecutive boxes to be your 3 block battleship!")
#battleship.update()


battleship.mainloop()
