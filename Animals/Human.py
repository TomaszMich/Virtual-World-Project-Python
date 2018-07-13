from Animal import Animal


class Human(Animal):
    def __init__(self, positionX, positionY, world):
        super().__init__(positionX, positionY, world)
        self.strength = 5
        self.initiative = 4

    def action(self):
        direction = self.world.humanDirection
        i = self.world.checkForCollision(self)
        if i != -1:
            if self.collision(self.world.organisms[i]):
                self.movement(direction)
        else:
            self.movement(direction)
        self.world.humanDirection = -1

    def collision(self, org):
        if 0 <= self.world.ability < 5:
            if self.strength > org.strength:
                self.world.removeOrganism(org)
                return True
            else:
                self.movementOnFree()
                return False
        else:
            return super().collision(org)


