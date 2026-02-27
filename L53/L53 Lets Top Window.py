from tkinter import *
from tkinter import messagebox

# Setup Tkinter Window
window = Tk()
window.title("Top Window")
window.geometry("400x300")

# Function for displaying warning message 
def topwin():
    # setting up top window
    top = Toplevel()
    top.geometry("250x100")
    top.title("toplevel")


    # adding a label widget to top window
    L2 = Label(top, text = "This is toplevel window")
    L2.pack()


    top.mainloop()

# Adding a label and button Widget to window (Main) Window
L = Label(window, text = "This is main window")
btn = Button(window, text = "Click here to open another window", bg="yellow", command =  topwin)

# arranging widgets
L.pack()
btn.pack()

window.mainloop()