import pygame
import random
from player import Player
from realBoard import Board


class Game:
    def __init__(self,x,y,amountP=2):
        pygame.init()
        pygame.display.set_caption("Input")
        self.activeP=0
        self.wSize=(x,y)
        self.window= pygame.display.set_mode(self.wSize)
        self.gridScale=(int(x*.4),int(y*.6))
        self.gridpos= (int(x*.3),int(y*.2))
        self.board = Board(self.gridScale,self.gridpos)
        self.lastE=None
        self.OnePlayer=False


        if(amountP==1):
            self.OnePlayer=True
            
        self.players=[Player("R",self.board),Player("B",self.board,self.OnePlayer)]

        self.window.fill((255,255,255))
        self.drawGrid(self.lastE)
        for p in self.players:
            self.drawTiles(p,self.gridScale,self.gridpos,self.lastE)

        pygame.display.flip()
    def run(self):
        pygame.time.delay(100)
        
        gScale=self.gridScale
        gPos=self.gridpos

        self.lookForEvent(self.players[self.activeP])
        if(self.activeP==0):
            self.activeP=1
        else:
            self.activeP=0
        return True

    def drawGrid(self,ev=None):
        for sq in range(12):
            dim=self.board.grid[sq]
            if self.board.tiles[sq] is not None:
                temp= pygame.transform.scale(pygame.image.load(self.board.tiles[sq].image),(dim.width,dim.height))
                rect= self.window.blit(temp,(dim.x,dim.y))
            else:
                pygame.draw.rect(self.window,(0,0,0),dim,1)
        if ev is not None:
            if ev[1] is not None:
                pygame.draw.rect(self.window,(255,255,0),self.board.grid[ev[1]],3)

                

    def drawTiles(self,p,gScale,gPos,ev=None):
        a=False
        if self.activeP== 0:
            pName="RED"
        else:
            pName="BLUE"
        font=pygame.font.Font('freesansbold.ttf', int(self.wSize[1]*.027))
        text = font.render('{} Player'.format(pName), True, (0,0,0)) 
        textRect = text.get_rect() 
        self.window.blit(text,textRect)

        temp1=self.displayReadyPile(p,gScale,gPos,ev)
        if(temp1):
            a=temp1
        temp2=self.displayTakenPile(p,gScale,gPos,ev)
        if(temp2):
            a=temp2
        temp3=self.displayRestPile(p,gScale,gPos,ev)
        if(temp3):
            a=temp3
        temp4 = self.displayMovedTile(p,gScale,gPos,ev)
        if(temp4):
            a=temp4
        return a

    def displayMovedTile(self,p, gScale,gPos,ev):
        if self.checkCurrentP(p):
            if ev is not None:
                if ev[1] is not None:
                    if ev == self.lastE:
                        if self.board.tiles[ev[1]] is not None:
                            if self.board.tiles[ev[1]].belongs == p.color:
                                worked=p.movePiece(self.board.tiles[ev[1]])
                                return worked
        return False
                        

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
        
        takeout=None
        for tile in range(len(p.restTiles)):
            start=xStart+((width+5)*tile)
            img= pygame.transform.scale(pygame.image.load(p.restTiles[tile].image).convert(),(width,height))
            rect=self.window.blit(img,(start,yStart))
            if ev is not None:
                if rect.collidepoint(ev[0]):
                    if self.lastE is not None and rect.collidepoint(self.lastE[0]):
                        takeout=tile
                    rectSpecs=(start,yStart,width,height)
                    pygame.draw.rect(self.window,(255,255,0),pygame.Rect(rectSpecs),7)
                    temp=False

        # if takeout is not None and p.color == self.activeP:
        nextPlayer=False
        if(self.checkCurrentP(p)):
            if takeout is not None:
                nextPlayer= p.addToReady(takeout)

        
        return nextPlayer
            
    def displayReadyPile(self,p,gScale,gPos,ev):
        #DIMENSIONS OF TILES
        width=(gScale[0]//3)
        height= gScale[1]//4
        #FONTS
        font=pygame.font.Font('freesansbold.ttf', int(self.wSize[1]*.027))
        text = font.render('Ready Pile', True, (0,0,0)) 
        textRect = text.get_rect() 

        X= gPos[0]+gScale[0]+20
        takeout= False
        if(p.color == "R"):
            yStart= gPos[1]+gScale[1] - height
            self.window.blit(text,(X,yStart-int(self.wSize[1]*.027)))
        else:
            yStart=gPos[1]
            self.window.blit(text,(X,yStart+int(self.wSize[1]*.027)+height))
        if(len(p.readyTiles)>0):
            rectSpecs=(X,yStart,width,height)
            img= pygame.transform.scale(pygame.image.load(p.readyTiles[-1].image),(width,height))
            rect=self.window.blit(img,(X,yStart))
            if rect.collidepoint(ev[0]):
                pygame.draw.rect(self.window,(255,255,0),pygame.Rect(rectSpecs),3)
                if self.lastE is not None and rect.collidepoint(self.lastE[0]):
                    takeout=True        
        # if takeout and p.color == self.activeP:
        if (self.checkCurrentP(p)):
            if takeout:
                return p.playPiece()

    def checkCurrentP(self,player):
        if(self.activeP==0):
            if( player.color=='R'):
                return True
        else:
            if(player.color== 'B'):
                return True
        return False
    
    def ComputerChoice(self,player):
        choice= None
        while choice == None:
            ans= random.randint(0, 2)
            if ans == 1:
                if(len(player.restTiles)>0):
                    if(player.addToReady(random.randrange(0,len(player.restTiles)))):
                        choice= 2
            elif ans== 2:
                if player.playPiece():
                    choice=2
            else:
                for i in player.BoardTiles.tiles:
                    if i is not None:
                        if i.belongs == player.color:
                            player.movePiece(i)
                            choice=2
                            break

        


    def lookForEvent(self, player):
        waitForE=False
        if not self.OnePlayer:
            while not waitForE:
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
                            if( player == p):
                                waitForE=self.drawTiles(p,self.gridScale,self.gridpos,thing)
                            else:
                                self.drawTiles(p,self.gridScale,self.gridpos,thing)
                        self.lastE=thing
                        pygame.display.update()
                        
        else:
            if self.activeP==0:
                while not waitForE:
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
                                if( player == p):
                                    waitForE=self.drawTiles(p,self.gridScale,self.gridpos,thing)
                                else:
                                    self.drawTiles(p,self.gridScale,self.gridpos,thing)
                            self.lastE=thing
                            pygame.display.update()
            else:
                self.ComputerChoice(player)
                self.window.fill((255,255,255))
                self.drawGrid(self.lastE)
                for p in self.players:
                    self.drawTiles(p,self.gridScale,self.gridpos,self.lastE)


        pygame.display.update()


            


