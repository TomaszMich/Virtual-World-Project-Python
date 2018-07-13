from random import randint

from Organism import Organism


class Plant(Organism):
    def __init__(self, positionX, positionY, world):
        super().__init__(positionX, positionY, world)
        self.initiative = 0

    def action(self):
        i = self.world.checkForCollision(self)
        if (i != -1 and self.collision(self.world.organisms[i])) or i == -1:
            if randint(0, 100) < 5:  # plants have 5% chance to reproduce
                self.reproduce()

    def movement(self, direction):
        pass
