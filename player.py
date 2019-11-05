from tile import Tile

class player:

    color = ""

    def __init__(self, c,): #this constructor initalizes the Rest Tiles and the color of the player
        self.color = c
        self.readyTiles = []
        self.restTiles = []
        self.takenTiles = []
        self.BoardTiles = []

        for i in range(6):
            t= Tile(c,i+1)
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
            self.BoardTiles.append(tile)
            tile.move()

    def movePiece(self, tile):
        if(tile.end()):
            val = input("add to rest(1) or to ready(2)")
            if(val == 1):
                self.restTiles.append(self.BoardTiles[tile])
            else: 
                self.readyTiles.append(self.BoardTiles[tile])
        self.BoardTiles[tile].action()
    
    def loc(self):
        print(self.BoardTiles[0].currentlocation())

play1= player("R")
play1.addToReady(3)
play1.playPiece()
# play1.loc()

