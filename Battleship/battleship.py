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

initx = -1
inity = -1


def createButton(text, row, column):
    b = Button(text=text)
    b.config(command=lambda: click(column, row))
    b.config(height=2, width=8)
    b.grid(row=row, column=column)
    return b


def createLabels(text, row, column):
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


def first3():
    global beginning


def click(x, y):
    if beginning == "first":
        bshipcreate(3, x, y)


def bshipcreate(size, x, y):
    x -= 1
    y -= 1
    global initx, inity, count
    count = size - 1
    if count < size:
        if initx != -1 and inity != -1:
            if x == initx - 1 or x == initx + 1:
                initx = x
            if y == inity - 1 or y == inity + 1:
                inity = y
                arrStr[initx][inity] = 'o'
        else:
            initx = x
            inity = y
            arrStr[initx][inity] = 'o'

        count += 1
        for arrRow in arrStr:
            print(arrRow)
        print()

    """game start"""


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
beginning = "first"

battleship.mainloop()
