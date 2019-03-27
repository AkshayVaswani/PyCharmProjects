from tkinter import *

calc = Tk()
counter = 0

calc.geometry("375x570")
calc.title("Calculator")


equation = StringVar()


e = Entry(calc, textvariable=equation, state='disabled', width=375, font="Helvetica 44 bold",justify="center", bg="#1E6FBA",fg="yellow",disabledbackground="#1E6FBA",disabledforeground="yellow",highlightbackground="black",highlightcolor="red",highlightthickness=1, bd=0)
e.configure(disabledbackground="white", disabledforeground="black")
#e.grid(columnspan=4, ipadx=70)


def callbackPlus():
    global counter
    counter = counter + 1
    equation.set("Count: " + str(counter))


def callbackMinus():
    global counter
    counter = counter - 1
    equation.set("Count: " + str(counter))


btns = [
    (lambda ctl: ctl.grid(row=r, column=c) or ctl)(
        Button(text=str(1 + r * 3 + c)))
    for c in (0, 1, 2) for r in (0, 1, 2)]


B = Button(calc, text="+", command=callbackPlus)
B.grid(row=3, column=0)
minus = Button(calc, text="-", command=callbackMinus)
minus.grid(row=1, column=1)

e = equation.get()
calc.mainloop()