from Animal import Animal


class Sheep(Animal):
    def __init__(self, positionX, positionY, world):
        super().__init__(positionX, positionY, world)
        self.strength = 4
        self.initiative = 4

    def spawn(self, x, y, world):
        self.world.addOrganism(Sheep(x, y, world))
