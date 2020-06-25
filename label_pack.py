from tkinter import *
root = Tk()
root.geometry('474x243')
root.title('My First GUI')
# IMPORTANT ATTRIBUTES OF LABEL
title_label = Label(text= "THIS IS MY FIRST GUI.WE READ HERE ABOUT\n THE ATTIBUTES OF LABEL CLASS....."
                    ,bg='red',fg='white',font=('comicsans',10,'bold')
                    ,borderwidth=5,relief=RAISED,padx=12,pady=12)
# IMPORTANT ATTRIBUTES OF PACK
title_label.pack(side= BOTTOM,anchor='nw',fill= X,padx=13,pady=23)
root.mainloop()