
#Victoria Ren Paint Project
#Big Hero 6 Paint
#-------------------------------------------------------------------------------------------------------

#import everything first
from pygame import *
from math import *
from random import *
from tkinter import *

############################################# set up

size = width, height = 1200,690
screen = display.set_mode(size)
display.set_caption("BIG HERO 6 PAINT - CREATED BY VICTORIA REN") #caption for window
init() #initialize 
SIZE=15 #for scroll button and allows user to change size of marker/spray paint

back="none" #variable for background
myClock = time.Clock() #for flood fill later on in the code

############################################for save and open

root = Tk()
root.withdraw() #hiding the tk window

#############################################Loading page

x=0
label=image.load("Pictures/text/bighero6.png")
label=transform.smoothscale(label,(690,276))
for i in range(1,120):
    time.wait(8)
    draw.rect(screen,(200,25,32),(x,138,50,276))
    x+=10
    display.flip()

screen.blit(label,(270,138))
display.flip()
time.wait(60)

#---------------------------------------------------------
white=255,255,255
black=0,0,0
green=0,255,0 #neccessary colours
ox=oy=300     #setting the variable of ox,oy
tool="pencil" #default tool
col=black     #default colour

#####################################music
mixer.music.load("immortals.mp3")
mixer.music.play()
#####################################

running = True
mx,my=0,0
smode="stamp" #selcect mode (select or stamp mode for select tool
mmode = "up" #mouse mode (clicked or released) (for stamps later on)

##################################################### all pictures needed for code
#stamps pictures

baymax=image.load("Pictures/Baymax.png")
gogo=image.load("Pictures/gogo.png")
lemon=image.load("Pictures/lemon.png")
dragon=image.load("Pictures/dragonguy.png")
hiro=image.load("Pictures/hiro.png")
superBaymax=image.load("Pictures/superbaymax.png")
superBaymaxPic=image.load("Pictures/superbaymax2.png")
wasabi=image.load("Pictures/wasabi.png")

###----------------------------------------second stamp for actual stamp

baymax2=image.load("Pictures/Baymax2.png")
gogo2=image.load("Pictures/gogo2.png")
lemon2=image.load("Pictures/lemon2.png")
dragon2=image.load("Pictures/dragonguy2.png")
hiro2=image.load("Pictures/hiro2.png")
superBaymax=image.load("Pictures/superbaymax.png")
superBaymaxPic=image.load("Pictures/superbaymax2.png")
wasabi2=image.load("Pictures/wasabi2.png")
background=image.load("Pictures/background.png")
bubbleTool=image.load("Pictures/bubble.png")
frame=image.load("Pictures/frame.png")
title=image.load("Pictures/title.png")

####################-----------icon pictures/tools

eraserIcon=image.load("Pictures/erasericon.png")
pencilIcon=image.load("Pictures/pencilicon.png")
markerIcon=image.load("Pictures/markericon.png")
sprayIcon=image.load("Pictures/sprayIcon.png")
fillIcon=image.load("Pictures/fillicon.png")
spectrum=image.load("Pictures/spectrumpaint.png")
filledRectIcon=image.load("Pictures/rectanglefilled.png")
filledCircleIcon=image.load("Pictures/filledcircle.png")
rectIcon=image.load("Pictures/rectangle.png")
circleIcon=image.load("Pictures/circle.png")
bubblesIcon=image.load("Pictures/bubbles.png")
limitFillIcon=image.load("Pictures/fill.png")
lineIcon=image.load("Pictures/lineIcon.png")
musicOn=image.load("Pictures/musicon.png")
musicOff=image.load("Pictures/musicoff.png")
undo=image.load("Pictures/undo.png")
redo=image.load("Pictures/redo.png")
selectIcon=image.load("Pictures/select.png")
newIcon=image.load("Pictures/new.png")
openIcon=image.load("Pictures/open.png")
saveIcon=image.load("Pictures/save.png")
backgroundIcon=image.load("Pictures/picture.png")
scene1=image.load("Pictures/scene1.png")
scene1Copy=image.load("Pictures/scene12.png")
scene2=image.load("Pictures/scene2.png")
scene2Copy=image.load("Pictures/scene22.png")
scene3=image.load("Pictures/scene3.png")
scene3Copy=image.load("Pictures/scene32.png")

############################################display for tool and saying what it does, loading the images first

