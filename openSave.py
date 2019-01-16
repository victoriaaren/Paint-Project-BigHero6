'''from pygame import *
from tkinter import *   

root = Tk()
root.withdraw() #hiding little annoying window

screen = display.set_mode((800,600))
openRect = Rect(20,80,40,40)
saveRect = Rect(65,80,40,40)

running =True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False


    mb = mouse.get_pressed()
    mx,my = mouse.get_pos()
    draw.rect(screen,(0,255,0),openRect,2)
    draw.rect(screen,(0,255,0),saveRect,2)

    if mb[0]==1 and openRect.collidepoint(mx,my):
        fname=filedialog.askopenfilename(filetypes=[("Images","*.png;*.jpg;*.bmp;*.jpeg")]) #THE FUNCTION THAT OPENS


    if mb[0]==1 and saveRect.collidepoint(mx,my):
        fname=filedialog.asksaveasfilename() #THE FUNCTION THAT SAVES

    display.flip()


quit()'''
from pygame import *
    
screen = display.set_mode((1200,675))

canvasRect = Rect(100,50,900,575)
running =True
screen.fill((255,255,255))
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type == MOUSEBUTTONDOWN:
            if e.button == 3:
                image.save(screen.subsurface(canvasRect),"test pic/jan8.png")
    
    mb = mouse.get_pressed()
    mx,my = mouse.get_pos()

    draw.rect(screen,(0,0,0), canvasRect,2)
    if mb[0]==1:
        draw.circle(screen, (0,0,0), (mx,my), 3)

    display.flip()

quit()
