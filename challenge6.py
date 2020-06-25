from tkinter import *
def getvals():
    print("Values Submitted....")
    # print(f"{usernamevalue.get(),passwordvalue.get()}")
    with open("file1.txt","a") as f:
        f.write(f"{usernamevalue.get(),passwordvalue.get()}\n")
root = Tk()
root.geometry("333x233")
root.title("Form")
# heading
label=Label(root,text="FORM",font="helvetica 13 bold",pady=20)
label.grid(row=0,column=4)
# username
username = Label(root,text="Username",font="helvetica 13 normal",padx=30,pady=10)
username.grid(row=1,column=3)
# password
password = Label(root,text="Password",font="helvetica 13 normal",padx=30,pady=10)
password.grid(row=2,column=3)
# variables
usernamevalue=StringVar()
passwordvalue=StringVar()
# entries
usernameentry=Entry(root,textvariable=usernamevalue)
passwordentry=Entry(root,textvariable=passwordvalue)
# packing of entry widgets
usernameentry.grid(row=1 ,column=4)
passwordentry.grid(row=2 ,column=4)
# button
Button(root,text="Submit",command=getvals,font="helvetica 16 normal").grid(row=3, column=4)
root.mainloop()