pencilSign=image.load("Pictures/text/pencil.png")
eraserSign=image.load("Pictures/text/eraser.png")
sign=image.load("Pictures/text/paper.png")
spraySign=image.load("Pictures/text/spray.png")
filledRectSign=image.load("Pictures/text/filledrect.png")
backgroundSign=image.load("Pictures/text/background.png")
bubbleSign=image.load("Pictures/text/bubble.png")
fillSign=image.load("Pictures/text/fill.png")
filledCircleSign=image.load("Pictures/text/filledcircle.png")
lineSign=image.load("Pictures/text/line.png")
markerSign=image.load("Pictures/text/marker.png")
selectSign=image.load("Pictures/text/select.png")
circleSign=image.load("Pictures/text/unfilledcircle.png")
rectSign=image.load("Pictures/text/unfilledrect.png")
limitFillSign=image.load("Pictures/text/limitfill.png")
undoSign=image.load("Pictures/text/undo.png")
redoSign=image.load("Pictures/text/redo.png")
openSign=image.load("Pictures/text/open.png")
saveSign=image.load("Pictures/text/save.png")
stampSign=image.load("Pictures/text/stamp.png")
newSign=image.load("Pictures/text/new.png")

############################################foundation for all icons, setting the rect positions

pencilRect=Rect(180,595,40,40)
eraserRect=Rect(180,645,40,40)
sprayRect=Rect(230,595,40,40)
fillRect=Rect(230,645,40,40)
markerRect=Rect(280,595,40,40)
rectRect=Rect(280,645,40,40)
circleRect=Rect(330,595,40,40)
limitFillRect=Rect(330,645,40,40)
filledRectRect=Rect(380,595,40,40)
filledCircleRect=Rect(380,645,40,40)
lineRect=Rect(430,595,40,40)
selectRect=Rect(430,645,40,40)
bubblesRect=Rect(135,262,40,40)
newRect=Rect(113,588,40,40)
openRect=Rect(86,313,40,40)
saveRect=Rect(136,313,40,40)

canvasRect=Rect(190,60,900,520)
screenRect=Rect(0,0,1200,690) #for all tools that are not meant just for the canvas

spectrumRect=Rect(485,595,500,90)

colourDisplayRect=Rect(990,595,110,90)
actualColourDisplay=Rect(1000,610,90,50)

musicOnRect=Rect(10,640,40,40)
musicOffRect=Rect(50,640,40,40)

undoRect=Rect(90,640,40,40)
redoRect=Rect(130,640,40,40)

backgroundRect=Rect(85,262,40,40)
backSelectRect=Rect(1,518,175,116)

scene1Rect=Rect(42,522,92,62)
scene2Rect=Rect(3,587,82,42)
scene3Rect=Rect(90,587,82,42)

##########################stamps

baymaxStamp=Rect(1105,60,86,86)
gogoStamp=Rect(1105,146,86,86)
lemonStamp=Rect(1105,232,86,86)
dragonStamp=Rect(1105,318,86,86)
hiroStamp=Rect(1105,404,86,86)
wasabiStamp=Rect(1105,490,86,86)
superBaymaxStamp=Rect(1105,576,86,110)

####################################################resize images

background=transform.smoothscale(background,(width,height))
screen.blit(background,(0,0))#must blit background first

frame=transform.smoothscale(frame,(920,540))
screen.blit(frame,(180,50))

title=transform.smoothscale(title,(575,63))
screen.blit(title,(0,0))

draw.rect(screen,white,canvasRect) #before the loop so you can draw on top of it

####################################################resizing images

baymax=transform.smoothscale(baymax,(86,86))
gogo=transform.smoothscale(gogo,(86,86))
lemon=transform.smoothscale(lemon,(86,86))
dragon=transform.smoothscale(dragon,(86,86))
hiro=transform.smoothscale(hiro,(86,86))
wasabi=transform.smoothscale(wasabi,(86,86))
superBaymaxPic=transform.smoothscale(superBaymaxPic,(86,110))

superBaymax=transform.smoothscale(superBaymax,(300,300))
baymax2=transform.smoothscale(baymax2,(150,150))
gogo2=transform.smoothscale(gogo2,(150,150))
lemon2=transform.smoothscale(lemon2,(175,175))
dragon2=transform.smoothscale(dragon2,(150,150))
hiro2=transform.smoothscale(hiro2,(125,125))
wasabi2=transform.smoothscale(wasabi2,(200,200))

spectrum=transform.smoothscale(spectrum,(500,90))

#####################################################icons

