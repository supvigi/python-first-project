# from tkinter import *
#
# okno = Tk()
# cn = Canvas(okno, width=1279, height=799, bg="gold")
# cn.pack()
# okno.title("Paint 1D B)")
#
# okno.mainloop()
#
# import keyboard
#
# keyboard.add_hotkey("g", lambda: keyboard.write("Кидаю гранату!"))
#
# keyboard.wait("Ctrl + shift + g")

import pygame

width = 1279
height = 799
flag = True

pygame.init()
pygame.display.set_caption("")
screen = pygame.display.set_mode((width, height))

while flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False

pygame.quit()
