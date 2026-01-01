from dataclasses import dataclass

@dataclass
class Hex():
    corners: list[int]
    edges: list[int]
    resource_type: str
    robber: bool = False
    
    def __str__(self):
        return f"Hex: {self.resource_type}"

