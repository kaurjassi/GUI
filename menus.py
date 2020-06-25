from tkinter import *
def myfunc():
    print("this is menu")
root = Tk()
root.title("GUI MENUS")
root.geometry("500x400")
# use this to make unknown
# mymenu = Menu(root)
# mymenu.add_command(label="file",command=myfunc)
# mymenu.add_command(label="Exit",command=quit)
# root.config(menu=mymenu)
Filemenu=Menu(root)
# tearoff =0 is that option which helps us to not to tear off the window
m1=Menu(Filemenu,tearoff=0,activebackground="blue",selectcolor="red")
m1.add_command(label="New",command=myfunc)
m1.add_command(label="Open",command=myfunc)
m1.add_command(label="Save",command=myfunc)
# separator addds a line between the previous and next submenu
m1.add_separator()
m1.add_command(label="Save As",command=myfunc)
root.config(menu=Filemenu)
# add_cascade is used to makw the main option name
Filemenu.add_cascade(label="file",menu=m1)
# In menus and submenus no pack. In this config used instead of pack,grid

# for next option "edit"
m2=Menu(Filemenu,tearoff=0)
m2.add_command(label="Cut",command=myfunc)
m2.add_command(label="Copy",command=myfunc)
m2.add_command(label="Paste",command=myfunc)
# separator addds a line between the previous and next submenu
m2.add_separator()
m2.add_command(label="Find",command=myfunc)
root.config(menu=Filemenu)
Filemenu.add_cascade(label="Edit",menu=m2)


root.mainloop()
