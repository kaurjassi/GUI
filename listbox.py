from tkinter import *
def add():
    global i
    lbs.insert(ACTIVE,f"{i}")
    i+=1
i=0       #intial value
root = Tk()
root.title("Listbox")
root.geometry("500x400")
# list box = list box is a widget which displays the alternate list..
# blank list box and insert the items in it
lbs = Listbox(root)
lbs.pack()
lbs.insert(END,"First item in list box")
Button(root,text="Add item",command=add).pack()
root.mainloop()