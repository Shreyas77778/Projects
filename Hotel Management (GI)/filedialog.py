from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

root=Tk()
root.title('Silders')
root.iconbitmap('icon.ico')
root.geometry('1000x1000')
def slide(var):
    Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get())+'x'+str(vertical.get()))

btm=Button(root, text='click',command=slide).pack()

vertical=Scale(root, from_=0, to=1000)
vertical.pack()
horizontal=Scale(root, from_=0, to=1000, orient=HORIZONTAL, command=slide)
horizontal.pack()
#filedialog return the location which then can be used for opening any image
#root.filename=filedialog.askopenfilename(initialdir='D:/', title='select a file', filetypes=(('png files','*.png'),('all files','*.*')))
#Label(root, text=root.filename).pack()
#img=ImageTk.PhotoImage(Image.open(root.filename))
#img_label=Label(root, image=img).pack()



mainloop()
