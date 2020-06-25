# here we talk about oops .
# there is no need to oops but when our program is long.then oops
# helps  us to enhance the readability of your program.
# otherwise we also make a gui without oops.
from tkinter import *
class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("744x377")

    def status(self):
        self.var= StringVar()
        self.var.set("Ready")
        self.statusbar=Label(self,textvar=self.var,
                             relief=SUNKEN,anchor="w")
        self.statusbar.pack(side=BOTTOM,fill=X)

    def click(self):
        print(f"BUTTTON CLICKED")

    def create_button(self,inptext):
        Button(text=inptext,command=self.click).pack()


# HERE WE DEFINE THE METHODS WE NEED TO WRITE THIS WITH THE WINDOW....
if __name__ == '__main__':
    window=GUI()
    window.status()
    window.create_button("CLICK ME")

    window.mainloop()