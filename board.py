from hex import Hex
from random import shuffle

class Board():
    def __init__(self):
        chits = [2,3,3,4,4,5,5,6,6,8,8,9,9,10,10,11,11,12]
        resources = ["desert"] + ["field"]*4 + ["forest"]*4 + ["hill"]*3 + ["mountain"]*3 + ["pasture"]*4
        shuffle(chits)
        shuffle(resources)
        rows = [3,4,5,4,3]
        self.vertices = [None] * 56 # 3,4,4,5,5,6,6,5,5,4,4,3
        self.tiles = []
        self.roll_to_hex = {i: [] for i in range(2, 13)}
        
        for n in rows:
            self.tiles.append([])
            for _ in range(n):
                hex = Hex(resources.pop())
                if hex.resource_type != "desert": self.roll_to_hex[chits.pop()].append(hex)
                self.tiles[-1].append(hex)

    def get_potential_builds(self, player: Player) -> tuple[tuple, tuple]:
        return tuple()

    def pretty_debug(self):
        for row in self.tiles:
            print('-'*(len(row)*3+1))
            print(f'|{"|".join(hex.resource_type[:2] for hex in row)}|')
            print('-'*(len(row)*3+1))
        print(self.roll_to_hex)
