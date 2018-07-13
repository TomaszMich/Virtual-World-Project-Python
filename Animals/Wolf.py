from Animal import Animal


class Wolf(Animal):
    def __init__(self, positionX, positionY, world):
        super().__init__(positionX, positionY, world)
        self.strength = 9
        self.initiative = 5

    def spawn(self, x, y, world):
        self.world.addOrganism(Wolf(x, y, world))