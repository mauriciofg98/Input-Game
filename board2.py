from player import Player
import pygame
from itertools import chain

pygame.init()

#window size
win = pygame.display.set_mode((800,600))

#fonts and colors use "B" stands for bright
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0,200,0)
BGREEN = (0,255,0)
BRED = (255,0,0)
RED = (200,0,0)
BLUE = (0,0,200)
BBLUE = (0,0,255)
PINK = (219,112,147)
BPINK = (255,105,180)
clock = pygame.time.Clock()
largeText = pygame.font.SysFont("lucidabright",75)
smallText = pygame.font.SysFont("gadugi",20)
tinyText = pygame.font.SysFont("gadugi",17)

pygame.display.set_caption("Input")
x=50
y=50
width = 40
height = 60
vel =5
background= pygame.image.load("Tiles/board.png")

#creates a text box and makes the text white
def text_objects(text, font):
    textSurface = font.render(text, True, WHITE)
    return textSurface, textSurface.get_rect()

#creates a redirecting button (message, x coord, y coord, width, height, inactive color, active color, the action aka function)
def button(msg,x,y,w,h,ic,ac,action= None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(win, ac,(x,y,w,h))
        if click[0] ==1 and action != None:
            action()
    else:
        pygame.draw.rect(win, ic,(x,y,w,h))

    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    win.blit(textSurf, textRect)

def truncline(text, font, maxwidth):
        real=len(text)       
        stext=text           
        l=font.size(text)[0]
        cut=0
        a=0                  
        done=1
        old = None
        while l > maxwidth:
            a=a+1
            n=text.rsplit(None, a)[0]
            if stext == n:
                cut += 1
                stext= n[:-cut]
            else:
                stext = n
            l=font.size(stext)[0]
            real=len(stext)               
            done=0                        
        return real, done, stext             
        
def wrapline(text, font, maxwidth): 
    done=0                      
    wrapped=[]                  
                               
    while not done:             
        nl, done, stext=truncline(text, font, maxwidth) 
        wrapped.append(stext.strip())                  
        text=text[nl:]                                 
    return wrapped

#slices text into a list where each item fits within the maxwidth
def wrap_multi_line(text, font, maxwidth):
    lines = chain(*(wrapline(line, font, maxwidth) for line in text.splitlines()))
    return list(lines)
#prints text in list
def displaytxt(txt, num):
    for words in txt:
        TextSurf, TextRect = text_objects(words, tinyText)
        TextRect.center = ((400),(num))
        win.blit(TextSurf, TextRect)
        num = num+20
#displays the "about us" information 
def about():
    run = True
    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        win.fill(BLACK)
        TextSurf, TextRect = text_objects("About Us", largeText)
        TextRect.center = ((800/2),(100))
        win.blit(TextSurf, TextRect)
        a = ['Group Q', 'Mauricio Flores', 'Alissa Flores', 'Roberto Rivas', 'William Reckley']
        displaytxt(a,400)
        TextSurf, TextRect = text_objects("Creator of Game: Milton Bradley ", smallText)
        TextRect.center = ((400),(300))
        win.blit(TextSurf, TextRect)

        pygame.display.flip()

#displays the rules of the game
def howto():
    run = True
    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        win.fill(BLACK)
        TextSurf, TextRect = text_objects("How to Play", largeText)
        TextRect.center = ((800/2),(100))
        win.blit(TextSurf, TextRect)

        font = pygame.font.SysFont("gadugi",20)
        a = wrapline("Each player has 6 tiles and 3 main areas – rest, ready, and taken.", font, 750 )
        displaytxt(a, 170)
        b = wrapline("A player turn consists of moving a tile from rest to ready, ready to board, or moving the tile to another location on the board.", font, 750)
        displaytxt(b,200)
        c = wrapline("Each tile contains an image of the spaces on in which the tile can occupy on the board. The hollow circle indicates its initial position, and the tile must be moved consecutively corresponding to its connected lines. Once a tile has occupied all of its spaces the player may either place it back in the “ready” or “rest” area. ", font, 750)
        displaytxt(c,250)
        d = wrapline("For a tile to be in play it must be moved from the rest area to the ready area. The ready area can hold up to three tiles at one time. A tile must be removed from the ready area and placed on the board in a last come first serve order meaning that the most recent tile placed in the area must be placed on the board first. ", font, 750 )
        displaytxt(d,350)
        e = wrapline("In order to take an opponent’s tile your tile must move to a space on the board that is already occupied by an opposing tile, therefore claiming the space and removing their tile to your taken area.", font, 750)
        displaytxt(e,440)
        f = wrapline("The player who claims and places all of their opponent’s tiles in their “taken” area wins.", font, 750)
        displaytxt(f,510)
        
        pygame.display.flip()

#main menu that redirects window to alterate pages via buttons
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        win.fill(BLACK)
        
        TextSurf, TextRect = text_objects("Input", largeText)
        TextRect.center = ((800/2),(600/4))
        win.blit(TextSurf, TextRect)

        button("Start",350,250,100,50,GREEN,BGREEN,game)
        button("How to Play",312.5,325,175,50,RED,BRED,howto)
        button("About Us",335,400,125,50,BLUE,BBLUE, about)
        button("Quit",350,475,100,50,PINK,BPINK,quit)

        pygame.display.update()
        clock.tick(15)
        

#initiates the game      
def game():
    run = True
    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        win.fill(WHITE)
        win.blit(pygame.transform.scale(background,(250,250)),(200,250))
        pygame.draw.circle(win, BLACK, [80, 80], 80, 0)
        
        pygame.display.flip()

game_intro()
game()
pygame.quit()
quit()

player1 = Player("R")
player2 = Player("B")


#Players=[Player("R"),Player("B")]