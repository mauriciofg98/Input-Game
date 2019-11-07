from player import Player
import pygame

# player1 = Player("R")
# player2 = Player("B")
# pla
#Players=[Player("R"),Player("B")]

play1= Player("R")
play1.printRestTiles()
play1.addToReady(5)
play1.printRestTiles()

play1.addToReady(4)

play1.playPiece()
play1.printRestTiles()

play1.printBoardTiles()
play1.printReadyTiles()


play1.loc()