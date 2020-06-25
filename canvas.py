from tkinter import *
root = Tk()
root.title("Canvas")
canvas_width = 500
canvas_height=300
root.geometry(f"{canvas_width}x{canvas_height}")
can_widget = Canvas(root,width = canvas_width,height=canvas_height)
can_widget.pack()
filename="first.png"
can_widget.create_image(20,20)


root.mainloop()