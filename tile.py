from  consts import TileConst
class Tile:
    belongs=""
    path={}
    OnPath=0
    def __init__(self,player,tileNumber):
        self.belongs=player
        if(player == "B"):
            tilepath=TileConst().altT(tileNumber)
        else:
            tilepath=TileConst().Paths[tileNumber]
        for i in range(len(tilepath)):
            self.path[i+1]=tilepath[i]

        print("{}=={}".format(tileNumber,self.path))
        print("~~~~~~~~~~~~")
    
    def move(self):
        # places tile in board
        self.OnPath=self.OnPath+1
        if(self.end()):
            self.OnPath=1
        return self.path[self.OnPath]

    def currentlocation(self):
        if(self.OnPath== 0):
            return (-1,-1)
        else:
            return self.path

    def end(self):
        if self.OnPath== 4:
            return True
        else:
            return False
    
    def setToRest(self):
        self.OnPath=0
        pass