from random import randint

from Plant import Plant


class Dandelion(Plant):
    def __init__(self, positionX, positionY, world):
        super().__init__(positionX, positionY, world)
        self.strength = 0

    def action(self):
        super().action()
        for i in range(2):
            if randint(0, 100) < 5:
                self.reproduce()

    def spawn(self, x, y, world):
        self.world.addOrganism(Dandelion(x, y, world))
