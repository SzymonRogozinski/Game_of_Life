from tkinter import *
from tkinter import ttk


class Gui(object):

    def __init__(self, width, height, iterations) -> None:
        if width > 640 or height > 400:
            raise 
        self.width = width
        self.height = height
        self.iterations = iterations
        if self.height < 5 and self.width < 8:
            self.weight = 160
        elif self.height < 10 and self.width < 16:
            self.weight = 80
        elif self.height < 20 and self.width < 32:
            self.weight = 40
        elif self.height < 40 and self.width < 64:
            self.weight = 20
        elif self.height < 80 and self.width < 128:
            self.weight = 10
        elif self.height < 160 and self.width < 256:
            self.weight = 5
        else:
            self.weight = 2


    def display(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, bg='black', height=self.height*self.weight, width=self.width*self.weight)
        self.canvas.pack()
        self.root.update()
        self.root.mainloop()


if __name__=="__main__":
    gui = Gui(400,400,[])
    gui.display()