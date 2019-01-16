#open and save

from pygame import *
from tkinter import *   

root = Tk()
root.withdraw() #hiding the tk window



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
        fname=filedialog.askopenfilename(filetypes=[("Images","*.png;*.bmp;*.jpg;*.jpeg")])
        print(fname)

    if mb[0]==1 and saveRect.collidepoint(mx,my):
        fname=filedialog.asksaveasfilename(defaultextension=".png")
        print(fname)        

if mb[0]==1 and saverect.collidepoint(mx,my) :
        fname = filedialog.asksaveasfilename(defaultextension=".png")
        image.save(screen.subsurface(canvas),fname)
    if mb[0]==1 and loadrect.collidepoint(mx,my):
        fname = filedialog.askopenfilename(filetypes=[("Images", "*.png;*.bmp;*.jpg;*.jpeg")])
        loaded=image.load(fname)
        screen.blit(loaded,(0,0))
    


    display.flip()


quit()

