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
        pass
    def altT(self,number):
        path=[]
        for a in Paths[number]:
            y= 3-a[1]
            x= 4-a[0]
            path.append((x,y))
        return path