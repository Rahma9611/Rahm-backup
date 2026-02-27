from tkinter import *
from tkinter import messagebox

# Setup Tkinter Window
window = Tk()
window.title("Message Box")
window.geometry("200x200")

# Function for displaying warning message 
def msg():
    messagebox.showwarning("Alert", "Stop! Virus Found.")

# adding button widget to window 
button =Button(window, text="Scan for Virus",fg="pink",bg="blue", command=msg)
button.place(x=50, y=80)

# entering main event loop
window.mainloop()
