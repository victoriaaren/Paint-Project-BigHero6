from pygame import *
    
screen = display.set_mode((1024,768))
init()                                  # need init to initialize the mixer
mixer.music.load("immortals.mp3")       # load a MUSIC object
mixer.music.play()

running =True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
    
    mb = mouse.get_pressed()
    mx,my = mouse.get_pos()

    if mb[0]==1:
        draw.circle(screen, (255,255,0), (mx,my), 3)

    display.flip()

quit()
