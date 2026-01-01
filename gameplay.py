from board import Board
from player import Player

class GameManager():
    def __init__(self):
        self.board = Board()
        self.players = [Player(f'Player {n}') for n in range(4)]
        for p in self.players:
            print(p)
