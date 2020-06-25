from tkinter import *
import tkinter.messagebox as tmsg
def order():
    tmsg.showinfo("Order Recieved",f"We have received your order as {var.get()}.\n"
                                   f"THANK YOU FOR ORDER WITH US.")
root = Tk()
root.title("Radiobutons")
root.geometry("500x400")
# radiobuttons
# for radiobuttons we make integer variable
# var = IntVar()
# set with 1
# radio=Radiobutton(root,text="Dosa",padx=14,variable=var,value=1).pack()
# radio=Radiobutton(root,text="Idaly",padx=14,variable=var,value=2).pack()
# radio=Radiobutton(root,text="Samosa",padx=14,variable=var,value=3).pack()
# radio=Radiobutton(root,text="Patties",padx=14,variable=var,value=4,pady=12).pack()
# var.set(1)
# Label(root,text="What would you like to have sir?",font="lucida 18 bold").pack()
# HOW TO RETRIVE THE VALUE
# Button(root,text="Order Now",command=order).pack()
# if we want to get the values in string then give the
# value attribute as a string like the text attribute.for this
# we also make a stringvar variable as intvar initial value bji deni hogi
var =StringVar()
var.set("radio")
Label(root,text="What would you like to have sir?",font="lucida 18 bold").pack()
# HOW TO RETRIVE THE VALUE
radio=Radiobutton(root,text="Dosa",padx=14,variable=var,value="Dosa").pack()
radio=Radiobutton(root,text="Idaly",padx=14,variable=var,value="Idaly").pack()
radio=Radiobutton(root,text="Samosa",padx=14,variable=var,value="Samosa").pack()
radio=Radiobutton(root,text="Patties",padx=14,variable=var,value="Patties",pady=12).pack()
Button(root,text="Order Now",command=order).pack()
root.mainloop()