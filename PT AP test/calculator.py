from tkinter import *

calc = Tk()
counter = 0

calc.geometry("375x450")
calc.title("Calculator")


equation = ''


ent = Entry(calc, textvariable=equation, state='disabled', width=11, font="Helvetica 44 bold", justify="center", bg="#1E6FBA",fg="yellow", disabledbackground="#1E6FBA", disabledforeground="yellow", highlightbackground="black", highlightcolor="red", highlightthickness=1, bd=0)
ent.configure(disabledbackground="white", disabledforeground="black")
#ent.grid(columnspan=4, ipadx=70)
ent.grid(row=0, column=0, columnspan=4, padx=4, pady=5)
#ent.configure(state='normal')


def createButton(val, write=True, width=10):
    return Button(calc, text=val, command=lambda: click(val, write), width=width, height=3, font=('Helvetica', '10'))
#test
b1 = createButton("%")
b2 = createButton(u"\u221A", None)
b3 = createButton("x²")
b4 = createButton(u"\u00B9" + u"\u2044" + u"\u2093", None)
b5 = createButton("CE")
b6 = createButton("C")
b7 = createButton(u"\u232B", None)
b8 = createButton(u"\u00F7")
b9 = createButton(7)
b10 = createButton(8)
b11 = createButton(9)
b12 = createButton(u"\u2715")
b13 = createButton(4)
b14 = createButton(5)
b15 = createButton(6)
b16 = createButton('-')
b17 = createButton(1)
b18 = createButton(2)
b19 = createButton(3)
b20 = createButton('+')
b21 = createButton(u"\u00B1")
b22 = createButton(0)
b23 = createButton('.')
b24 = createButton('=', None)

#symbols
#https://en.wikipedia.org/wiki/List_of_Unicode_characters




buttons = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19, b20, b21, b22, b23, b24 ]

count = 0
for row in range(1, 7):
    for column in range(4):
        buttons[count].grid(row=row, column=column)
        count += 1


def click(text, write):
    global equation
    if write is None:
        if text == '=' and equation:
            equation = re.sub(u"\u00F7", '/', equation)
            equation = re.sub(u"\u2715", '*', equation)
            answer = str(eval(equation))
            clear_screen()
            print(equation.get())
            insert_screen(answer)
        elif text == u"\u232B":
            clear_screen()
    else:
        insert_screen(text)


def clear_screen():
    global equation
    global ent
    equation = ''
    ent.configure(state='normal')
    ent.delete('1.0', END)


def insert_screen(value):
    global ent
    global equation
    #ent.configure(state='normal')
    ent.insert(END, value)
    equation = str(value)
    ent = equation.get()
    ent.configure(state='disabled')
calc.mainloop()










"""











from tkinter import *


class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Python Calculator")

        # create screen widget
        self.screen = Text(master, state='disabled', width=30, height=3, background="yellow", foreground="blue")

        # position screen in window
        self.screen.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        self.screen.configure(state='normal')

        # initialize screen value as empty
        self.equation = ''

        # create buttons using method createButton
        b1 = self.createButton(7)
        b2 = self.createButton(8)
        b3 = self.createButton(9)
        b4 = self.createButton(u"\u232B", None)
        b5 = self.createButton(4)
        b6 = self.createButton(5)
        b7 = self.createButton(6)
        b8 = self.createButton(u"\u00F7")
        b9 = self.createButton(1)
        b10 = self.createButton(2)
        b11 = self.createButton(3)
        b12 = self.createButton('*')
        b13 = self.createButton('.')
        b14 = self.createButton(0)
        b15 = self.createButton('+')
        b16 = self.createButton('-')
        b17 = self.createButton('=', None, 34)

        # buttons stored in list
        buttons = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17]

        # intialize counter
        count = 0
        # arrange buttons with grid manager
        for row in range(1, 5):
            for column in range(4):
                buttons[count].grid(row=row, column=column)
                count += 1
        # arrange last button '=' at the bottom
        buttons[16].grid(row=5, column=0, columnspan=4)

    def createButton(self, val, write=True, width=7):
        # this function creates a button, and takes one compulsory argument, the value that should be on the button

        return Button(self.master, text=val, command=lambda: self.click(val, write), width=width)

    def click(self, text, write):
        # this function handles what happens when you click a button
        # 'write' argument if True means the value 'val' should be written on screen, if None, should not be written on screen
        if write == None:

            # only evaluate code when there is an equation to be evaluated
            if text == '=' and self.equation:
                # replace the unicode value of division ./.with python division symbol / using regex
                self.equation = re.sub(u"\u00F7", '/', self.equation)
                print(self.equation)
                answer = str(eval(self.equation))
                self.clear_screen()
                self.insert_screen(answer, newline=True)
            elif text == u"\u232B":
                self.clear_screen()


        else:
            # add text to screen
            self.insert_screen(text)

    def clear_screen(self):
        # to clear screen
        # set equation to empty before deleting screen
        self.equation = ''
        self.screen.configure(state='normal')
        self.screen.delete('1.0', END)

    def insert_screen(self, value, newline=False):
        self.screen.configure(state='normal')
        self.screen.insert(END, value)
        # record every value inserted in screen
        self.equation += str(value)
        self.screen.configure(state='disabled')


root = Tk()
my_gui = Calculator(root)
root.mainloop()
"""