# floodFill.py

#Use the left click to draw any closed shape, then right click INSIDE
#the shape to fill the shape with red colour

from pygame import *


size = width, height = 800, 600
screen = display.set_mode(size)

mx,my = 0,0


screen.fill((255,255,255))
col=255,0,0
myClock = time.Clock()
running = True
while running:
    for evnt in event.get():               
        if evnt.type == QUIT:
            running = False

    omx,omy = mx,my
    mx,my = mouse.get_pos()
    mb = mouse.get_pressed()

    if mb[0]==1:#left click
        draw.line(screen, col, (omx,omy), (mx,my))
    if mouse.get_pressed()[2]==1:#right click
        rc=screen.get_at((mx,my))
        #gets the colour of the pixel where the user right-clicked 
        
        spots = [(mx,my)] #list of points
        while len(spots)>0:
            newSpots =[]
            for fx,fy in spots:
                     #inside the 800x600    #current point is the same colour as the initial when we right-clicked
                if 0<fx<width and 0<fy<height and screen.get_at((fx,fy))==rc:
                    
                    screen.set_at((fx,fy),col)

                    #*******************************************************************************
                    display.flip()  #comment this line if you don't want to wait for the area to be filled 
                    #*****************************************************************************************
                    
                    newSpots += [(fx+1,fy),(fx-1,fy),(fx,fy-1),(fx,fy+1)]
                    #mark the 4 points for filling (right, left, up and down from the current point)
                    
                    
            spots = newSpots

        

    display.flip()
    #myClock.tick(10)                        
    
quit()
