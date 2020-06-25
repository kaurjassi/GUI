from tkinter import *
root = Tk()
root.title("Calculator")
root.geometry("345x600")
root.wm_iconbitmap("calculator.ico")
def click(event):
    # how to capture the value
    global entryvalue
    text = event.widget.cget("text")
    if text == "=":
        if entryvalue.get().isdigit():
            value = int(entryvalue.get())
        else:
            value = eval(E1.get())
        entryvalue.set(value)
        E1.update()
    elif text == "Clear":
        entryvalue.set("")
        E1.update()
    else:
        entryvalue.set(entryvalue.get() + text)
        E1.update()

entryvalue = StringVar()
entryvalue.set("")
E1=Entry(root,font="lucida 33 bold",textvar=entryvalue)
E1.pack(fill=X,ipadx=8,padx=10,pady=10)
f1 = Frame(root)
b1 = Button(f1,text="9",font="comicsans 23 italic bold",
              borderwidth=3,relief=GROOVE,padx=10,pady=10)
b1.pack(side=LEFT)
b1.bind("<Button-1>",click)
b1 = Button(f1,text="8",font="comicsans 23 italic bold",
    pady=10,padx=10,borderwidth=3,relief=GROOVE)
b1.pack(side=LEFT)
b1.bind("<Button-1>",click)
b1 = Button(f1,text="7",font="comicsans 23 italic bold",
              padx=10,pady=10,borderwidth=3,relief=GROOVE)
b1.pack(side=LEFT)
b1.bind("<Button-1>",click)
b1 = Button(f1,text="+",font="comicsans 23 italic bold",
              padx=10,pady=10,borderwidth=3,relief=GROOVE)
b1.pack(side=LEFT)
b1.bind("<Button-1>",click)
f1.pack()
f2 = Frame(root)
b1 = Button(f2,text="6",font="comicsans 23 italic bold",
              padx=11,pady=10,borderwidth=3,relief=GROOVE)
b1.pack(side=LEFT)
b1.bind("<Button-1>",click)
b1 = Button(f2,text="5",font="comicsans 23 italic bold",
                padx=11,pady=10,borderwidth=3,relief=GROOVE)
b1.pack(side=LEFT)
b1.bind("<Button-1>",click)
b1 = Button(f2,text="4",font="comicsans 23 italic bold",
              padx=11,pady=10,borderwidth=3,relief=GROOVE)
b1.pack(side=LEFT)
b1.bind("<Button-1>",click)
b1 = Button(f2,text="-",font="comicsans 23 italic bold",
              padx=12,pady=10,borderwidth=3,relief=GROOVE)
b1.pack(side=LEFT)
b1.bind("<Button-1>",click)
f2.pack()
f3 = Frame(root)
b1 = Button(f3,text="3",font="comicsans 23 italic bold",
              padx=11,pady=10,borderwidth=3,relief=GROOVE)
b1.pack(side=LEFT)
b1.bind("<Button-1>",click)
b1 = Button(f3,text="2",font="comicsans 23 italic bold",
              padx=11,pady=10,borderwidth=3,relief=GROOVE)
b1.pack(side=LEFT)
b1.bind("<Button-1>",click)
b1 = Button(f3,text="1",font="comicsans 23 italic bold",
              padx=11,pady=10,borderwidth=3,relief=GROOVE)
b1.pack(side=LEFT)
b1.bind("<Button-1>",click)
b1 = Button(f3,text="*",font="comicsans 23 italic bold",
              padx=12,pady=10,borderwidth=3,relief=GROOVE)
b1.pack(side=LEFT)
b1.bind("<Button-1>",click)
f3.pack()
f4=Frame(root)
b1.pack(side=LEFT)
b1 = Button(f4,text="/",font="comicsans 23 italic bold",
              padx=12,pady=10,borderwidth=3,relief=GROOVE)
b1.pack(side=LEFT)
b1.bind("<Button-1>",click)
b1 = Button(f4,text=".",font="comicsans 23 italic bold",
              borderwidth=3,relief=GROOVE,padx=13,pady=10)
b1.pack(side=LEFT)
b1.bind("<Button-1>",click)
b1 = Button(f4,text="0",font="comicsans 23 italic bold",
            padx=10,pady=10,borderwidth=3,relief=GROOVE)
b1.pack(side=LEFT)
b1.bind("<Button-1>",click)
b1 = Button(f4,text="00",font="comicsans 23 italic bold",
              padx=5,pady=10,borderwidth=3,relief=GROOVE)
b1.pack(side=LEFT)
b1.bind("<Button-1>",click)
f4.pack()
f5=Frame(root)
b1 = Button(f5,text="=",font="comicsans 23 italic bold",borderwidth=3,
            relief=GROOVE,padx=110,pady=8)
b1.pack(side=LEFT)
b1.bind("<Button-1>",click)
f5.pack()
f6=Frame(root)
b1 = Button(f6,text="Clear",font="comicsans 23 italic bold",borderwidth=3,
            relief=GROOVE,padx=80,pady=8)
b1.pack(side=LEFT)
b1.bind("<Button-1>",click)
f6.pack()

root.mainloop()