pencilIcon=transform.smoothscale(pencilIcon,(40,40))
eraserIcon=transform.smoothscale(eraserIcon,(40,40))
markerIcon=transform.smoothscale(markerIcon,(40,40))
sprayIcon=transform.smoothscale(sprayIcon,(40,40))
fillIcon=transform.smoothscale(fillIcon,(40,40))
filledRectIcon=transform.smoothscale(filledRectIcon,(40,40))
filledCircleIcon=transform.smoothscale(filledCircleIcon,(40,40))
rectIcon=transform.smoothscale(rectIcon,(40,40))
circleIcon=transform.smoothscale(circleIcon,(40,40))
bubblesIcon=transform.smoothscale(bubblesIcon,(40,40))
limitFillIcon=transform.smoothscale(limitFillIcon,(40,40))
lineIcon=transform.smoothscale(lineIcon,(40,40))
selectIcon=transform.smoothscale(selectIcon,(40,40))
newIcon=transform.smoothscale(newIcon,(40,40))
openIcon=transform.smoothscale(openIcon,(40,40))
saveIcon=transform.smoothscale(saveIcon,(40,40))
backgroundIcon=transform.smoothscale(backgroundIcon,(40,40))

musicOn=transform.smoothscale(musicOn,(40,37))
musicOff=transform.smoothscale(musicOff,(41,40))

undo=transform.smoothscale(undo,(40,40))
redo=transform.smoothscale(redo,(40,40))

scene1Copy=transform.smoothscale(scene1Copy,(92,62)) #####all of this is for background feature
scene2Copy=transform.smoothscale(scene2Copy,(82,42))
scene3Copy=transform.smoothscale(scene3Copy,(82,42))

scene1=transform.smoothscale(scene1,(900,520))
scene2=transform.smoothscale(scene2,(900,520))
scene3=transform.smoothscale(scene3,(900,520))

########################################################resize display signs

pencilSign=transform.smoothscale(pencilSign,(300,43))
eraserSign=transform.smoothscale(eraserSign,(300,43))
sign=transform.smoothscale(sign,(300,43))
spraySign=transform.smoothscale(spraySign,(300,43))
filledRectSign=transform.smoothscale(filledRectSign,(300,43))
backgroundSign=transform.smoothscale(backgroundSign,(300,43))
bubbleSign=transform.smoothscale(bubbleSign,(300,43))
fillSign=transform.smoothscale(fillSign,(300,43))
filledCircleSign=transform.smoothscale(filledCircleSign,(300,43))
lineSign=transform.smoothscale(lineSign,(300,43))
markerSign=transform.smoothscale(markerSign,(300,43))
selectSign=transform.smoothscale(selectSign,(300,43))
circleSign=transform.smoothscale(circleSign,(300,43))
rectSign=transform.smoothscale(rectSign,(300,43))
limitFillSign=transform.smoothscale(limitFillSign,(300,43))
undoSign=transform.smoothscale(undoSign,(300,43))
redoSign=transform.smoothscale(redoSign,(300,43))
openSign=transform.smoothscale(openSign,(300,43))
saveSign=transform.smoothscale(saveSign,(300,43))
stampSign=transform.smoothscale(stampSign,(300,43))
newSign=transform.smoothscale(newSign,(300,43))

########################################################blitting images

screen.blit(baymax,(1105,60))
screen.blit(gogo,(1105,146))
screen.blit(lemon,(1105,232))
screen.blit(dragon,(1105,318))
screen.blit(hiro,(1105,404))
screen.blit(wasabi,(1105,490))
screen.blit(superBaymaxPic,superBaymaxStamp)

#####################blitting icons

screen.blit(pencilIcon,pencilRect)
screen.blit(eraserIcon,eraserRect)
screen.blit(markerIcon,markerRect)
screen.blit(sprayIcon,sprayRect)
screen.blit(fillIcon,fillRect)
screen.blit(spectrum,spectrumRect)
screen.blit(filledRectIcon,filledRectRect)
screen.blit(filledCircleIcon,filledCircleRect)
screen.blit(circleIcon,circleRect)
screen.blit(rectIcon,rectRect)
screen.blit(bubblesIcon,bubblesRect)
screen.blit(limitFillIcon,limitFillRect)
screen.blit(lineIcon,lineRect)
screen.blit(musicOn,musicOnRect)
screen.blit(musicOff,musicOffRect)
screen.blit(undo,undoRect)
screen.blit(redo,redoRect)
screen.blit(selectIcon,selectRect)
screen.blit(openIcon,openRect)
screen.blit(saveIcon,saveRect)
screen.blit(newIcon,newRect)
screen.blit(backgroundIcon,backgroundRect)

######################################################let's begin

screenShot = screen.subsurface(canvasRect).copy() #take a picture before everything begins, as a blank canvas

takePicture=screen.subsurface(canvasRect).copy() #screen shot/capture

