from pygame import *
from random import randint

init()
size = width, height = 1200,600
screen = display.set_mode(size)
                        
wheel=image.load("Pictures\spectrum.jpg")
running=True
while running:
    for evnt in event.get():
        if evnt.type==QUIT:
            running=False
            
    if mouse.get_pressed()[0]==1:
        mx,my=mouse.get_pos()
        screen.blit(wheel,(mx,my))

    display.flip()

quit()
