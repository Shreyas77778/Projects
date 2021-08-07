from tkinter import *
from PIL import ImageTk, Image

#frames and radio buttons

root=Tk()
root.title('Hotel ShreeRam')
root.iconbitmap('icon.ico')
frame=LabelFrame(root,padx=100, pady=50)
frame.pack()

b=Button(frame, text="basic button")
b.grid(row=0,column=0)
b1=Button(frame, text = 'button 2')
b1.grid(row=1, column=1)

root.mainloop()
