class Hex():
    def __init__(self, resource_type: str):
        self.corners: list[int] = [0]*6
        self.edges: list[int] = [0]*6
        self.resource_type: str = resource_type
        self.robber: bool = False

    def __str__(self):
        return f"Hex: {self.resource_type}"

