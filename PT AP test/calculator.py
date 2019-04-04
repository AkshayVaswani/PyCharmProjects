
from tkinter import *

calc = Tk()
counter = 0

lastnumber = 0

calc.geometry("359x425")
calc.title("Calculator")


equation = ''

screen = Text(calc, state='disabled', width=45, height=3, background="white", foreground="black", font=('Helvetica', '10'))
screen.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
screen.configure(state='normal')


def createButton(val, write, isint, width=10):
    return Button(calc, text=val, command=lambda: click(val, write, isint), width=width, height=3, font=('Helvetica', '10'))

#test
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
b23 = createButton('.', True, False)
b24 = createButton('=', False, False)

#symbols
#https://en.wikipedia.org/wiki/List_of_Unicode_characters

buttons = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19, b20, b21, b22, b23, b24]

count = 0
for row in range(1, 7):
    for column in range(4):
        buttons[count].grid(row=row, column=column)
        count += 1


def click(text, write, isint):
    global equation
    global lastnumber
    if isint:
        islastnum(text, True)
    else:
        islastnum(text, False)
    if write is False:
        if equation:
            if text == u"\u00B1":
                multiplybyneg()
            if text == '=':
                equation = re.sub(u"\u00F7", '/', equation)
                equation = re.sub(u"\u2715", '*', equation)
                print(equation)
                answer = str(eval(equation))
                clear_screen()
                insert_screen(answer)
            elif text == u"\u232B":
                clear_screen()
    else:
        insert_screen(text)

def islastnum(text, clearorna):
    global lastnumber
    if clearorna:
        lastnumber = int(str(lastnumber) + str(text))
        print("last" + str(lastnumber))
    else:
        if text != '=' and text != u"\u00B1":
            lastnumber = 0
            print("last" + str(lastnumber))

def multiplybyneg():
    global lastnumber
    lastnumber *= (-1)
    print(equation)
    refresh_screen()

def clear_screen():
    global equation
    global screen
    equation = ''
    screen.configure(state='normal')
    screen.delete('1.0', END)


def insert_screen(value):
    global screen
    global equation
    screen.configure(state='normal')
    screen.insert(END, value)
    equation = equation + str(value)
    screen.configure(state='disabled')

def refresh_screen():
    answer = str(eval(equation))
    clear_screen()
    insert_screen(answer)


calc.mainloop()