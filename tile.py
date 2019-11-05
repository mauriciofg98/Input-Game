import TileConst from consts
class Tile:
    belongs=""
    path={}
    OnPath=0
    def __init__(player,tileNumber):
        
        tilepath=TileConst().altT(tileNumber)
        for( i in range(len(tilepath)):
            self.path[i+1]=tilepath[i]
        self.belongs=player
    
    def move(self):
        # places tile in board
        self.OnPath=self.OnPath+1
        if(self.OnPath>4):
            self.OnPath=1
        return self.path[OnPath]

    def currentlocation():
        return self.path[self.OnPath]

    def end(self):
        if self.OnPath== 4:
            return True
        else
            return False
        