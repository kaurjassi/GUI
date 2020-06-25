from tkinter import *

root = Tk()
# THIS REPRESENTS THE SIZE OF WINDOW WHEN WE OPEN IT.THE WINDOW SEES IN THE GEOMETRY. 
root.geometry('799x430')
# MAXIMUM SIZE OF WINDOW 
root.maxsize(1044,942)
# MINIMUM SIZE OF WINDOW
root.minsize(200,100)
# MAKING LABBLS : USER DID NOT INTERACT WITH LABEL
main = Label(text ='WHAT IS YOUR NAME')
# THREE METHODS TO DO THE PACKING 
# 1. pack()
# 2. grid()
# 3.
main.pack()


root.mainloop()