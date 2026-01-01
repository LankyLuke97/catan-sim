from hex import Hex
from random import shuffle

class Board():
    def __init__(self):
        chits = [2,3,3,4,4,5,5,6,6,8,8,9,9,10,10,11,11,12]
        resources = ["desert"] + ["field"]*4 + ["forest"]*4 + ["hill"]*3 + ["mountain"]*3 + ["pasture"]*4
        shuffle(chits)
        shuffle(resources)
        rows = [3,4,5,4,3]
        self.tiles = []
        self.probabilities = {i: [] for i in range(2, 13)}
        
        while rows:
            n = rows.pop()
            self.tiles.append([])
            for _ in range(n):
                hex = Hex([],[],resources.pop())
                if hex.resource_type != "desert": self.probabilities[chits.pop()].append(hex)
                self.tiles[-1].append(hex)
        
        for row in self.tiles:
            print('-'*(len(row)*3+1))
            print(f'|{"|".join(hex.resource_type[:2] for hex in row)}|')
            print('-'*(len(row)*3+1))
        print(self.probabilities)