rec=Rect(1,1,1,1) #defining rect used later on in select tool
miniscreen=screen.subsurface(rec).copy() #defining subsurface used later on in select tool

#-------------------------------------------------------

redo=[] #redo list
undo=[screenShot] #undo list, first add the blank screenshot of the canvas

#-------------------------------------------------------

blitting=False
forming= True #for select tool

#-------------------------------------------------------

while running:
    
    clicked=False
    clickUp=False
    
    for evnt in event.get():
        if evnt.type == QUIT:
            running = False
        
        if evnt.type==MOUSEBUTTONDOWN:
            screenShot = screen.subsurface(canvasRect).copy() #screenshot, making it a subsurface
            
            clicked=True
            sx,sy=evnt.pos #coordinate of where the mouse is clicked
            takePicture=screen.subsurface(canvasRect).copy()

        if evnt.type==MOUSEBUTTONUP: #for select, if the mouse is up then "click up"
            clickUp = True
            clicked=False
            if canvasRect.collidepoint(mx,my) and mb[0]==1:
                undo1=screen.subsurface(canvasRect).copy() #take another screenshot
                undo.append(undo1) #append
       
            if evnt.button==4: #scrolling up
                if SIZE<50: #max size 50
                    SIZE+=1
            elif evnt.button==5: #scrolling down
                if SIZE>15: #min size 15
                    SIZE-=1
                    
    if mmode == "up" and mouse.get_pressed()[0]==1:#mouse is not clicked,then clicked
        screenShot = screen.subsurface(canvasRect).copy() #screen capture,  like a screenshot
        mmode = "down" #mouse mode becomes down, like the mouse is pressed down
    if mmode == "down" and mouse.get_pressed()[0]==0: #if mouse is released while it's down
        mmode = "up" #no more screen shots
        
########################################################
        
    if smode == "stamp" and mouse.get_pressed()[0]==1:#mouse is not clicked,then clicked
        smode = "select" #mouse mode becomes down, like the mouse is pressed down
    if smode == "select" and mouse.get_pressed()[0]==0: #if mouse is released while it's down
        smode = "stamp" 

    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
    
#####################################################drawing all the icon rectangles
    
    draw.rect(screen,black,pencilRect,2)
    draw.rect(screen,black,eraserRect,2)
    draw.rect(screen,black,sprayRect,2)
    draw.rect(screen,black,fillRect,2)
    draw.rect(screen,black,markerRect,2)
    draw.rect(screen,black,rectRect,2)
    draw.rect(screen,black,circleRect,2)
    draw.rect(screen,black,limitFillRect,2)
    draw.rect(screen,black,filledRectRect,2)
    draw.rect(screen,black,filledCircleRect,2)
    draw.rect(screen,black,spectrumRect,3)
    draw.rect(screen,black,lineRect,2)
    draw.rect(screen,black,bubblesRect,2)
    draw.rect(screen,white,colourDisplayRect)
    draw.rect(screen,col,actualColourDisplay)
    draw.rect(screen,black,superBaymaxStamp,2)
    draw.rect(screen,black,backgroundRect,2)
    draw.rect(screen,black,selectRect,2)
    draw.rect(screen,black,newRect,2)
    draw.rect(screen,black,undoRect,2)
    draw.rect(screen,black,redoRect,2)
    draw.rect(screen,black,openRect,2)
    draw.rect(screen,black,saveRect,2)

    draw.rect(screen,black,baymaxStamp,2)
    draw.rect(screen,black,gogoStamp,2)
    draw.rect(screen,black,lemonStamp,2)
    draw.rect(screen,black,hiroStamp,2)
    draw.rect(screen,black,dragonStamp,2)
    draw.rect(screen,black,wasabiStamp,2)
    draw.rect(screen,black,superBaymaxStamp,2)

