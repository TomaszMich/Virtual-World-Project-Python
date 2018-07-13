from Plant import Plant


class DeadlyNightshade(Plant):
    def __init__(self, positionX, positionY, world):
        super().__init__(positionX, positionY, world)
        self.strength = 99

    def collision(self, org):
        self.world.removeOrganism(org)
        return True

    def spawn(self, x, y, world):
        self.world.addOrganism(DeadlyNightshade(x, y, world))
