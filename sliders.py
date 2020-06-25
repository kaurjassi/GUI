from tkinter import *
import tkinter.messagebox as tmsg
def getdollar():
    tmsg.showinfo("credited dollar",f"We have credited {myslider2.get()} dollars "
                                    f"in your account.\nTHANK YOU.")
root = Tk()
root.geometry("500x400")
root.title("sliders")
# for vertical slider
# myslider = Scale(root,from_=0,to=100)
# myslider.pack()
# for horizontal slider
# how to excess value with thw help of slider
Label(root,text="how many dollars you want??").pack()
myslider2=Scale(root,activebackground="red",width=20,state="active",sliderlength=10,from_=0,to=200,orient=HORIZONTAL,resolution=10,troughcolor="blue",tickinterval=30,length=200,digits=2)
myslider2.pack()
Button(root,text="Get Dollars",command=getdollar).pack()
# how to access the slider with not 0 ,with 10
# change the from_ value= 10 ,that you want to give
# if we want that oue slider starts with 0 but initial value is 10 ,then
# make a set function
# myslider2.set(34)
# this value gives before pack the slider.
# if we want that the values are in particular interval then do like this
# give a option after slider tickinterval=5
# if we want to give the interval of 5

root.mainloop()