##############################################################
    
  #display tool selection display
    if pencilRect.collidepoint(mx,my) and mb[0]==1: #if you collide with pencil rect
        tool="pencil" #tool is pencil
    if tool=="pencil": #if tool is pencil
        draw.rect(screen,green,pencilRect,2) #to highlight and show selected tool draw a different coloured rect on top
        screen.blit(pencilSign,(772,7)) #blit the sign saying what the tool does
        
    if eraserRect.collidepoint (mx,my) and mb[0]==1: #same for all tools
        tool="eraser"
    if tool=="eraser":
        draw.rect(screen,green,eraserRect,2)
        screen.blit(eraserSign,(772,7))
        
    if sprayRect.collidepoint(mx,my) and mb[0]==1:
        tool="spray paint"
    if tool=="spray paint":
        draw.rect(screen,green,sprayRect,2)
        screen.blit(spraySign,(772,7))
        
    if fillRect.collidepoint(mx,my) and mb[0]==1:
        tool="fill screen"
    if tool=="fill screen":
        draw.rect(screen,green,fillRect,2)
        screen.blit(fillSign,(772,7))
        
    if markerRect.collidepoint(mx,my) and mb[0]==1:
        tool="marker"
    if tool=="marker":
        draw.rect(screen,green,markerRect,2)
        screen.blit(markerSign,(772,7))
        
    if rectRect.collidepoint(mx,my) and mb[0]==1:
        tool="draw unfilled rectangle"
    if tool=="draw unfilled rectangle":
        draw.rect(screen,green,rectRect,2)
        screen.blit(rectSign,(772,7))
        
    if circleRect.collidepoint(mx,my) and mb[0]==1:
        tool="draw unfilled circle"
    if tool=="draw unfilled circle":
        draw.rect(screen,green,circleRect,2)
        screen.blit(circleSign,(772,7))
        
    if limitFillRect.collidepoint(mx,my) and mb[0]==1:
        tool="limit fill"
    if tool=="limit fill":
        draw.rect(screen,green,limitFillRect,2)
        screen.blit(limitFillSign,(772,7))
        
    if filledRectRect.collidepoint(mx,my) and mb[0]==1:
        tool="filled rectangle"
    if tool=="filled rectangle":
        draw.rect(screen,green,filledRectRect,2)
        screen.blit(filledRectSign,(772,7))
        
    if filledCircleRect.collidepoint(mx,my) and mb[0]==1:
        tool="filled circle"
    if tool=="filled circle":
        draw.rect(screen,green,filledCircleRect,2)
        screen.blit(filledCircleSign,(772,7))
        
    if lineRect.collidepoint(mx,my) and mb[0]==1:
        tool="draw line"
    if tool=="draw line":
        draw.rect(screen,green,lineRect,2)
        screen.blit(lineSign,(772,7))
        
    if bubblesRect.collidepoint(mx,my) and mb[0]==1:
        tool="draw bubbles"
    if tool=="draw bubbles":
        draw.rect(screen,green,bubblesRect,2)
        screen.blit(bubbleSign,(772,7))
        
    if backgroundRect.collidepoint(mx,my) and mb[0]==1:
        tool="choose a background"
        draw.rect(screen,white,backSelectRect) 
    if tool=="choose a background":
        screen.blit(backgroundSign,(772,7))
        #if tool is background then we draw the options rectangles and blit the icons
        draw.rect(screen,green,backgroundRect,2)
        draw.rect(screen,black,scene1Rect,2)
        draw.rect(screen,black,scene2Rect,2)
        draw.rect(screen,black,scene3Rect,2)
        
        screen.blit(scene1Copy,scene1Rect)
        screen.blit(scene2Copy,scene2Rect)
        screen.blit(scene3Copy,scene3Rect)
    
        if scene1Rect.collidepoint(mx,my) and mb[0]==1:
            back="scene 1" #must use different variable other than tool or it will not work since tool is already "choose a background"
        if back=="scene 1":
            draw.rect(screen,green,scene1Rect,2)
            screen.blit(scene1,(190,60))
            
        if scene2Rect.collidepoint(mx,my) and mb[0]==1:
            back="scene 2"
        if back=="scene 2":
            draw.rect(screen,green,scene2Rect,2)
            screen.blit(scene2,(190,60))
            
        if scene3Rect.collidepoint(mx,my) and mb[0]==1:
            back="scene 3"
        if back=="scene 3":
            draw.rect(screen,green,scene3Rect,2)
            screen.blit(scene3,(190,60))

    if newRect.collidepoint(mx,my) and mb[0]==1:
        tool="new canvas"
    if tool=="new canvas":
        draw.rect(screen,green,newRect,2)
        screen.blit(newSign,(772,7))
        
    if selectRect.collidepoint(mx,my) and mb[0]==1:
        tool="select"
    if tool=="select":
        draw.rect(screen,green,selectRect,2)
        screen.blit(selectSign,(772,7))

    if saveRect.collidepoint(mx,my) and mb[0]==1:
        tool="save"
    if tool=="save":
        draw.rect(screen,green,saveRect,2)
        screen.blit(saveSign,(772,7))

    if openRect.collidepoint(mx,my) and mb[0]==1:
        tool="open"
    if tool=="open":
        draw.rect(screen,green,openRect,2)
        screen.blit(openSign,(772,7))

    if undoRect.collidepoint(mx,my) and mb[0]==1:
        tool="undo"
    if tool=="undo":
        draw.rect(screen,green,undoRect,2)
        screen.blit(undoSign,(772,7))

    if redoRect.collidepoint(mx,my) and mb[0]==1:
        tool="redo"
    if tool=="redo":
        draw.rect(screen,green,redoRect,2)
        screen.blit(redoSign,(772,7))
        
