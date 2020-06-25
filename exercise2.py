from tkinter import *
def apply():
    print("Applied")
    root.geometry(f"{width_value.get()}x{height_value.get()}")
root = Tk()
root.title("GUI Window")
root.geometry("500x300")
heading=Label(root,text="Reset Window",font="lucida 22 bold italic",bg="black",fg="white")
heading.grid(row=0,column=3)
width = Label(root,text="Enter The Width: ",font="comicsans 14 italic"
              ,pady=18,padx=18)
height = Label(root,text="Enter The Height: ",font="comicsans 14 italic"
               ,pady=18,padx=18)
width.grid(row=1,column=2)
height.grid(row=2,column=2)
width_value=StringVar()
height_value=StringVar()
widthentry = Entry(root,textvariable=width_value)
widthentry.grid(row=1,column=3)
heightentry=Entry(root,textvariable=height_value)
heightentry.grid(row=2,column=3)
b1=Button(root,text="Apply",command=apply,font="comicsans 14 bold",bg="black",fg="white")
b1.grid(row=3,column=3)
root.mainloop()