from csv import DictWriter
from tkinter import *
def getvals():
      print("Form Submitted......")
      with open("file2.csv","a",newline='') as f:
            csv_writer = DictWriter(f, fieldnames=['FIRSTNAME','LASTNAME','AGE','EMAIL','CONTACT'])
            csv_writer.writeheader()
            csv_writer.writerow({
                  'FIRSTNAME':firstvalue.get(),
                  'LASTNAME':lastvalue.get(),
                   'AGE':agevalue.get(),
                    'EMAIL':emailvalue.get(),
            'CONTACT':contactvalue.get()})
root = Tk()
root.geometry("844x454")
root.title("Registration Form")
f1=Frame(root,bg="grey",borderwidth=5,relief=SUNKEN)
f1.grid()
l1 =Label(f1,text="DANCE REGISTRATION FORM",fg="black",font="comicsans 20 bold")
l1.grid()
# frame 2nd
f2 = Frame(root,borderwidth=5,relief= GROOVE)
f2.grid()
# label for first name
first = Label(f2,text= "FIRSTNAME",font="helvetica 10 normal")
first.grid()
# entry widget for firstname
firstvalue = StringVar()
firstentry=Entry(f2,textvariable=firstvalue)
firstentry.grid(row=0,column=1)
# frame
f3= Frame(root,borderwidth=5,relief= GROOVE)
f3.grid()
# last name
last=Label(f3,text="LASTNAME",font="helvetica 10 normal")
last.grid()
# entry widget for lastname
lastvalue = StringVar()
lastentry=Entry(f3,textvariable=lastvalue)
lastentry.grid(row=0,column=2)
# frame
f4 = Frame(root,borderwidth=5,relief= GROOVE)
f4.grid()
# age label
age=Label(f4,text="AGE",font="helvetica 10 normal")
age.grid()
# entry widget for age
agevalue = StringVar()
ageentry=Entry(f4,textvariable=agevalue)
ageentry.grid(row=0,column=3)
# frame
f5 = Frame(root,borderwidth=5,relief= GROOVE)
f5.grid()
# email label
email=Label(f5,text="EMAIL",font="helvetica 10 normal")
email.grid()
# entry widget for email
emailvalue = StringVar()
emailentry=Entry(f5,textvariable=emailvalue)
emailentry.grid(row=0,column=4)
# frame
f6= Frame(root,borderwidth=5,relief= GROOVE)
f6.grid()
# contact label
contact=Label(f6,text="CONTACT",font="helvetica 10 normal")
contact.grid()
# entry widget for contact
contactvalue = StringVar()
contactentry=Entry(f6,textvariable=contactvalue)
contactentry.grid(row=0,column=5)
Button(root,text="SUBMIT",command=getvals,font="helvetica 10 normal").grid()

root.mainloop()