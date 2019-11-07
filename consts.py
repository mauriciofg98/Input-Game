class TileConst:
    Paths={
        1:[(1,3),(3,3),(4,2),(3,1),(2,1)],
        2:[(1,3),(2,3),(4,3),(3,1),(2,2)],
        3:[(1,2),(2,3),(3,2),(4,1),(2,2)],
        4:[(1,1),(2,2),(3,3),(4,2),(2,1)],
        5:[(1,2),(3,3),(3,2),(4,1),(2,1)],
        6:[(1,1),(2,3),(4,3),(3,2),(3,1)],
    }

    images={
        1: 'Tiles/red1.png',
        2: 'Tiles/red2.png',
        3: 'Tiles/red3.png',
        4: 'Tiles/red4.png',
        5: 'Tiles/red5.png',
        6: 'Tiles/red6.png',
        7: 'Tiles/blue1.png',
        8: 'Tiles/blue2.png',
        9: 'Tiles/blue3.png',
        10: 'Tiles/blue4.png',
        11: 'Tiles/blue5.png',
        12: 'Tiles/blue6.png'
    }
    
    def __init__(self):
        self.path = []

    def altT(self,number):
        self.path=[]
        for a in self.Paths[number]:
            y= 4-a[1]
            x= 5-a[0]
            self.path.append((x,y))
        return self.path
    
    def blueImages(self, number):
        return self.images[number+6]
    
    def redImages(self, number):
        return self.images[number]
