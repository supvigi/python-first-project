# import requests
#
# response = requests.get("https://time100.ru")
# response.encoding = "utf-8"
#
# if response:
#     print("Success!")
# else:
#     print("An error has occurred")
#     exit(1)
#
# print(response.headers["Date"])
#
from time import sleep
import tkinter


def click_1():
    btn.destroy()
    lbl_2 = tkinter.Label(text="BYE!")
    lbl_2.place(x=30, y=30)


babkino_okosko = tkinter.Tk()
babkino_okosko.geometry("350x622")
babkino_okosko.title("MEME")

img = tkinter.PhotoImage(file="/Users/vlas/Desktop/meme.png")
lbl_1 = tkinter.Label(image=img)
lbl_1.place(x=1, y=1)

btn = tkinter.Button(text="NO!", command=click_1)
btn.place(x=30, y=30)

babkino_okosko.mainloop()
