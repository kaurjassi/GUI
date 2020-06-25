from tkinter import *
class GUI(Tk):
    # CONSTRUCTOR
    def __init__(self):
        super().__init__();
        self.title("My Menu")
        self.geometry("500x300")
        # MENU
    def menu1(self):
        self.filemenu=Menu(self)
        self.m1 = Menu(self.filemenu, tearoff=0, activebackground="blue", selectcolor="red")
        self.m1.add_command(label="New")
        self.m1.add_command(label="Open")
        self.m1.add_command(label="Save")
        self.config(menu=self.filemenu)
        self.filemenu.add_cascade(label="file", menu=self.m1)
    # SCROLLBAR
    def scrollbar1(self):
        self.scrollbar = Scrollbar(self)
        self.scrollbar.pack(fill=Y,side=RIGHT)
    # FOr ADDING TEXT
    def textadd(self):
        self.text = Text(self, yscrollcommand=self.scrollbar.set, font="comicsans 15 italic")
        self.text.pack(fill=BOTH)
        self.scrollbar.config(command=self.text.yview)

if __name__ == '__main__':
    window = GUI()
    window.menu1()
    window.scrollbar1()
    window.textadd()
    window.mainloop()


