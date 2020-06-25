from tkinter import *
# different functions for different buttons
def fun1():
      print("THIS IS FUNCTION 1.")
def fun2():
      print("THIS IS FUNCTION 2.")
def fun3():
      print("THIS IS FUNCTION 3.")
def fun4():
      print("THIS IS FUNCTION 4.")
root = Tk()
root.geometry("555x320")
# frame for label
f1 = Frame(root, bg = "grey", borderwidth = 5, relief = RAISED, pady = 20)
f1.pack(anchor = "center" , fill = X)
# frame for buttons
f2 = Frame(root , borderwidth = 5 , relief = GROOVE ,pady = 15)
f2.pack(anchor = "center", fill= X)
# label
l1 = Label(f1,text="WELCOME TO PYCHARM",font="helvetica 18 bold",fg="red")
l1.pack(anchor = "center" )
# button 1
b1 = Button(f2,text ="Submit1",bg = "black",fg="red",font ="comicsans 14 bold",command=fun1)
b1.pack(side=LEFT , anchor= "center",pady = 10, padx=120)
# for button2
b2 = Button(f2,text ="Submit2",bg = "black",fg="red",font ="comicsans 14 bold",command=fun2)
b2.pack(side =LEFT,anchor= "center",pady = 10, padx=120)
# for button 3
b3 = Button(f2,text ="Submit3",bg = "black",fg="red",font ="comicsans 14 bold",command=fun3)
b3.pack(side =LEFT,anchor= "center",pady = 10, padx=120)
# for button 4
b4 = Button(f2,text ="Submit4",bg = "black",fg="red",font ="comicsans 14 bold",command=fun4)
b4.pack(side =LEFT,anchor= "center", pady = 10, padx=120)



root.mainloop()
