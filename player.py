from tile import Tile
#import numpy as np


class Player:

    color = ""

    def __init__(self, c,boar): #this constructor initalizes the Rest Tiles and the color of the player
        self.color = c
        self.readyTiles = []
        self.restTiles = []
        self.takenTiles = []
        self.BoardTiles = boar
        for i in range(6):
            t = Tile(c,i+1)
            self.restTiles.append(t)
             
    def addToReady(self, tile): #this function adds a tile from the resttile to the ready tile by passing an integer to the function
        if(len(self.readyTiles) >= 3):
            print("invalid move")
        else:
            self.readyTiles.append(self.restTiles[tile])
            del self.restTiles[tile]

    def playPiece(self):
        if(len(self.readyTiles)==0):
            print("invalid move")
        else:
            tile = self.readyTiles.pop()
            self.BoardTiles.addToB(tile)
            tile.move()

    def movePiece(self, tile):
        if(tile.end()):
            val = input("add to rest(1) or to ready(2)")
            if(val == 1):
                self.restTiles.append(self.BoardTiles[tile])
            else: 
                self.readyTiles.append(self.BoardTiles[tile])
        self.BoardTiles.action(tile)
        tile.move()
    
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

