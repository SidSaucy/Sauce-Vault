
import pygame
from pygame.locals import *

import time, random
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Comet Defender Gamemenu')
pygame.event.get() 
purple = (97,0,242)
black = (0,0,0)
blue = (97,0,242)
seafoam = (77,245,135)
lightturquoise = (204,255,229)
butterscotch = (255,255,153)
lavender = (204,204,255)
lightpink = (255,204,229)
pistachio =  (204,255,204)
viscolor = (153,204,255)
NeonPink = (255,0,237)
Lime = (170,255,0)
rottenPumpkin = (255,213,0)
yellow = (255,255,0)
red = (255,0,0)
white=(255,255,255)

def show_text(msg,x,y,color,size):
    fontobj=pygame.font.SysFont('freesans',size)
    msgobj=fontobj.render(msg,False,color)

    screen.blit(msgobj,(x,y))








screen = pygame.display.set_mode((1024,576))
pygame.display.set_caption("Comet Defender")
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)

score=0

##    show_text ("Score:0",10,10,blue)
img4 = pygame.image.load('Laser.png')
img5 = pygame.image.load('Ex1.png')
astro = ['Astro1.png','Astro2.png','Astro3.png','Astro4.png','Astro5.png','Astro6.png','Astro7.png','Astro8.png','Astro9.png','Astro10.png','Astro11.png','Astro12.png','Astro13.png','Astro14.png','Astro15.png','Astro16.png','Astro17.png','Astro18.png','Astro19.png','Astro20.png','Astro25.png']
clock = pygame.time.Clock()
def player():
    global score
    xf=900
    yf=00
    gf = 395
    hf = 215
    chhf=0
    shoot = 0
    hg = 300
    b=0
    a=1
    speed =1
    while True:
        show_text (str(score),10,10,blue,30)
    ##    clock.tick(5)
        print(gf,shoot)
        #pygame.display.update()
        for event in pygame.event.get():
           if event.type == QUIT:
                    pygame.quit()
                    exit()
           if event.type ==KEYDOWN:
                if event.key ==K_w:
                    chhf = -6
                if event.key==K_s:
                    chhf = 6
           if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                shoot = 1
            


        for x in astro:
            show_text (str(score),10,10,white,30)
            pygame.display.update()
            img1 = pygame.image.load('circstars.png')
            screen.blit(img1,(0,00))
            img = pygame.image.load(x)
            hf +=chhf
            if hf  < 0:
                hf =0
                chhf = 0
            elif hf >400:
                hf = 400
                chhf =0
            screen.blit(img,(hg,hf))
            time.sleep(.03)  
            #pygame.display.update()
            img3 = pygame.image.load('flamemeteor.png')
            screen.blit(img3,(xf,yf))
            if xf< hg <xf+50 and yf < hf<yf+35:
                
                screen.blit(img5,(xf,yf))
                pygame.display.update()
                time.sleep(1)
                xf=900
                yf=00
                gf = 395
                hf = 215
                chhf=0
                shoot = 0
                hg = 300
           
                screen.fill((0,0,0))
                show_text ('Game Over, you got clobbered by an asteroid',10,10,red,40)
                score=0
                pygame.display.update()
                time.sleep(1)
              
                gf = 395
                hf = 215
                y()
                
            
            
            if xf <0:
                screen.fill((0,0,0))
                show_text ('Game Over, you let an asteroid hit Earth',10,10,red,40)
                score = 0
                pygame.display.update()
                time.sleep(1)
                y()
                
                gf = 395
                hf = 215
                xf = 900
                
                yf = random.randint(0,500)

            if shoot == 1:
                
                screen.blit(img4,(gf,hf+75))
                gf=gf+25
                
            if xf<gf<xf+50 and yf<hf+50<yf+50:
                score  += 1
            
                screen.blit(img5,(xf,yf))
                pygame.display.update()
                time.sleep(0.1)
                xf = 900
                yf = random.randint(0,450)
                    
                    
            if gf >1024:
                shoot=0
                gf = 395
    ##       
    ##        screen.blit(img4,(gf,hf))
            #gf=gf+1
            yf=yf+0
            xf=xf-5
            yf=yf+1

            if score>4:
                    xf += -4
            if score>9:
                xf +=-9
        

##        if x  == 'Astro20.png':
##                  print("shooting")
##                  img4 = pygame.image.load('Laser.png')
##                  screen.blit(img4,(gf,hf))                
##     
    #screen.blit(img,(0,0))
def y():
    
    while True:
        pygame.display.update()
        img7 = pygame.image.load('gamescreen.png')
        screen.blit(img7,(0,00))
        #pygame.display.update()
        
        show_text('Comet Defender',100,100,NeonPink,100)
        show_text('By:Sid',200,200,Lime,65)
        show_text('Play',100,400,seafoam,60)
        show_text ('Quit',100,500, blue,60)
        pygame.draw.rect(screen,viscolor,(100,400,150,60),10)
        pygame.draw.rect(screen,red,(100,500,150,60),10)
        for event in pygame.event.get() :
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button==1:
                    print('x is : ',event.pos[0])
                    print('y is : ',event.pos[1])
                    print(event.pos)
                    x,y=event.pos
                    if x in range (100,250) and y in range (500,560):
                         pygame.quit()
                    elif x in range (100,250) and y in range (150,460):
                        print("loading")
                        player()
                                


y()              

def o():
    while true: 
        show_text('W key to move up, s key to move down,click to shoot',100,100,NeonPink,100)
        pygame.draw.rect(screen,viscolor,(100,400,150,60),10)
        pygame.draw.rect(screen,red,(100,500,150,60),10)

        if event.type == pygame.MOUSEBUTTONDOWN and event.button==1:
                    print('x is : ',event.pos[0])
                    print('y is : ',event.pos[1])
                    print(event.pos)
                    x,y=event.pos
                    if x in range (100,250) and y in range (500,560):
                         pygame.quit()
                    elif x in range (100,250) and y in range (150,460):
                        print("loading")
                        player()
y()
