from Plant import Plant


class Grass(Plant):
    def __init__(self, positionX, positionY, world):
        super().__init__(positionX, positionY, world)
        self.strength = 0

    def spawn(self, x, y, world):
        self.world.addOrganism(Grass(x, y, world))
