#stamps lets go
# move.py
from pygame import *

init()
size = width, height = 1300,700
green = 0, 255, 0
red = 255, 0, 0
screen = display.set_mode(size)
mmode = "up" #mouse mode (clicked or released)
baymax=image.load("Pictures/Baymax.png")
baymax=Rect(baymax)
baymax=transform.smoothscale(baymax,(100,100))
screen.blit(baymax,(0,0))

running = True

while running:
    for evnt in event.get():              
        if evnt.type == QUIT:
            running = False
    mx,my=mouse.get_pos()       
    if mmode == "up" and mouse.get_pressed()[0]==1:#mouse is not clicked,then clicked
        screenShot = screen.copy() #screen capture,  like a screenshot
        mmode = "down" #mouse mode becomes down, like the mouse is pressed down
        #print("screen capture") #screenshot
    if mmode == "down" and mouse.get_pressed()[0]==0: #if mouse is released while it's down
        mmode = "up" #back up bro, no more screen shots
        #print("mouse up")
    if baymax.collidepoint(mx,my) and mouse.get_pressed()[0]==1:
        
    
    
        if mmode == "down":
            screen.blit(screenShot, (0,0)) #dont really get the 0,0 but whateves
            
            
            screen.blit(baymax,(mx,my))
        
    
    display.flip()               
    
quit()
