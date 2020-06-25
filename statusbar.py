from tkinter import *
root = Tk()
root.title("status bar")
root.geometry("500x200")
# make a function to update the status bar
def upload():
    statusvar.set("busy.....")
    # update function is used to update our data ...busy tb chalega jb hm update function lo use krege..
    sbar.update()
    import time
    time.sleep(2)
    statusvar.set("Ready Now")
# make a stauts bar : there is no status bar in tkinter .but we are try to make a status bar
# statsus bar is the downward part of any gui and any website.
statusvar=StringVar()
statusvar.set("Ready")
sbar=Label(root,textvariable=statusvar,relief=SUNKEN,
           anchor="w",padx=20,font="lucida 12 italic bold")
sbar.pack(fill=X,side=BOTTOM)
Button(root,text="upload",font="lucida 20 italic normal",command=upload).pack()



root.mainloop()