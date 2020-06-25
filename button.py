from tkinter import *
root = Tk()
def hello():
      print("Hello, This is a button")

root.geometry("555x222")
f1 = Frame(root, bg = "black" , borderwidth = 6, relief = RIDGE)
f1.pack(fill = Y,anchor = "nw")
b1 = Button(f1, text= "submit" , fg= "red", font= "helvetica 16 bold", command = hello)
b1.pack(fill = X, side = LEFT,padx= 26,pady= 20)

b2 = Button(f1, text= "submit" , fg= "red", font= "helvetica 16 bold", command = hello)
b2.pack(fill = X, side = LEFT,padx= 26,pady= 20)

b3 = Button(f1, text= "submit" , fg= "red", font= "helvetica 16 bold", command = hello)
b3.pack(fill = X, side = LEFT, padx=26,pady= 20)

b4 = Button(f1, text= "submit" , fg= "red", font= "helvetica 16 bold", command = hello)
b4.pack(fill = X, side = LEFT ,padx= 26,pady= 20)

b5 = Button(f1, text= "submit" , fg= "red", font= "helvetica 16 bold", command = hello)
b5.pack(fill = X, side = LEFT,padx= 26,pady= 20)
root.mainloop()