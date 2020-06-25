#  geometry= '733x434'
# Make a GUI TO DISLAY A WINDOW OF SIZE '733X434' AND WRITE A TEXT THAT 'WELCOME TO PYCHARM'

from tkinter import * 
root = Tk()
root.geometry('733x434')

root_Label = Label(text= 'WELCOME TO PYCHARM......',font=" helvetica 33 bold")
root_Label.pack()

root.mainloop() 