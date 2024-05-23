from tkinter import *
from tkinter import ttk


class Gui(object):

    def __init__(self, width, height, iterations) -> None:
        if width > 640 or height > 350:
            raise 
        self.width = width
        self.height = height
        self.iterations = iterations
        if self.height < 5 and self.width < 7:
            self.weight = 160
        elif self.height < 10 and self.width < 14:
            self.weight = 80
        elif self.height < 20 and self.width < 28:
            self.weight = 40
        elif self.height < 40 and self.width < 56:
            self.weight = 20
        elif self.height < 80 and self.width < 112:
            self.weight = 10
        elif self.height < 160 and self.width < 224:
            self.weight = 5
        else:
            self.weight = 2



    def draw(self):
        print("Hello world")



    def display(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, bg='black', height=self.height*self.weight, width=self.width*self.weight)
        self.canvas.pack(padx=20, pady=5)
        self.entry=Entry(self.root, width=40)
        self.entry.pack(pady=10)
        self.button=Button(self.root, text="Wyświetl", command=self.draw)
        self.button.pack(pady=10)
        self.root.update()
        self.root.mainloop()



if __name__=="__main__":
    gui = Gui(400,300,[])
    gui.display()