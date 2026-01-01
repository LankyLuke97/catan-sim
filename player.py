class Player:
    def __init__(self, name: str):
        self.development_cards: list[DevelopmentCard] = []
        self.resources: dict[str, int] = {"brick":0, "ore":0, "sheep":0, "wheat":0, "wood":0}
        self.name: str = name
        self.cities: int = 4
        self.roads: int = 15
        self.settlements: int = 5

    def __str__(self):
        return f'Player {self.name}: {len(self.development_cards)} development cards, {self.cities} cities, {self.settlements} settlements, {self.roads} roads, and {", ".join([f"{v} of {k}" for k, v in self.resources.items()])}'
