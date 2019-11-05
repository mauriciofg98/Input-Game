import Tile from tile

class player:

    color = ""
    readyTiles = []
    restTiles = []
    takenTiles = []
    BoardTiles = []

    def __init__(self, c,): #this constructor initalizes the Rest Tiles and the color of the player
        self.color = c
        for i in range(1,7):
            tile1 = tile(c, i)
            self.restTiles.append(tile1)

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
            tile.action()

    def movePiece(self, tile):
        if(tile.end()):
            val = input("add to rest(1) or to ready(2)")
            if(val == 1):
                self.restTiles.append(self.BoardTiles[tile])
            else: 
                self.readyTiles.append(self.BoardTiles[tile])
        self.BoardTiles[tile].action()
    


