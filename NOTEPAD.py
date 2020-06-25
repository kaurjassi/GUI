from tkinter import *
import tkinter.messagebox as tmsg
import os
from tkinter.filedialog import asksaveasfilename,askopenfilename




def newFile():
    global file
    root.title("Untitled - Notepad")
    file= None
    TextArea.delete(1.0,END)
    # from ist line 0 column to the end

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",filetypes=
    [("All Files","*.*"),("Text Documents","*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + "- Notepad")
        TextArea.delete(1.0,END)
        f= open(file,"r")
        TextArea.insert(1.0,END)
        f.close()

def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt",defaultextensions=".txt",
                                filetypes=([("All Files","*.*"),
                                            ("Text Documents","*.txt")]))
        if file == "":
            file = None
        else:
            f= open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()

            root.title(os.path.basename(file) + "- Notepad")
    else:
        f=open(file,"w")
        f.write(TextArea.get(1.0,END))
        f.close()


def quitapp():
    root.destroy()

def Cut():
    TextArea.event_generate("<<Cut>>")

def Copy():
    TextArea.event_generate("<<Copy>>")


def Paste():
    TextArea.event_generate("<<Paste>>")

def Help():
    tmsg.showinfo("Help","This Code is run by Jaswinder")


if __name__ == '__main__':
    # basic tkinter setup
    root = Tk()
    root.title("Untitled-Notepad")
    root.geometry("644x788")
    root.wm_iconbitmap("notepad.ico")


    # Add textarea
    TextArea = Text(root,font="lucida 15")
    file = None    #(this targets the open file.)
    TextArea.pack(fill=BOTH,expand=True)
      # for menubars
    MenuBar = Menu(root)
    FileMenu = Menu(MenuBar,tearoff=0)
    # to open new file
    FileMenu.add_command(label="New",command=newFile)
     # to open the file
    FileMenu.add_command(label="Open",command=openFile)
    # to save file
    FileMenu.add_command(label="Save",command=saveFile)
    # add separator
    FileMenu.add_separator()
    # to exit
    FileMenu.add_command(label="Exit",command=quitapp)
    MenuBar.add_cascade(label="File",menu=FileMenu)
    # for making edit
    EditMenu = Menu(MenuBar,tearoff=0)
    EditMenu.add_command(label="Cut",command=Cut)
    EditMenu.add_command(label="Copy",command=Copy)
    EditMenu.add_command(label="Paste",command=Paste)
    MenuBar.add_cascade(label= "Edit",menu=EditMenu)
    # for help
    HelpMenu = Menu(MenuBar,tearoff=0)
    HelpMenu.add_command(label="Help",command=Help)
    MenuBar.add_cascade(label="Help",menu=HelpMenu)
    root.config(menu=MenuBar)

    # scrollbar
    Scroll = Scrollbar(TextArea)
    Scroll.pack(fill=Y,side=RIGHT)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)

    root.mainloop()