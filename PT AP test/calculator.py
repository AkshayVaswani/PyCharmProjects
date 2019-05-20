
from tkinter import *

calc = Tk()
counter = 0

# variable instantiation

lastnumber = float(0)
lastnumberlength = 0

calc.geometry("359x425")
calc.title("Calculator")


equation = ''

# creating the top text box in which all data is explained
screen = Text(calc, state='disabled', width=45, height=3, background="white", foreground="black", font=('Helvetica', '10'))
screen.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
screen.configure(state='normal')

# recalled method to create buttons


def createButton(val, write, isint, width=10):
    return Button(calc, text=val, command=lambda: click(val, write, isint), width=width, height=3, font=('Helvetica', '10'))

# Creating all the buttons with each individual requirement
b1 = createButton("%", False, False)
b2 = createButton(u"\u221A", True, False)
b3 = createButton("x²", True, False)
b4 = createButton(u"\u00B9" + u"\u2044" + u"\u2093", False, False)
b5 = createButton("CE", False, False)
b6 = createButton("C", False, False)
b7 = createButton(u"\u232B", False, False)
b8 = createButton(u"\u00F7", True, False)
b9 = createButton(7, True, True)
b10 = createButton(8, True, True)
b11 = createButton(9, True, True)
b12 = createButton(u"\u2715", True, False)
b13 = createButton(4, True, True)
b14 = createButton(5, True, True)
b15 = createButton(6, True, True)
b16 = createButton('-', True, False)
b17 = createButton(1, True, True)
b18 = createButton(2, True, True)
b19 = createButton(3, True, True)
b20 = createButton('+', True, False)
b21 = createButton(u"\u00B1", False, False)
b22 = createButton(0, True, True)
b23 = createButton(".", True, True)
b24 = createButton('=', False, False)

# symbols
# https://en.wikipedia.org/wiki/List_of_Unicode_characters

# creating an array out of all the buttons
buttons = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19, b20, b21, b22, b23, b24]


# setting up the grid for the buttons in desired positions
count = 0
for row in range(1, 7):
    for column in range(4):
        buttons[count].grid(row=row, column=column)
        count += 1

# function called when button is clicked
def click(text, write, isint):
    global equation
    global answer
    global lastnumber
    if isint:
        islastnum(text, True)
    else:
        islastnum(text, False)
    if write is False:
        if equation:
            if text == u"\u00B1":   # plus/minus button
                multiplybyneg()
            if text == '=':
                equation = re.sub(u"\u00F7", '/', equation)  # re subbing certain characters in my equation string
                equation = re.sub(u"\u2715", '*', equation)
                print(equation)
                answer = str(eval(equation))       # solving equation
                lastnumber = float(answer)
                print("lastnum " + str(lastnumber))
                clear_screen()
                insert_screen(answer)
            elif text == u"\u232B":
                deletelast()
            elif text == 'C':
                lastnumber = 0
                clear_screen()

    else:
        insert_screen(text)


# function used to find last inputted number

def islastnum(text, clearorna):
    global lastnumber
    if clearorna:
        lastnumber = (str(lastnumber) + str(text))
        print("last1: " + str(lastnumber))
    else:
        if text != '=' and text != u"\u00B1" and text != '.':
            lastnumber = 0
            print("last2: " + str(lastnumber))
# function to multiply last inputted variable by negative 1
def multiplybyneg():
    global lastnumber
    global lastnumberlength
    global equation
    print(str(lastnumber) + " first")
    lastnumberlength = int(len(str(lastnumber)))
    lastnumber = lastnumber * (-1)
    print("not annexed yet" + equation)
    equation = equation[:-lastnumberlength]
    print("not added to yet:" + equation)
    equation += str(lastnumber)
    print(lastnumber)
    print("annexed: "+equation)
    refresh_screen()


# function to delete last number or digit from string

def deletelast():
    global equation
    global lastnumber
    equation = equation[:-1]
    print("del E: " + equation)
    lastnumber = lastnumber // 10  # trying to remove the last number from the lastnumber variable so I can accuratly turn it negative
    print("del"+str(lastnumber))
    refresh_screen()


# clears screen and empties variable

def clear_screen():
    global equation
    global screen
    equation = ''
    screen.configure(state='normal')
    screen.delete('1.0', END)

# inserts values to screen

def insert_screen(value):
    global screen
    global equation
    screen.configure(state='normal')
    screen.insert(END, value)
    equation = equation + str(value)
    screen.configure(state='disabled')

# refreshes screen and re-evaluates equation

def refresh_screen():
    answer = str(eval(equation))
    clear_screen()
    insert_screen(answer)


calc.mainloop()