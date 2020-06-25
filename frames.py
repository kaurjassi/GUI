from tkinter import *
root = Tk()
root.geometry('855x355')
f1 = Frame(root,bg='grey',borderwidth=10,relief=SUNKEN)
f1.pack(side = LEFT, fill =Y )
l1 = Label(f1,text = ' welcome to pycharm',fg='red' , font = "helvetica 10 bold")
l1.pack(anchor= "w")
f2 = Frame(root, bg = "black",borderwidth = 8 , relief= GROOVE)
f2.pack(side = TOP , fill=X)
l2 =Label(f2,text= "hello world, this is pycharm" ,font= ("times new roman", 15 ,  "bold"), fg = "green")
l2.pack()




root.mainloop()