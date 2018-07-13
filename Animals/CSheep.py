from random import randint

from Animal import Animal


class CSheep(Animal):
    def __init__(self, positionX, positionY, world):
        super().__init__(positionX, positionY, world)
        self.strength = 11
        self.initiative = 4
        self.hX = -1
        self.hY = -1

    def spawn(self, x, y, world):
        self.world.addOrganism(CSheep(x, y, world))

    def searchForHogweed(self):
        for x in self.world.organisms:
            if type(x).__name__ == 'Hogweed':
                self.hX = x.positionX
                self.hY = x.positionY
                break

    def action(self):
        self.searchForHogweed()
        if self.hX == -1 and self.hY == -1:
            super().action()
        else:
            if self.hY < self.positionY:
                direction = 0
            elif self.hY > self.positionY:
                direction = 1
            elif self.hX > self.positionX:
                direction = 3
            elif self.hX < self.positionX:
                direction = 2
            else:
                direction = randint(0, 3)

            i = self.world.checkForCollision(self)
            if i != -1:
                if self.collision(self.world.organisms[i]):
                    self.movement(direction)
            else:
                self.movement(direction)
            self.hX = -1
            self.hY = -1
