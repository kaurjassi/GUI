from tkinter import *
from PIL import Image, ImageTk
import os
root = Tk()
root.geometry('474x277')
root_label = Label(text = "IMAGES")
root_label.pack()
photo = Image.open('F:\cute baby2.jpg')
photo_1 = ImageTk.PhotoImage(photo)
photolabel = Label(image = photo_1)
photolabel.pack()
photo1 = Image.open('F:\cute_baby.png')
photo_2 = ImageTk.PhotoImage(photo1)
photo_label = Label(image = photo_2)
photo_label.pack()
root.mainloop()