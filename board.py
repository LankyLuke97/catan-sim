from hex import Hex
from random import shuffle

class Board():
    def __init__(self):
        resources = ["desert"] + ["field"]*4 + ["forest"]*4 + ["hill"]*3 + ["mountain"]*3 + ["pasture"]*4
        shuffle(resources)
        rows = [3,4,5,4,3]
        self.tiles = []
        
        while rows:
            n = rows.pop()
            self.tiles.append([])
            for _ in range(n):
                self.tiles[-1].append(Hex([],[],resources.pop()))
        
        for row in self.tiles:
            print('-'*(len(row)*3+1))
            print(f'|{"|".join(hex.resource_type[:2] for hex in row)}|')
            print('-'*(len(row)*3+1))
