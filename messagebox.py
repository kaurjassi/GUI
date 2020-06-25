from tkinter import *
import tkinter.messagebox as tmsg
def myfunc():
    print("this is menu")
def help():
    print("May i help you....")
    a=tmsg.showinfo("help,i wll help you with this gui..")
    # a has return value "ok".sometimes we need the return value..

def rate():
   value=tmsg.askquestion("was your experience good???","you used this gui experiene..")
   print(value)
def new():
    a=tmsg.showwarning("Do Not Use More...","This is dangerous ")
def new2():
    b = tmsg._show("hello","what is your name???")
def func2():
    c = tmsg.showerror("Error","Please Check Again.")
root = Tk()
root.title("GUI MENUS")
root.geometry("500x400")
# use this to make unknown
# mymenu = Menu(root)
# mymenu.add_command(label="file",command=myfunc)
# mymenu.add_command(label="Exit",command=quit)
# root.config(menu=mymenu)
Filemenu=Menu(root,font="comicsans 18 bold")
# tearoff =0 is that option which helps us to not to tear off the window
m1=Menu(Filemenu,tearoff=0)
m1.add_command(label="New",command=myfunc,font="comicsans 10 normal")
m1.add_command(label="Open",command=myfunc,font="comicsans 10 normal")
m1.add_command(label="Save",command=myfunc,font="comicsans 10 normal")
# separator addds a line between the previous and next submenu
m1.add_separator()
m1.add_command(label="Save As",command=myfunc,font="comicsans 10 normal")
root.config(menu=Filemenu)
# add_cascade is used to makw the main option name
Filemenu.add_cascade(label="file",menu=m1,font="lucida 18 bold")
# In menus and submenus no pack. In this config used instead of pack,grid

# for next option "edit"
m2=Menu(Filemenu,tearoff=0)
m2.add_command(label="Cut",command=myfunc,font="comicsans 10 normal")
m2.add_command(label="Copy",command=myfunc,font="comicsans 10 normal")
m2.add_command(label="Paste",command=myfunc,font="comicsans 10 normal")
# separator addds a line between the previous and next submenu
m2.add_separator()
m2.add_command(label="Find",command=myfunc,font="comicsans 10 normal")
root.config(menu=Filemenu)
Filemenu.add_cascade(label="Edit",menu=m2,font="comicsans 18 bold")
# m3

m3=Menu(Filemenu,tearoff=0)
m3.add_command(label="help",command=help,font="comicsans 10 normal")
m3.add_command(label="About",command=func2,font="comicsans 10 normal")
m3.add_command(label="Rate Us",command=rate,font="comicsans 10 normal")
m3.add_command(label="Rename",command=new,font="comicsans 10 normal")
m3.add_command(label="Use",command=new2,font="comicsans 10 normal")
Filemenu.add_cascade(label="help",menu=m3)

root.config(menu=Filemenu)
root.mainloop()












