##################################################################stamps
        
    if baymaxStamp.collidepoint(mx,my) and mb[0]==1:
        tool="baymax stamp"
    if tool=="baymax stamp":
        draw.rect(screen,green,baymaxStamp,2)
        screen.blit(stampSign,(772,7))
        
    if gogoStamp.collidepoint(mx,my) and mb[0]==1:
        tool="gogo stamp"
    if tool=="gogo stamp":
        draw.rect(screen,green,gogoStamp,2)
        screen.blit(stampSign,(772,7))
        
    if lemonStamp.collidepoint(mx,my) and mb[0]==1:
        tool="lemon stamp"
    if tool=="lemon stamp":
        draw.rect(screen,green,lemonStamp,2)
        screen.blit(stampSign,(772,7))
        
    if dragonStamp.collidepoint(mx,my) and mb[0]==1:
        tool="dragon stamp"
    if tool=="dragon stamp":
        draw.rect(screen,green,dragonStamp,2)
        screen.blit(stampSign,(772,7))
        
    if hiroStamp.collidepoint(mx,my) and mb[0]==1:
        tool="hiro stamp"
    if tool=="hiro stamp":
        draw.rect(screen,green,hiroStamp,2)
        screen.blit(stampSign,(772,7))
        
    if wasabiStamp.collidepoint(mx,my) and mb[0]==1:
        tool="wasabi stamp"
    if tool=="wasabi stamp":
        draw.rect(screen,green,wasabiStamp,2)
        screen.blit(stampSign,(772,7))
        
    if superBaymaxStamp.collidepoint(mx,my) and mb[0]==1:
        tool="super baymax stamp"
    if tool=="super baymax stamp":
        draw.rect(screen,green,superBaymaxStamp,2)
        screen.blit(stampSign,(772,7))
        
#################################################################for music
        
    if musicOffRect.collidepoint(mx,my) and mb[0]==1:
        mixer.music.pause() #pause the music
    if musicOnRect.collidepoint(mx,my) and mb[0]==1:
        mixer.music.unpause() #unpause the music
        
#################################################################the tools
    if tool=="select" and clickUp and canvasRect.collidepoint(mx,my) and canvasRect.collidepoint(sx,sy): #clickUp cannot be in while loop so
            #it is outside, canvasRect.collidepoint must be mx,my AND sx,sy because you can only select what is on the screen
            
        dx=mx-sx #dimensions from before
        dy=my-sy
        
        if dx==0:
            dx=1 #just in case dx is 0 set it to one
        if dy==0:
            dy==1 #same as above
            
        rec=Rect(sx,sy,dx,dy) #restating the rect
        rec.normalize() #in case the rect dimensions include negative integers which can cause errors
        screen.blit(screenShot,canvasRect)
        if forming:
            miniscreen=screen.subsurface(rec).copy() #make the rec into a subsurface
            forming=False
            blitting = True
        elif blitting:
            forming = True
            blitting = False
            screen.blit(miniscreen,(mx,my)) #blit the subsurface at mx,my   

#-----------------------------------------------------------------------------------------------
        
    if canvasRect.collidepoint(mx,my) and mb[0]==1:
        screen.set_clip(canvasRect) #can only modify the canvas that is IT
        
        if tool=="pencil": #from before, only if you click the box it would work
            draw.line(screen,col,(ox,oy),(mx,my),2) #draw a line from oldx,oldy to mx,my

#-----------------------------------------------------------------------------------------------
            
        if tool=="spray paint":
            for i in range(30): #draw 30 circles within a circled area
                size = SIZE #the spray paint will go SIZE pixels tops away from mx,my
                sprayPaintx = randint(mx-size*2,mx+size*2) #randint from mx-diameter to mx+diameter
                sprayPainty = randint(my-size*2,my+size*2) #same as above only using my
                if hypot(mx-sprayPaintx,my-sprayPainty)<=size*2: #the hypotenuse must be contained within the diameter, it cannot go past it
                    draw.circle(screen,col,(sprayPaintx,sprayPainty),1,1) #draw small circles within a circled area

#-----------------------------------------------------------------------------------------------
                    
        if tool=="fill screen":
            draw.rect(screen,col,canvasRect) #fill screen with whatever colour you choose

