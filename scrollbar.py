from tkinter import *
root = Tk()
root.title("scroll bar")
root.geometry("500x400")
# to make a scrollbar (horizontal) do 2 things
# 1.wideget(ysccrollcommand = scrollbar.set)
# 2. scrollbar.config(command=widget.yview)
scrollbar = Scrollbar(root)
scrollbar.pack(fill=Y,side=RIGHT)
listbox = Listbox(root,yscrollcommand=scrollbar.set)
# for i in range(344):
#     listbox.insert(END, f"item {i}")
# listbox.pack(fill=BOTH,padx=34)
# scrollbar.config(command=listbox.yview)


# MAKE A SCROLLBAR FOR WRITING A TEXT
text = Text(root,yscrollcommand=scrollbar.set,font="lucida 15 italic bold")
text.pack(fill=BOTH)
scrollbar.config(command=text.yview)


root.mainloop()