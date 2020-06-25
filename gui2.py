# images with tkinter
# image is also a label with which user is not interacted.
# tkinter always take a photo /image with extension 'png' only...
from tkinter import *
from PIL import Image , ImageTk
root = Tk()
root_label = root.geometry('1200x900')
# photo = PhotoImage(file = 'cute_Baby.png')
image = Image.open("cute baby2.jpg")
photo = ImageTk.PhotoImage(image)

photo_label = Label(image = photo)
photo_label.pack()

# how to change a image of 'jpg' extension used 







root.mainloop() 