from abc import ABC
from random import randint


class Organism(ABC):
    def __init__(self, positionX, positionY, world):
        self.positionX = positionX
        self.positionY = positionY
        self.world = world
        self.age = 0
        self.movedTo = -1
        self.step = 1

    def action(self):
        pass

    def movement(self, direction):
        pass

    def spawn(self, x, y, world):
        pass

    def draw(self):
        self.world.drawOrganism(self.positionX, self.positionY, type(self).__name__)

    def collision(self, org):
        if self.strength > org.strength:
            self.world.removeOrganism(org)
            return True
        else:
            self.world.removeOrganism(self)
            return False

    def reproduce(self):
        place = randint(0, 3)
        x = self.positionX
        y = self.positionY
        fail = 0

        while x == self.positionX and y == self.positionY and fail < 4:
            if place == 0 and not self.world.isThereOrganism(x, y - 1) and y != 0:
                y = y - 1
            elif place == 1 and not self.world.isThereOrganism(x, y + 1) and y != self.world.sizeY - 1:
                y = y + 1
            elif place == 2 and not self.world.isThereOrganism(x - 1, y) and x != 0:
                x = x - 1
            elif place == 3 and not self.world.isThereOrganism(x + 1, y) and x != self.world.sizeX - 1:
                x = x + 1
            fail = fail + 1
            place = (place + 1) % 4

        if fail <= 4:
            self.spawn(x, y, self.world)
            self.world.infoBoard("Created new "+type(self).__name__+".")

    def increaseAge(self):
        self.age = self.age + 1

    def strengthPlus3(self):
        self.strength = self.strength + 3
