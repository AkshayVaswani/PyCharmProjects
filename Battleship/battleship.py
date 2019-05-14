from tkinter import *
from tkinter import messagebox

battleship = Tk()

beginning = "opening"

battleship.geometry("525x325")
battleship.title("Battleship")


def createButton(text, row, column):

    b = Button(text=text)
    b.config(command=lambda: click())
    b.config(height=2, width=8)
    b.grid(row=row, column=column)
    return b

def createLabels(text, row, column):
    w = Label(text=""+text)
    w.config(height=2, width=8)
    w.grid(row=row, column=column)
    return w

for i in range(1, 8):
    createLabels(str(i), 0, i)
    createLabels(str(i), i, 0)


def position(r, c):
    print("row: "+str(r) + " and column: " + str(c))
    arrBtn[r-1][c-1].config(text="X")


def first3():
    global beginning

def click():
    if beginning == "first":
        bshipcreate(3)




def bshipcreate(size):
    count = size-1


    """game start"""

arrBtn = []
arrStr = []
for i in range(1, 8):
    rowBtn = []
    rowStr = []
    for j in range(1, 8):
        rowBtn.append(createButton("~", i, j))
        rowStr.append('~')
    arrBtn.append(rowBtn)
    arrStr.append(rowStr)

messagebox.showinfo("Battleship!", "Choose three consecutive boxes to be your 3 block battleship!")
beginning = "first"




battleship.mainloop()