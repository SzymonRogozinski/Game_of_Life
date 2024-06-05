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
        if self.entry.get() is not '':
            iteration = int(self.entry.get())
            if iteration < 0 or iteration >= len(self.iterations):
                print("The iteration is out of range")
                return
            #print(self.iterations[iteration].plane)
            iter = []
            for row in self.iterations[iteration].plane:
                for cell in row:
                    if cell is True:
                        iter.append(1)
                    else:
                        iter.append(0)
            self.entry.delete(0, END)
            y = 0
            for i, life in enumerate(iter):
                #print(life)
                if life == 1:
                    color = 'black'
                else:
                    color = 'white'
                #print(i*self.weight, y*self.weight, (i+1)*self.weight, (y+1)*self.weight, sep=' ')
                self.canvas.create_rectangle((i%self.width)*self.weight, y*self.weight, (i%self.width+1)*self.weight, (y+1)*self.weight, outline=color, fill=color)
                if (i+1)%(self.width) == 0:
                    y = y + 1


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
    iters = []
    iters.append([1,1,1,1,1,1,1,1,1])
    iters.append([0,0,0,0,0,0,0,0,0])
    iters.append([1,0,1,0,1,0,1,0,1])
    iters.append([0,1,0,1,0,1,0,1,0])
    gui = Gui(3,3,iterations=iters)
    gui.display()