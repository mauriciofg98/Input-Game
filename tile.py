from  consts import TileConst
class Tile:
    
    belongs=""
    path=[]
    OnPath=0
    image = ''
<<<<<<< HEAD
=======
<<<<<<< HEAD
    label = ""
=======
>>>>>>> a7ab81b2806004e0994f13d3805e484b48ee983b
>>>>>>> d49bcb4c2fdf5dc99d585be9e5480ab96a782871
    t = TileConst()
    def __init__(self,player,tileNumber):
        self.belongs=player
        self.label = tileNumber

        if(player == "B"):
            self.tilepath = self.t.altT(tileNumber)
            self.image = self.t.blueImages(tileNumber)
        else:
            self.tilepath=self.t.Paths[tileNumber]
            self.image=self.t.redImages(tileNumber)
        
        self.path = self.tilepath

    
    def move(self):
        # places tile in board
        self.OnPath=self.OnPath+1
        if(self.end()):
            self.OnPath=1
        

    def currentlocation(self):
        if(self.OnPath== 0):
            return (-1,-1)
        else:
            return self.path[self.OnPath-1]

    def end(self):
        if self.OnPath== 4:
            return True
        else:
            return False
    
    def setToRest(self):
        self.OnPath=0
        pass