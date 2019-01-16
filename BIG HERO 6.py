# otherTools.py
from pygame import *

init()
size = width, height = 800, 600
green = 0, 255, 0
red = 255, 0, 0
black=0,0,0
screen = display.set_mode(size)
cursorPic = image.load("Pictures/bubbles.png")
cw = cursorPic.get_width() #gets width of the cursor
ch = cursorPic.get_height() #gets height of the cursor

running = True
mx,my = 0,0

mouse.set_visible(False) #hiding the cursor
screenBuff = screen.copy() #screen capture
while running:
    for evnt in event.get():                
        if evnt.type == QUIT:
            running = False
        if evnt.type == MOUSEBUTTONDOWN:
            print("down")
            sx,sy = evnt.pos
            print(evnt.pos)
            #coordinates at the time the user clicks
        if evnt.type == MOUSEBUTTONUP:
            print("up")
            screen.blit(screenBuff, (0,0)) #show the screen capture
            draw.line(screen, green, (sx,sy), (mx,my)) #draw a new line
            screenBuff = screen.copy() #screen capture that includes the new line

    mx,my = mouse.get_pos()
    mb = mouse.get_pressed()

    screen.blit(screenBuff, (0,0))
    if mb[0]==1:
        draw.line(screen, green, (sx,sy), (mx,my))
        #as long as the mouse button is down, draw a line
    #if mouse.get_pressed()[2]==1:
        #screen.fill(black)

    #screen.blit(cursorPic,(mx-cw/2,my-ch/2))#centering the ship   
    
    display.update()
        

quit()
