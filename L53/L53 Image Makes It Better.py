from tkinter import *
from PIL import Image, ImageTk

# create a window with a title bar and set its geometry as well
window = Tk()
window.title('image')
window.geometry('400x400')

# now use Image.open to open and identigy the given image file.
upload = Image.open("L53/crochet1.jpg")

# convert this Image to Tkinter compatible image
image2 = ImageTk.PhotoImage(upload)

# add image to Tkinter Label
label = Label(window, image=image2, height=250, width=300)
label.place(x=50, y=20)

label2 = Label(window, text='Crochet')
label2.place(x=200, y=290)

# run the application
window.mainloop()