from pygame import *


init()
size = width, height = 800, 600
screen = display.set_mode(size)

green = 0, 255, 0   
red = 255, 0, 0
black=0,0,0
white=255,255,255
baymax=image.load("Paint Project/Pictures/Baymax.png")


running = True

while running:
    for evnt in event.get():
        if evnt.type == QUIT:
            running = False
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()

    if mouse.get_pressed()[0]==1:
                                  #to make it centred move by half the length.width
        screen.blit(baymax,(mx,my))

    

    display.flip()

quit()
