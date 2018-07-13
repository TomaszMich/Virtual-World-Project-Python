from tkinter import *

from random import randint
from Animals.Antelope import Antelope
from Animals.CSheep import CSheep
from Animals.Fox import Fox
from Animals.Human import Human
from Animals.Sheep import Sheep
from Animals.Turtle import Turtle
from Animals.Wolf import Wolf
from Plants.Dandelion import Dandelion
from Plants.DeadlyNightshade import DeadlyNightshade
from Plants.Grass import Grass
from Plants.Guarana import Guarana
from Plants.Hogweed import Hogweed


class World:
    def __init__(self, sizeX, sizeY):
        self.organisms = list(())
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.humanDirection = -1
        self.ability = -1
        self.lines = 0
        self.master = Tk()
        self.master.minsize(width=self.sizeY*30 + 250, height=self.sizeX*30 + 50)
        self.frame = Frame(self.master, height=self.sizeY * 30, width=self.sizeX * 30, background='gray')
        self.info = Frame(self.master,  height=self.sizeY * 30, width=200, background='gray')
        self.createOrganisms()
        self.createWindow()

    def createWindow(self):
        self.frame.bind('<Button-1>', self.add)
        self.frame.pack()
        self.frame.place(x=10, y=10)
        self.info.pack()
        self.info.place(x=self.sizeX*30 + 20, y=10)
        button = Button(self.master, text="Make tur", command=self.executeTur)
        button.pack()
        button.place(x=10, y=self.sizeY*30 + 20)
        self.drawAllOrganism()
        self.master.bind('<Left>', self.leftKey)
        self.master.bind('<Right>', self.rightKey)
        self.master.bind('<Up>', self.upKey)
        self.master.bind('<Down>', self.downKey)
        self.master.bind('<a>', self.aKey)
        self.master.bind('<space>', self.spaceKey)
        menubar = Menu(self.master)
        gamemenu = Menu(menubar, tearoff=0)
        gamemenu.add_command(label="Save", command=self.saveGame)
        gamemenu.add_command(label="Load", command=self.loadGame)
        menubar.add_cascade(label="Game", menu=gamemenu)
        self.master.config(menu=menubar)
        self.master.update()

    def saveGame(self):
        save = open("save.txt", "w")
        save.write(str(self.sizeX)+"\n"+str(self.sizeY)+"\n"+str(len(self.organisms)))
        for x in self.organisms:
            name = type(x).__name__
            save.write("\n"+name+"\n"+str(x.positionX)+"\n"+str(x.positionY)+"\n"+str(x.strength)+"\n"+str(x.movedTo)+"\n"+str(x.age))
        save.close()
        self.lines = 0
        self.clearInfo()
        self.infoBoard("Your game has been saved")

    def loadGame(self):
        save = open("save.txt", "r")
        self.organisms.clear()
        self.sizeX = int(save.readline())
        self.sizeY = int(save.readline())
        quantity = int(save.readline())

        for i in range(quantity):
            name = str(save.readline().rstrip('\n'))
            posX = int(save.readline())
            posY = int(save.readline())
            strn = int(save.readline())
            mvd = int(save.readline())
            age = int(save.readline())
            self.loadOrganism(name, posX, posY, strn, mvd, age)

        save.close()
        self.master.destroy()
        self.master = Tk()
        self.master.minsize(width=self.sizeY*30 + 250, height=self.sizeX*30 + 50)
        self.frame = Frame(self.master, height=self.sizeY * 30, width=self.sizeX * 30, background='gray')
        self.info = Frame(self.master,  height=self.sizeY * 30, width=200, background='gray')
        self.createWindow()
        self.lines = 0
        self.drawAllOrganism()
        self.infoBoard("Your game has been loaded")

    def add(self, event):
        x = int(event.x / 30)
        y = int(event.y / 30)
        if not self.isThereOrganism(x, y):
            self.addDialog(x, y)

    def addDialog(self, x, y):
        window = Tk()
        window.minsize(width=100, height=100)
        entry = Entry(window)
        entry.pack()
        submit = Button(window, text="Submit", command=lambda: self.submit(entry, x, y))
        submit.pack(side=BOTTOM)

    def submit(self, entry, x, y):
        name = entry.get()
        self.addOrganismByName(name, x, y)
        self.drawOrganism(x, y, name)
        self.frame.update()

    def drawOrganism(self, posX, posY, name):
        img = PhotoImage(file="Img/"+name+".png")
        label = Label(self.frame, image=img)
        label.img = img
        label.pack()
        label.place(height=30, width=30, x=30*posX, y=30*posY)

    def drawAllOrganism(self):
        for i in range(len(self.organisms) - 1):
            self.organisms[i].draw()

    def executeTur(self):
        self.lines = 0
        self.clearInfo()
        self.organisms.sort(reverse=True, key=lambda x: (x.initiative, x.age))

        for x in self.organisms:
            if x.age != 0:
                x.action()

        self.increaseAges()
        self.clearFrame()
        self.drawAllOrganism()
        self.frame.update()
        if self.ability >= 0:
            if self.ability < 5:
                self.infoBoard("Ability is on")
            self.ability += 1
        if self.ability == 10:
            self.ability = -1

    def infoBoard(self, message):
        if self.lines < self.sizeY:
            label = Label(self.info, text=message)
            label.pack()
            label.place(y=self.lines*30)
            self.info.update()
            self.lines += 1

    def increaseAges(self):
        for i in range(0, len(self.organisms) - 1):
            self.organisms[i].increaseAge()

    def clearFrame(self):
        self.frame.destroy()
        self.frame = Frame(self.master, height=self.sizeY * 30, width=self.sizeX * 30, background='gray')
        self.frame.pack()
        self.frame.place(x=10, y=10)

    def clearInfo(self):
        self.info.destroy()
        self.info = Frame(self.master,  height=self.sizeY * 30, width=200, background='gray')
        self.info.pack()
        self.info.place(x=self.sizeX*30 + 20, y=10)

    def addOrganism(self, org):
        self.organisms.append(org)

    def removeOrganism(self, org):
        self.infoBoard(type(org).__name__+" died.")
        self.organisms.remove(org)

    def isThereOrganism(self, x, y):
        for i in range(0, len(self.organisms) - 1):
            if self.organisms[i].positionX == x and self.organisms[i].positionY == y:
                return True
        return False

    def findOrganism(self, x, y):
        for i in range(0, len(self.organisms) - 1):
            if self.organisms[i].positionX == x and self.organisms[i].positionY == y:
                return i
        return -1

    def checkForCollision(self, org):
        for i in range(0, len(self.organisms) - 1):
            if self.organisms[i].positionX == org.positionX and self.organisms[i].positionY == org.positionY and self.organisms[i] != org:
                return i
        return -1

    def generateXandY(self):
        coordinates = [randint(0, self.sizeX - 1), randint(0, self.sizeY - 1)]
        while self.isThereOrganism(coordinates[0], coordinates[1]):
            coordinates[0] = randint(0, self.sizeX - 1)
            coordinates[1] = randint(0, self.sizeY - 1)
        return coordinates

    def loadOrganism(self, name, posX, posY, strn, mvd, age):
        temp = Grass(posX, posY, self)
        if name == "Antelope":
            temp = Antelope(posX, posY, self)
        elif name == "CSheep":
            temp = CSheep(posX, posY, self)
        elif name == "Fox":
            temp = Fox(posX, posY, self)
        elif name == "Human":
            temp = Human(posX, posY, self)
        elif name == "Sheep":
            temp = Sheep(posX, posY, self)
        elif name == "Turtle":
            temp = Turtle(posX, posY, self)
        elif name == "Wolf":
            temp = Wolf(posX, posY, self)
        elif name == "Dandelion":
            temp = Dandelion(posX, posY, self)
        elif name == "DeadlyNightshade":
            temp = DeadlyNightshade(posX, posY, self)
        elif name == "Grass":
            temp = Grass(posX, posY, self)
        elif name == "Guarana":
            temp = Guarana(posX, posY, self)
        elif name == "Hogweed":
            temp = Hogweed(posX, posY, self)

        temp.age = age
        temp.strength = strn
        temp.movedTo = mvd
        self.organisms.append(temp)

    def fill(self):
        return 0.12 * self.sizeX * self.sizeY

    def createOrganisms(self):
        a = self.generateXandY()
        count = 0
        typ = 0
        num = 0
        self.addOrganism(Human(a[0], a[1], self))
        while count < self.fill():
            a = self.generateXandY()
            if num >= 22:
                typ = randint(0, 10)

            if typ == 0:
                self.addOrganism(Antelope(a[0], a[1], self))
            elif typ == 1:
                self.addOrganism(CSheep(a[0], a[1], self))
            elif typ == 2:
                self.addOrganism(Fox(a[0], a[1], self))
            elif typ == 3:
                self.addOrganism(Sheep(a[0], a[1], self))
            elif typ == 4:
                self.addOrganism(Turtle(a[0], a[1], self))
            elif typ == 5:
                self.addOrganism(Wolf(a[0], a[0], self))
            elif typ == 6:
                self.addOrganism(Dandelion(a[0], a[1], self))
            elif typ == 7:
                self.addOrganism(DeadlyNightshade(a[0], a[1], self))
            elif typ == 8:
                self.addOrganism(Grass(a[0], a[1], self))
            elif typ == 9:
                self.addOrganism(Guarana(a[0], a[1], self))
            elif typ == 10:
                self.addOrganism(Hogweed(a[0], a[1], self))

            count += 1
            if num < 22:
                typ = (typ + 1) % 11
                num += 1
        for i in range(len(self.organisms) - 1):
            self.organisms[i].increaseAge()

    def addOrganismByName(self, name, posX, posY):
        temp = Grass(posX, posY, self)
        if name == "Antelope":
            temp = Antelope(posX, posY, self)
        elif name == "CSheep":
            temp = CSheep(posX, posY, self)
        elif name == "Fox":
            temp = Fox(posX, posY, self)
        elif name == "Human":
            temp = Human(posX, posY, self)
        elif name == "Sheep":
            temp = Sheep(posX, posY, self)
        elif name == "Turtle":
            temp = Turtle(posX, posY, self)
        elif name == "Wolf":
            temp = Wolf(posX, posY, self)
        elif name == "Dandelion":
            temp = Dandelion(posX, posY, self)
        elif name == "DeadlyNightshade":
            temp = DeadlyNightshade(posX, posY, self)
        elif name == "Grass":
            temp = Grass(posX, posY, self)
        elif name == "Guarana":
            temp = Guarana(posX, posY, self)
        elif name == "Hogweed":
            temp = Hogweed(posX, posY, self)
        self.organisms.append(temp)

    def aKey(self, event):
        if self.ability == -1:
            self.ability = 0

    def spaceKey(self, event):
        self.executeTur()

    def upKey(self, event):
        self.humanDirection = 0

    def downKey(self, event):
        self.humanDirection = 1

    def leftKey(self, event):
        self.humanDirection = 2

    def rightKey(self, event):
        self.humanDirection = 3
