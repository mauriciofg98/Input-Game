class TileConst:
    Paths={
        1:[(1,3),(3,3),(4,2),(3,1),(2,1)],
        2:[(1,3),(2,3),(4,3),(3,1),(2,2)],
        3:[(1,2),(2,3),(3,2),(4,1),(2,2)],
        4:[(1,1),(2,2),(3,3),(4,2),(2,1)],
        5:[(1,2),(3,3),(3,2),(4,1),(2,1)],
        6:[(1,1),(2,3),(4,3),(3,2),(3,1)],
    }

    def __init__(self):
        self.path = []

    def altT(self,number):
        #self.path=[]
        for a in self.Paths[number]:
            y= 4-a[1]
            x= 5-a[0]
            self.path.append((x,y))
        return self.path