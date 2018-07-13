from Plant import Plant


class Hogweed(Plant):
    def __init__(self, positionX, positionY, world):
        super().__init__(positionX, positionY, world)
        self.strength = 10

    def action(self):
        up = self.world.findOrganism(self.positionX, self.positionY - 1)
        down = self.world.findOrganism(self.positionX, self.positionY + 1)
        left = self.world.findOrganism(self.positionX - 1, self.positionY)
        right = self.world.findOrganism(self.positionX + 1, self.positionY)

        if up != -1 and type(self.world.organisms[up]).__name__ != 'CSheep':
            self.world.removeOrganism(self.world.organisms[up])
        if down != -1 and type(self.world.organisms[down]).__name__ != 'CSheep':
            self.world.removeOrganism(self.world.organisms[down])
        if left != -1 and type(self.world.organisms[left]).__name__ != 'CSheep':
            self.world.removeOrganism(self.world.organisms[left])
        if right != -1 and type(self.world.organisms[right]).__name__ != 'CSheep':
            self.world.removeOrganism(self.world.organisms[right])

        super().action()

    def collision(self, org):
        if type(org).__name__ == 'CSheep':
            self.world.removeOrganism(self)
            return False
        else:
            self.world.removeOrganism(org)
            return True

    def spawn(self, x, y, world):
        self.world.addOrganism(Hogweed(x, y, world))
