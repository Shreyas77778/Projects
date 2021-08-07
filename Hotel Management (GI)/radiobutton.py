from tkinter import *
root=Tk()
root.title("radio button sample")
root.iconbitmap('icon.ico')


#r=IntVar()
#r.set('2')

modes=[
    ("Pepperoni","Pepperoni"),
    ("Cheese","Cheese"),
    ("Mushroom","Mushroom"),
    ("Onion","Onion")
]

pizza=StringVar()
pizza.set("Pepperoni")
def clicked(value):
    myLabel=Label(root, text=value)
    myLabel.pack()

for text, mode in modes:
    Radiobutton(root, text=text,variable=pizza, value=mode, command=lambda:clicked(pizza.get())).pack(anchor=W)



#Radiobutton(root, text='option_1', variable=r, value=1, command=lambda:clicked(r.get())).pack()
#Radiobutton(root, text='option_2', variable=r, value=2, command=lambda:clicked(r.get())).pack()

myButton=Button(root,text='click me', command=lambda:clicked(pizza.get()))
myButton.pack()
root.mainloop()
