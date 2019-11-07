import pygame
from player import Player
from board2 import Board


class Game:
    def __init__(self,x,y,amountP=2):
        pygame.init()
        pygame.display.set_caption("Input")
        self.activeP="R"
        self.wSize=(x,y)
        self.window= pygame.display.set_mode(self.wSize)
        self.gridScale=(int(x*.4),int(y*.6))
        self.gridpos= (int(x*.3),int(y*.2))
        self.board = Board(self.gridScale,self.gridpos)
        self.lastE=None


        if(amountP==1):
            exit() #FOR NOW IT EXITS
        else:
            self.players=[Player("R",self.board),Player("B",self.board)]
        self.players[0].addToReady(0)
        self.players[0].playPiece()

        self.window.fill((255,255,255))
        self.drawGrid(self.lastE)
        for p in self.players:
            self.drawTiles(p,self.gridScale,self.gridpos,self.lastE)

        pygame.display.flip()
    def run(self):
        pygame.time.delay(100)
        
        gScale=self.gridScale
        gPos=self.gridpos

        self.lookForEvent(self.players[0])
        return True

    def drawGrid(self,ev=None):
        for sq in range(12):
            dim=self.board.grid[sq]
            if self.board.tiles[sq] is not None:
                temp= pygame.transform.scale(pygame.image.load(self.board.tiles[sq].image),(dim.width,dim.height))
                self.window.blit(temp,(dim.x,dim.y))
            else:
                pygame.draw.rect(self.window,(0,0,0),dim,1)
        if ev is not None:
            if ev[1] is not None:
                pygame.draw.rect(self.window,(255,255,0),self.board.grid[ev[1]],3)
    def drawTiles(self,p,gScale,gPos,ev=None):
        a=self.displayRestPile(p,gScale,gPos,ev)
        self.displayReadyPile(p,gScale,gPos,ev)
        self.displayTakenPile(p,gScale,gPos,ev)
        return a

    def displayTakenPile(self,p,gScale,gPos,ev):
        #DIMENSIONS OF TILES
        width=(gScale[0]//3)
        height= gScale[1]//4
        #FONTS
        font=pygame.font.Font('freesansbold.ttf', int(self.wSize[1]*.027))
        text = font.render('Taken Pieces:{}'.format(len(p.takenTiles)), True, (0,0,0)) 
        textRect = text.get_rect() 

        X= gPos[0]-width
        
        if(p.color == "R"):
            yStart= gPos[1]+gScale[1] - height
            textRect.center=(X,yStart-int(self.wSize[1]*.027))
            self.window.blit(text,textRect)
        else:
            yStart=gPos[1]
            textRect.center=(X,yStart+int(self.wSize[1]*.027)+height)
            self.window.blit(text,textRect)

        if(len(p.takenTiles)>0):
            img= pygame.transform.scale(pygame.image.load(p.takenTiles[-1].image),(width,height))
            self.window.blit(img,(X-20,yStart))

    
    def displayRestPile(self,p,gScale,gPos,ev):
        temp=True
        amountR=len(p.restTiles)
        width=(gScale[0]//3)
        height= gScale[1]//4
        xStart= (self.wSize[0]-((width+5)*amountR))//2
        if(p.color == "R"):
            yStart= gPos[1]+gScale[1] +10
        else:
            yStart=gPos[1]-height-10

        for tile in range(len(p.restTiles)):
            start=xStart+((width+5)*tile)
            img= pygame.transform.scale(pygame.image.load(p.restTiles[tile].image).convert(),(width,height))
            rect=self.window.blit(img,(start,yStart))
            if ev is not None:
                if rect.collidepoint(ev[0]):
                    rectSpecs=(start,yStart,width,height)
                    pygame.draw.rect(self.window,(255,255,0),pygame.Rect(rectSpecs),7)
                    temp=False
        return temp
            
    def displayReadyPile(self,p,gScale,gPos,ev):
        #DIMENSIONS OF TILES
        width=(gScale[0]//3)
        height= gScale[1]//4
        #FONTS
        font=pygame.font.Font('freesansbold.ttf', int(self.wSize[1]*.027))
        text = font.render('Ready Pile', True, (0,0,0)) 
        textRect = text.get_rect() 

        X= gPos[0]+gScale[0]+20
        
        if(p.color == "R"):
            yStart= gPos[1]+gScale[1] - height
            self.window.blit(text,(X,yStart-int(self.wSize[1]*.027)))
        else:
            yStart=gPos[1]
            self.window.blit(text,(X,yStart+int(self.wSize[1]*.027)+height))

        if(len(p.readyTiles)>0):
            img= pygame.transform.scale(pygame.image.load(p.readyTiles[-1].image),(width,height))
            self.window.blit(img,(X,yStart))
        


    def lookForEvent(self, player):
        waitForE=True
        
        while waitForE:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.window.fill((255,255,255))
                    eventX,eventY = event.pos
                    ev ,waitForE=self.board.getTile(eventX,eventY)
                    thing= ((eventX,eventY),ev)
                    self.drawGrid(((eventX,eventY),ev))
                    for p in self.players:
                        waitForE=self.drawTiles(p,self.gridScale,self.gridpos,thing)
                    self.lastE=thing
                    pygame.display.update()

                    


                    
                    
                    


        

w= Game(750,750)
r=True
while r:
    r=w.run()
pygame.quit()

