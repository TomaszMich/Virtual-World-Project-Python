from random import randint

from Animal import Animal


class Turtle(Animal):
    def __init__(self, positionX, positionY, world):
        super().__init__(positionX, positionY, world)
        self.strength = 2
        self.initiative = 1

    def action(self):
        super().action()
        if randint(0, 100) <= 75:
            self.goBack(self)

    def collision(self, org):
        if org.strength < 5:
            self.goBack(org)
            return True
        else:
            return super().collision(org)

    def spawn(self, x, y, world):
        self.world.addOrganism(Turtle(x, y, world))
