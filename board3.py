from player import Player
import pygame

player1 = Player("R")
player2 = Player("B")

pygame.init()

win = pygame.display.set_mode((500,500))
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

horizontal = 25
pygame.display.set_caption("Input")
x=50
y=50
width = 40
height = 60
vel =5
background= pygame.image.load("Tiles/board.png")
grid = pygame.transform.rotate(background,90)
run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    win.fill(WHITE)

    for i in player1.restTiles:
        temp = pygame.image.load(i.image)
        win.blit(pygame.transform.rotate(pygame.transform.scale(temp,(60,80)),180),(horizontal,0))
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Set the x, y postions of the mouse click
            k, j = event.pos
            if temp.get_rect().collidepoint(k, j):
                print("clicked on this image {}".format(i.label))
        horizontal = horizontal+75
    
    horizontal = 25

    for i in player2.restTiles:
        temp = pygame.image.load(i.image)
        win.blit(pygame.transform.scale(temp,(70,85)),(horizontal,350))
        horizontal = horizontal+75
    horizontal = 25


    win.blit(pygame.transform.scale(grid,(150,200)),(200,100))
    
    pygame.display.flip()

pygame.quit()

#player1 = Player("R")
#player2 = Player("B")


#Players=[Player("R"),Player("B")]