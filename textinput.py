from pygame import *

def getText(screen,xx,yy):
    ans = ""        # final text will be built one letter at a time.
    comicFont = font.SysFont("Comic Sans MS", 16)
    back = screen.copy()  
    textArea = Rect(xx,yy,200,25) 

    cursorShow = 0
    myclock = time.Clock()
    typing = True
    while typing:
        cursorShow += 1
        for e in event.get():
            if e.type == QUIT:
                event.post(e)   # puts QUIT back in event list so main quits
                return ""
            if e.type == KEYDOWN:
                if e.key == K_BACKSPACE:    # remove last letter
                    if len(ans)>0:
                        ans = ans[:-1]
                elif e.key == K_KP_ENTER or e.key == K_RETURN : 
                    typing = False
                elif e.key < 256:
                    ans += e.unicode       # add character to ans
                    
        txtPic = comicFont.render(ans, True, (0,0,0))   #
        draw.rect(screen,(170,249,244),textArea)        # draw the text window and the text.
        draw.rect(screen,(0,0,0),textArea,2)            
        screen.blit(txtPic,(textArea.x+3,textArea.y+2))
       
        if cursorShow // 50 % 2 == 1:
            cx = textArea.x+txtPic.get_width()+3
            cy = textArea.y+3
            draw.rect(screen,(255,0,0),(cx,cy,2,textArea.height-6))
        myclock.tick(100)
        display.flip()
        
    screen.blit(back,(0,0))
    return ans
