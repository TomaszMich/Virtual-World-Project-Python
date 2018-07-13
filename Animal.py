from random import randint

from Organism import Organism


class Animal(Organism):
    def __init__(self, positionX, positionY, world):
        super().__init__(positionX, positionY, world)

    def action(self):
        direction = randint(0, 3)
        i = self.world.checkForCollision(self)
        if i != -1:
            if self.collision(self.world.organisms[i]):
                self.movement(direction)
        else:
            self.movement(direction)

    def collision(self, org):
        if type(self) is type(org):
            self.goBack(org)
            self.reproduce()
            return False
        else:
            return super().collision(org)

    def goBack(self, org):
        where = org.movedTo
        if where == 0:
            org.movement(1)
        if where == 1:
            org.movement(0)
        if where == 2:
            org.movement(3)
        if where == 3:
            org.movement(2)

    def movement(self, direction):
        x = self.positionX
        y = self.positionY
        fail = 0

        while x == self.positionX and y == self.positionY and fail < 4:
            if direction == 0 and self.positionY != 0 and self.positionY != self.step - 1:
                self.positionY -= self.step
                self.movedTo = 0
            elif direction == 1 and self.positionY != self.world.sizeY - 1 and self.positionY != self.world.sizeY - self.step:
                self.positionY += self.step
                self.movedTo = 1
            elif direction == 2 and self.positionX != 0 and self.positionX != self.step - 1:
                self.positionX -= self.step
                self.movedTo = 2
            elif direction == 3 and self.positionX != self.world.sizeX - 1 and self.positionX != self.world.sizeX - self.step:
                self.positionX += self.step
                self.movedTo = 3
            elif direction == -1:
                break
            fail += 1
            direction = (direction + 1) % 4

    def movementOnFree(self):
        direction = randint(0, 3)
        x = self.positionX
        y = self.positionY
        fail = 0

        while x == self.positionX and y == self.positionY and fail < 4:
            if direction == 0 and self.positionY != 0 and self.positionY != self.step - 1 and not self.world.isThereOrganism(x, y - self.step):
                self.positionY -= self.step
                self.movedTo = 0
            elif direction == 1 and self.positionY != self.world.sizeY - 1 and self.positionY != self.world.sizeY - self.step and not self.world.isThereOrganism(x, y + self.step):
                self.positionY += self.step
                self.movedTo = 1
            elif direction == 2 and self.positionX != 0 and self.positionX != self.step - 1 and not self.world.isThereOrganism(x - self.step, y):
                self.positionX -= self.step
                self.movedTo = 2
            elif direction == 3 and self.positionX != self.world.sizeX - 1 and self.positionX != self.world.sizeX - self.step and not self.world.isThereOrganism(x + self.step, y):
                self.positionX += self.step
                self.movedTo = 3

            fail += 1
            direction = (direction + 1) % 4


