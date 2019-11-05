class player:
    
    color = ""
    readyTiles = []
    restTiles = []
    takenTiles = []
    BoardTiles = []

    def __init__(self, c, Tilelist[]): #this constructor initalizes the Rest Tiles and the color of the player
        self.color = c
        readyTiles = Tilelist

    def addToReady(self, tile): #this function adds a tile from the resttile to the ready tile by passing an integer to the function
        if(len(self.readyTiles) >= 3):
            print("invalid move")
        else:
            self.readyTiles.append(restTiles[tiles])
            del restTiles[tile]

    def playPiece(self):
        if(len(self.readyTiles)==0):
            print("invalid move")
        else:
            tile = self.readyTiles.pop()
            BoardTiles.append(tile)
            tile.action()

    def movePiece(self, tile)
        if(BoardTiles[tile].end())
        {
            val = input("add to rest(1) or to ready(2)")
            if(val == 1):
                restTiles.append(BoardTiles[tile])
            else: 
                readyTiles.append(BoardTiles[tile])
        }
        tile.action()
    