#-----------------------------------------------------------------------------------------------
            
        if tool=="marker":
            tx=mx-ox #trianglex distance
            ty=my-oy #triangley distance
            dist=hypot(tx,ty) #hypotenuse
           
            dist=max(1,dist) #if dist is smaller than one then, dist becomes one
            sx=(tx/dist) #x coordinate of the small triangle formed with dimensions 1x1, found by similar triangle theorem
            sy=(ty/dist) #y coordinate
          
            for i in range(int(dist)): #for every pixel between ox and mx
                
                draw.circle(screen,col,(ox+int(sx*i),oy+int(sy*i)),SIZE) #draw a circle, it is ox+(sx*i) so that sx is being multiplied otherwise it would just keep drawing the circle in one place

#-----------------------------------------------------------------------------------------------
                
        if tool=="draw unfilled circle":
            screen.blit(screenShot,canvasRect) #blit the screenshot from memory so the circle does not continuously draw
            dx=mx-sx #dimensions of the right triangle formed when connecting points ox,oy&mx,my
            dy=my-sy
            if abs(dx)>3 and abs(dy)>3: #must be absolute value in case of negative values which would crash the program
               ellRect=Rect(min(mx,sx),min(my,sy),abs(dx),abs(dy))  #min between mx and sx
               draw.ellipse(screen,col,ellRect,2) #draw the ellipse which is technically inside an invisible rect

#-----------------------------------------------------------------------------------------------
                
        if tool=="filled circle":
            screen.blit(screenShot,canvasRect) #blit screenshot
            dx=mx-sx #dimensions
            dy=my-sy
            ellRect=Rect(sx,sy,dx,dy)
            ellRect.normalize() #normalize in case the number is negative
            draw.ellipse(screen,col,ellRect)

#-----------------------------------------------------------------------------------------------
                         
        if tool=="draw line":
            screen.blit(screenShot,canvasRect) #blit the screenshot from earlier
            draw.line(screen,col,(sx,sy),(mx,my),SIZE) #draw from start pos to current pos

#-----------------------------------------------------------------------------------------------
                         
        if tool=="draw unfilled rectangle":
            screen.blit(screenShot,canvasRect) #screenshot
            dx=mx-sx #to find the width
            dy=my-sy #to find the height
            draw.rect(screen,col,(sx,sy,dx,dy),3) #so the rectangle starts where you first clicked and the dimensions are based on where the user decides to drag the other sides

#-----------------------------------------------------------------------------------------------

        if tool=="filled rectangle":
            screen.blit(screenShot,canvasRect)
            dx=mx-sx
            dy=my-sy
            draw.rect(screen,col,(sx,sy,dx,dy)) #same as unfilled except you don't set a rectangle width

#-----------------------------------------------------------------------------------------------
                         
        if tool=="eraser":
            tx=mx-ox #trianglex
            ty=my-oy #triangley
            dist=hypot(tx,ty) #hypotenuse
            dist=max(1,dist)
            sx=(tx/dist) #coordinate of the small triangle formed with dimensions 1x1
            sy=(ty/dist)
            for i in range(int(dist)):
                draw.circle(screen,white,(ox+int(sx*i),oy+int(sy*i)),15) #same as marker except you can only draw in white

#-----------------------------------------------------------------------------------------------
                         
        if tool=="limit fill":
               sc=screen.get_at((mx,my)) #gets the colour of the pixel where the user right-clicked 

               pixels = [(mx,my)] #list of points
               while len(pixels)>0: #the length of the list must be greater than 0
                   newPixels =[] #new list
                   for fillx,filly in pixels: #for every pixel within the pixel list
                       if 0<fillx<width and 0<filly<height and screen.get_at((fillx,filly))==sc:

                            screen.set_at((fillx,filly),col) #make that pixel the colour user selects

                            newPixels += [(fillx+1,filly),(fillx-1,filly),(fillx,filly-1),(fillx,filly+1)] #for all the pixels going up
                            #down, right and left around each pixel
                   pixels = newPixels #pixels list gets bigger
               tool="no tool" #now set it to no tool so that the program does not lag or crash
                            
#-----------------------------------------------------------------------------------------------

        if tool=="draw bubbles": #an additional tool for good measure
            bubbleTool=transform.smoothscale(bubbleTool,(50,50))
            screen.blit(bubbleTool,(mx-20,my-20)) #user can blit bubbles as they please

