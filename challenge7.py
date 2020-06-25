from tkinter import *
import tkinter.messagebox as tmsg
def submit():
    with open("file3.txt","a") as f:
        f.write(f"{myslider.get()}\n")
        tmsg.showinfo("Rating",f"You are rating {myslider.get()} with your experience.")
root=Tk()
root.title("Rate Us")
root.geometry("400x200")
Label(root,text="Please Rate To Our GUI?",font="lucida 15 italic bold").pack()
myslider=Scale(root,from_=0,to=10,orient=HORIZONTAL,sliderlength=8
               ,activebackground="black",tickinterval=1,length=200)
myslider.pack()
Button(root,text="Submit",font="lucida 15 italic bold",bg="black",fg="white",command=submit).pack()
root.mainloop()