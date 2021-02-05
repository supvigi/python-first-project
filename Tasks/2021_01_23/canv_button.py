from tkinter import *


def click_l(event):
    global clicked
    if 175 <= event.x <= 525 and 175 <= event.y <= 525:
        if clicked is False:
            clicked = True
            cn.create_rectangle(175, 175, 525, 525, fill="green", outline="black")
            cn.create_text(350, 350, text="THANK YOU!", font=90, fill="black")
        else:
            clicked = False
            cn.create_rectangle(175, 175, 525, 525, fill="red", outline="black")
            cn.create_text(350, 350, text="PRESS ME!", font=90, fill="black")


def move(event):
    global clicked
    if clicked is False:
        if 175 <= event.x <= 525 and 175 <= event.y <= 525:
            cn.create_rectangle(175, 175, 525, 525, fill="red", outline="black")
            cn.create_text(350, 350, text="PRESS ME!", font=90, fill="black")
        else:
            cn.create_rectangle(175, 175, 525, 525, fill="gold", outline="black")
            cn.create_text(350, 350, text="PRESS ME!", font=90, fill="black")


okno = Tk()
okno.title("canvas button")
okno.geometry("700x700")
clicked = False

cn = Canvas(okno, width=700, height=700, bg="white")
cn.pack()

cn.create_rectangle(175, 175, 525, 525, fill="gold", outline="black")
cn.create_text(350, 350, text="PRESS ME!", font=90, fill="black")
okno.bind("<Motion>", move)
okno.bind("<Button-1>", click_l)

okno.mainloop()