#-----------------------------------------------------------------------------------------------
            
        if tool=="select":
            screen.blit(screenShot,canvasRect) #blit the screenshot
            if mb[0]==1: #mouse is down
                if forming:      
                    dx=mx-sx #dimensions of rectangle
                    dy=my-sy
                    rec = Rect(sx,sy,dx,dy)
                    draw.rect(screen,white,rec,2)  #user can drag and draw the rect
                elif blitting==True:
                    draw.rect(screen,white,Rect(mx-1,my-1,miniscreen.get_width()+2,miniscreen.get_height()+2))#highlights copied area
                    screen.blit(miniscreen,(mx,my)) #blit the subsurface at mx,my

#----------------------------------------------------------------------------------------------

#########################################################################################stamps
        
        if tool=="baymax stamp":
            
            if mmode=="down": #if mouse is down
                screen.blit(screenShot,canvasRect) #blit the screenshot so the stamp does not continuously draw
                screen.blit(baymax2,(mx-73,my-53)) #then blit the stamp, I set it so that the cursor is at the centre of the stamp
                
        #same goes for all the other stamps
                
        if tool=="gogo stamp":
            if mmode=="down":
                screen.blit(screenShot,canvasRect)
                screen.blit(gogo2,(mx-59,my-48))
                
        if tool=="lemon stamp":
            if mmode=="down":
                screen.blit(screenShot,canvasRect)
                screen.blit(lemon2,(mx-95,my-50))
                
        if tool=="dragon stamp":
            if mmode=="down":
                screen.blit(screenShot,canvasRect)
                screen.blit(dragon2,(mx-88,my-72))
                
        if tool=="hiro stamp":
            if mmode=="down":
                screen.blit(screenShot,canvasRect)
                screen.blit(hiro2,(mx-68,my-58))
                
        if tool=="wasabi stamp":
            if mmode=="down":
                screen.blit(screenShot,canvasRect)
                screen.blit(wasabi2,(mx-105,my-103))   #must have correct cooridinates for cursor so that it is centered
                
        if tool=="super baymax stamp":
            if mmode=="down":
                screen.blit(screenShot,canvasRect)
                screen.blit(superBaymax,(mx-100,my-100))
   
        screen.set_clip(None) #now there is no need to only modify canvas because there are no more tools

#-----------------------------------------------------------------------------------------------

    if screenRect.collidepoint(mx,my) and mb[0]==1: #for the tools which do not need to interfere with the canvas
        
        if tool=="undo" and clicked:
            if len(undo)>1: #list size must be greater than one
                redo.append(undo.pop()) #pop function is same as del function
                screen.blit(undo[-1], (190,60)) #blit the last image in the list
            
                
        if tool=="redo" and clicked:
            if len(redo)>=1:
                screen.blit(redo[-1],(190,60)) #blit last image
                undo.append(redo.pop()) #then add to undo list
                
        if canvasRect.collidepoint(mx,my) and mb[0]==1: #if the mouse clicks on the canvas
            if tool!=redo and tool!=undo and len(redo)>0: #and user clicks on any other tool and the redo list has at least one image
                redo=[] #clear out the redo list
                #we must do this because if the user clicks undo, but then draws something else with a different tool and then
                #presses redo, then the program would have blitted an image before the user clicked undo because that image is still
                #in the list so it will blit. While using the program the user could undo and redo many times, however these three
                #lines make sure that the moment you draw something on the canvas, last, then you cannot redo because there is nothing
                #to redo, without these lines the program would blit the image.pop() when you first clicked undo.
        

        if tool=="open":
            fname = filedialog.askopenfilename(filetypes=[("Images", "*.png;*.bmp;*.jpg;*.jpeg")]) #function to make open dialogue box pop up, file types are included for which ones are compliant
            openImage=image.load(fname) #load the image
            screen.blit(openImage,(190,60)) #blit the image
            tool="no tool" #change tool to no tool so open does not glitch

        if tool=="save":
            fname = filedialog.asksaveasfilename(defaultextension=".png") #dialogue box pops up, file automatically saves as a png file
            image.save(screen.subsurface(canvasRect),fname) #save the image the user saved
            tool="no tool" #change tool to no tool so save does not glitch

        if tool=="new canvas":
            draw.rect(screen,white,canvasRect)

#-----------------------------------------------------------------------------------------------
 
#-----------------------------------------------------------------------------------------------     
  
    ox=mx #for tools
    oy=my
    
#-----------------------------------------------------------------------------------------------
    
    if spectrumRect.collidepoint(mx,my) and mb[0]==1: #if mouse collides with the spectrum, and they click
        col=screen.get_at((mx,my)) #colour is set to whatever the mouse clicks on in the color spectrum

#-----------------------------------------------------------------------------------------------
    
    display.flip()
    display.update()
    myClock.tick(60)
    
    #print(smode)
    
quit()
#Done
