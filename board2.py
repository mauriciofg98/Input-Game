from player import Player
import pygame

pygame.init()

win = pygame.display.set_mode((500,500))
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.display.set_caption("Input")
x=50
y=50
width = 40
height = 60
vel =5
background= pygame.image.load("Tiles/board.png")
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

pygame.quit()

player1 = Player("R")
player2 = Player("B")


#Players=[Player("R"),Player("B")]