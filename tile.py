from  consts import TileConst
import tkinter as tk
from tkinter import messagebox
import random
win=tk.Tk()

class Tile:
    
    belongs=""
    path=[]
    OnPath=-1
    image = ''
    label = ""

    t = TileConst()
    def __init__(self,player,tileNumber,comp=False):
        self.belongs=player
        self.label = tileNumber
        self.comp=comp
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
            if self.comp:
                ap= random.randint(0,1)
                if ap== 0:
                    ans=True
                else:
                    ans=False
            else:
                ans=messagebox.askyesno("PICK","Do you want to send it back to Rest Pile?")
            if(ans):
                self.setToRest()
            else:
                self.OnPath=0
            return self.OnPath
    
    def reset(self):
        self.OnPath=0
        

    def currentlocation(self):
        if(self.OnPath== 0):
            return (-1,-1)
        else:
            return "THIS IS CURRENTLY AT:{}".format(self.path[self.OnPath-1])

    def end(self):
        if self.OnPath== 5:
            return True
        else:
            return False
    
    def setToRest(self):
        self.OnPath=-1
        pass