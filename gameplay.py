from random import randrange

from board import Board
from player import Player

class GameManager():
    def __init__(self):
        self.board = Board()
        self.players = [Player(f'Player {n}') for n in range(4)]
        for p in self.players:
            print(p)

    def roll(self):
        d1, d2 = randrange(1, 6), randrange(1, 6)
        print(d1, d2, self.board.probabilities[d1+d2])
