from pygame import *
from random import randint

init()
size = width, height = 800,600
screen = display.set_mode(size)
mmode="up"                     
green=0,255,0
ox=oy=300
running=True
tool="pen"
a=image.load("Pictures/baymax/1.png")
b=image.load("Pictures/baymax/2.png")

meep=Rect(0,0,40,40)
merp=Rect(50,0,40,40)
while running:
    clicked=False
    for evnt in event.get():
        if evnt.type == QUIT:
            running = False
        if evnt.type==MOUSEBUTTONDOWN:
            clicked=True
            sx,sy=evnt.pos #coordinate of where the mouse is clicked
            screenshot=screen.copy()
            #undoScreen=screen.subsurface(canvasRect).copy()
            #undo.append.screen.subsurface(undoScreen)
            if evnt.button==4: #scrolling up
                if SIZE<5: #max size 5
                    SIZE+=1
            elif evnt.button==5: #scrolling down
                if SIZE>1: #min size 1
                    SIZE-=1

    screen.blit(a,(0,0))
    time.wait(5000)
    screen.blit(b,(0,0))
    time.wait(5000)

    
   
    ox=mx
    oy=my
    display.flip()

quit()
