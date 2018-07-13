from Animal import Animal


class Fox(Animal):
    def __init__(self, positionX, positionY, world):
        super().__init__(positionX, positionY, world)
        self.strength = 3
        self.initiative = 7

    def action(self):
        super().action()
        i = self.world.checkForCollision(self)
        if i != -1 and self.world.organisms[i].strength > self.strength:
            self.goBack(self)

    def spawn(self, x, y, world):
        self.world.addOrganism(Fox(x, y, world))
