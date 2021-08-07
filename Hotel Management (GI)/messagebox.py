from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root=Tk()
root.title('message box example')
root.iconbitmap('icon.ico')
#showinfo showwaring showerror askquestion askokcancel askyesno
def popup():
    res=messagebox.askokcancel('this is popup','hello world')
    if res=='yes':
        Label(root, text="you clicked yes").pack()
    else:
        Label(root, text="you clicked no").pack()
button=Button(root, text='Popup', command=popup)
button.pack()


root.mainloop()
