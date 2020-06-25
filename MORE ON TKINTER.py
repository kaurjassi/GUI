from tkinter import *
root = Tk()
root.title("more things")
root.geometry("555x333")
# how  to change the icon of our gui
# root.wm_iconbitmap("1.ico")
# 1.ico is a file name of icon here we have no file of that name
root.configure(background="grey")
# this changes the backgrund color of  all gui
# screen width
width = root.winfo_screenwidth()
height= root.winfo_screenheight()
print(f"{width}x{height}")
Button(text="Close" ,command=root.destroy).pack()
# root.destroy() function is used to destroy the window of our gui


root.mainloop()