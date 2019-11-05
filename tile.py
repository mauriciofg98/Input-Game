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
    
    def move():
        # places tile in board
        OnPath=OnPath+1
        if(OnPath>4):
            OnPath=1
        return path[OnPath]

    def currentlocation():
        return path[OnPath]

    def end():
        if OnPath== 4:
            return True
        else
            return False
        