class Settlement:
    def __init__(self, player: Player) -> None:
        self.player = player
        self.upgraded = False

    def add_resource(self, resource_type: str) -> None:
        self.player.add_resources(resource_type)
        if self.upgraded: self.player.add_resources(resource_type)

    def upgrade(self) -> bool:
        if self.upgraded: return False
        return self.upgraded = True
