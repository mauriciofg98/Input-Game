from tile import Tile
#import numpy as np


class Player:

    color = ""

    def __init__(self, c,boar,comp=False): #this constructor initalizes the Rest Tiles and the color of the player
        self.color = c
        self.readyTiles = []
        self.restTiles = []
        self.takenTiles = []
        self.BoardTiles = boar
        self.comp=comp
        for i in range(6):
            t = Tile(c,i+1,self.comp)
            self.restTiles.append(t)
             
    def addToReady(self, tile): #this function adds a tile from the resttile to the ready tile by passing an integer to the function
        if(len(self.readyTiles) >= 3):
            print("invalid move")
            return False
        else:
            self.readyTiles.append(self.restTiles[tile])
            del self.restTiles[tile]
            return True

    def playPiece(self):
        if(len(self.readyTiles)==0):
            print("invalid move")
        else:
            tile = self.readyTiles.pop()
            tile.move()
            ans=self.BoardTiles.addToB(tile)
            if ans is False:
                tile.OnPath-=1
                self.readyTiles.append(tile)
                return False
            elif ans is None:
                return True
            else:
                self.takenTiles.append(ans)
                return True
                


    def movePiece(self, tile):
        if tile is None:
            return False
        ans=self.BoardTiles.action(tile)
        if(ans == -1):
            self.restTiles.append(tile)
            return True
        if ans == None:
            return True
        elif  ans== tile:
            return False
        else:
            self.takenTiles.append(ans)
            return True





        # if(tile.end()):
        #     val = input("add to rest(1) or to ready(2)")
        #     if(val == 1):
        #         self.restTiles.append(self.BoardTiles[tile])
        #     else: 
        #         self.readyTiles.append(self.BoardTiles[tile])
        # self.BoardTiles.action(tile)
        
    
    def loc(self):
        print("the location of the tile is")
        print(self.BoardTiles[0].currentlocation())

    def printRestTiles(self):
        print("These are the tiles at rest")
        for i in self.restTiles:
            print(i.path)
        print("~~~~~~~~~~~~~~~~~~")
        
    def printReadyTiles(self):
        print("These are the tiles that are ready to play")
        for i in self.readyTiles:
            print(i.path)
        print("~~~~~~~~~~~~~~~~~~~~")
    
    def printBoardTiles(self):
        print("These are the tiles that are on the board")
        for i in self.BoardTiles:
            print(i.path)
        print("~~~~~~~~~~~~~~~~~~~~")


# play1= Player("R")
# play1.printRestTiles()
# play1.addToReady(5)

# play1.addToReady(4)

# play1.playPiece()
# play1.printRestTiles()

# play1.printBoardTiles()
# play1.printReadyTiles()


# play1.loc()

