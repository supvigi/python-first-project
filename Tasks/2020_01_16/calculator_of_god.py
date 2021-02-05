import tkinter


def submit():
    global num1, num2
    a = stroka.cget("text")
    if a != 0:
        if num1 == 0:
            num1 = a
            stroka.configure(text="0")
        elif num1 != 0:
            num2 = a


def equals(x):
    global num1, num2, result
    if x == 1:
        result = int(num1) + int(num2)
    elif x == 2:
        result = int(num1) - int(num2)
    elif x == 3:
        result = int(num1) * int(num2)
    elif x == 4:
        result = int(num1) / int(num2)
    stroka.configure(text=result)


def erase():
    stroka.configure(text="0")


def digits(x):
    a = stroka.cget("text")
    if a == "0":
        stroka.configure(text=x)
    else:
        stroka.configure(text=a + x)


okno_boga = tkinter.Tk()
okno_boga.geometry("152x290")
okno_boga.title("Calculator")
num1 = 0
num2 = 0
result = 0

stroka = tkinter.Label(text="0", font=("arial", 20))
stroka.place(x=0, y=5)

plus = tkinter.Button(text="+", width=2, height=2, command=lambda: equals(1))
plus.place(x=0, y=44)

minus = tkinter.Button(text="-", width=2, height=2, command=lambda: equals(2))
minus.place(x=22, y=44)

multiply = tkinter.Button(text="x", width=2, height=2, command=lambda: equals(3))
multiply.place(x=44, y=44)

divide = tkinter.Button(text="/", width=2, height=2, command=lambda: equals(4))
divide.place(x=66, y=44)

plus_or_minus = tkinter.Button(text="+/-", width=2, height=2)
plus_or_minus.place(x=88, y=44)

equals = tkinter.Button(text="=", width=2, height=2, command=equals)
equals.place(x=110, y=44)

zero = tkinter.Button(text="0", width=5, height=3, command=lambda: digits("0"))
zero.place(x=2, y=236)

one = tkinter.Button(text="1", width=5, height=3, command=lambda: digits("1"))
one.place(x=2, y=184)

two = tkinter.Button(text="2", width=5, height=3, command=lambda: digits("2"))
two.place(x=52, y=184)

three = tkinter.Button(text="3", width=5, height=3, command=lambda: digits("3"))
three.place(x=102, y=184)

four = tkinter.Button(text="4", width=5, height=3, command=lambda: digits("4"))
four.place(x=2, y=132)

five = tkinter.Button(text="5", width=5, height=3, command=lambda: digits("5"))
five.place(x=52, y=132)

six = tkinter.Button(text="6", width=5, height=3, command=lambda: digits("6"))
six.place(x=102, y=132)

seven = tkinter.Button(text="7", width=5, height=3, command=lambda: digits("7"))
seven.place(x=2, y=80)

eight = tkinter.Button(text="8", width=5, height=3, command=lambda: digits("8"))
eight.place(x=52, y=80)

nine = tkinter.Button(text="9", width=5, height=3, command=lambda: digits("9"))
nine.place(x=102, y=80)
dot = tkinter.Button(text="Submit", width=5, height=3)
dot.place(x=52, y=236)
erase = tkinter.Button(text="AC", width=5, height=3, command=erase)
erase.place(x=102, y=236)

okno_boga.mainloop()
