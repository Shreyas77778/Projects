from tkinter import *
from PIL import ImageTk, Image
root=Tk()
root.title("window test")
root.iconbitmap('icon.ico')
def open():
    global img
    top=Toplevel()
    top.title("window test")
    top.iconbitmap('icon.ico')
    img=ImageTk.PhotoImage(Image.open('img_1.jpg'))
    Label(top, image=img).pack()
    button=Button(top, text='close window', command=top.destroy)
    button.pack()

btn=Button(root, text='open second window', command=open)
btn.pack()
mainloop()
