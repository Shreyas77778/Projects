from tkinter import *
from PIL import ImageTk, Image

root=Tk()
root.title('checkBox title')
root.iconbitmap('icon.ico')
root.geometry('400x400')
def show():
    Label(root, text=var.get()).pack()


var=StringVar()

c=Checkbutton(root, text='check this box', variable=var,onvalue='on',offvalue='off')
#the button is selected by default so deselcting using the below function
c.deselect()
c.pack()
Label(root, text=var.get()).pack()

btn=Button(root, text='show selection', command=show)
btn.pack()

def show():
    Label(root, text=var.get()).pack()
#dropdown
var=StringVar()
var.set('Monday')
drop=OptionMenu(root, var, 'monday','tuesday', 'wednesday', 'thursday','friday')
drop.pack()
Button(root, text='Click',command=show).pack()
mainloop()
