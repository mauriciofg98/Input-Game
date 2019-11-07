import pygame
class Board:
    grid=[]
    tiles=[None for a in range(12)]
    def __init__(self,bscale,bpos):
        width=int(bscale[0]/3)
        height= int(bscale[1]/4)
        xStart=bpos[0]
        yStart=bpos[1]
        row= -1
        col=0
        for a in range(12):
            if a %3== 0 :
                row=row+1
            if col==3:
                col=0
            squareX=xStart+(width*col)
            squareY= yStart+(height*row)
            rectSpecs=(squareX,squareY,width,height)
            self.grid.append(pygame.Rect(rectSpecs))
            col=col+1
    
    def addToB(self,tile):
        #(y,x)
        i= tile.path[tile.OnPath]
        newI=11-(((i[0]-1)*3) +(i[1]-1))
        print("{} {}".format(newI,tile.path[tile.OnPath]))
        self.tiles[newI]=tile
    
    def getTile(self,eX,eY):
        for a in range(len(self.grid)):
            if self.grid[a].collidepoint(eX,eY):
                return (a,False)
        return (None,True)

    def action(self,tile):
        i= tile.path[tile.OnPath]
        newI=12-(((i[0]-1)*3) +(i[1]-1))
        self.tiles[newI]=tile

        a= tile.path[tile.OnPath-1]
        newA=12-(((a[0]-1)*3) +(a[1]-1))
        self.tiles[newA]= None