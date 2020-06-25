from tkinter import *
from PIL import Image , ImageTk
root = Tk()
root.geometry('500x400')
root.title('My Newspaper')
root_label = Label(root, text='NEWSPAPER',bg='black',fg='white',font=('Applechancery', 15, 'bold'),borderwidth=5,relief = RIDGE)
root_label.pack(side=TOP,fill = X)
# FOR FIRST NEWS
f1 =Frame(root,borderwidth = 6 ,relief = GROOVE)
f1.pack(side=TOP, padx = 20)
# PHOTO
photo1 = Image.open('first.png')
photo_1 = ImageTk.PhotoImage(photo1)
Photo1_label = Label(f1, image = photo_1,borderwidth= 4, relief =RIDGE,padx = 15 , pady= 15)
Photo1_label.pack(side =LEFT)
# FOR TXT FILE
with open("first.txt") as f:
      data  = f.read()
      # label of text file
label1 = Label(f1,text = data,fg='black',font=('Applechancery', 15, 'bold'))
label1.pack(padx = 20 , pady = 30,side= RIGHT)
# FOR 2ND NEWS
# frame
f2 =Frame(root,borderwidth = 6 ,relief = GROOVE)
f2.pack()
# photo
photo2 = Image.open('2.png')
photo_2 = ImageTk.PhotoImage(photo2)
Photo2_label = Label(f2,image = photo_2,borderwidth= 4, relief =RIDGE,padx = 15 , pady= 15)
Photo2_label.pack(side = RIGHT) 
#  text file
with open("2.txt") as f:
      data2  = f.read()
      # label of text file
label2 = Label(f2 , text = data2,fg='black',font=('Applechancery', 15, 'bold'))
label2.pack(side = LEFT, padx = 20, pady = 30)


# photo3 = Image.open('3.png')
# photo_3 = ImageTk.PhotoImage(photo3)
# Photo3_label = Label(image = photo_3,borderwidth = 4 , relief = GROOVE, pady= 100 )
# Photo3_label.pack(anchor= 'w' , side =LEFT)
# label3 = Label(text= "This is image 3.", bg ='black',fg='white',font=('Applechancery', 15, 'bold'))
# label3.pack(anchor='ne',fill =X, padx = 15 , pady = 15)

# photo4 = Image.open('4.png')
# photo_4 = ImageTk.PhotoImage(photo4)
# Photo4_label = Label(image = photo_4)
# Photo4_label.pack(anchor= 'nw' , side =BOTTOM)



root.mainloop()