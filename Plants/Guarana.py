from Plant import Plant


class Guarana(Plant):
    def __init__(self, positionX, positionY, world):
        super().__init__(positionX, positionY, world)
        self.strength = 0

    def collision(self, org):
        org.strengthPlus3()
        return super().collision(org)

    def spawn(self, x, y, world):
        self.world.addOrganism(Guarana(x, y, world))
