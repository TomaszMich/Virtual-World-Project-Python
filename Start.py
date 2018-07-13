from tkinter import *

from World import World


class Start:
    def __init__(self):
        self.master = Tk()
        self.master.minsize(width=20, height=110)
        self.label = Label(self.master, text="Enter sizes X and Y: ")
        self.label.pack()
        self.lX = Label(self.master, text="X:")
        self.lX.pack(side=LEFT)
        self.enX = Entry(self.master)
        self.enX.pack(side=LEFT)
        self.lY = Label(self.master, text="Y:")
        self.lY.pack(side=LEFT)
        self.enY = Entry(self.master)
        self.enY.pack(side=LEFT)
        self.button = Button(self.master, text="Enter", command=self.enter)
        self.button.pack()
        self.button.place(x=90, y=80, width=100, height=30)

    def enter(self):
        sizeX = int(self.enX.get())
        sizeY = int(self.enY.get())
        self.master.destroy()
        if sizeX < 4 or sizeX > 50:
            sizeX = 16
        if sizeY < 4 or sizeY > 50:
            sizeY = 16
        World(sizeX, sizeY)
