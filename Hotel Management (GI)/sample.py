from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Hotel ShreeRam Palace')
root.iconbitmap('icon.ico')



button_quit=Button(root, text="QUIT", command=root.quit)


my_img=ImageTk.PhotoImage(Image.open('sample.jpg'))
my_img1=ImageTk.PhotoImage(Image.open('img_1.jpg'))
my_img2=ImageTk.PhotoImage(Image.open('img_2.jpg'))
my_img3=ImageTk.PhotoImage(Image.open('img_3.jpg'))

image_list=[my_img,my_img1,my_img2,my_img3]


my_label=Label(image=my_img)
my_label.grid(row=0, column=0, columnspan=3)
status=Label(root, text='Image 1 of '+str(len(image_list)), bd=1, relief=SUNKEN, anchor=W)

def forward(index):
    global my_label
    global button_next
    global button_back

    my_label.grid_forget()
    my_label=Label(image=image_list[index-1])
    my_label.grid(row=0,column=0,columnspan=3)
    button_next=Button(root, text='>>', command=lambda:forward(index+1))
    button_back=Button(root, text='<<', command=lambda:back(index-1))
    if index==4:
        button_next=Button(root, text='>>', state=DISABLED  )
    button_back.grid(row=1, column=0)
    button_next.grid(row=1, column=2)
    status=Label(root, text='Image '+str(index)+' of '+str(len(image_list)), bd=1, relief=SUNKEN, anchor=W)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


def back(index):
    global my_label
    global button_next
    global button_back
    my_label.grid_forget()
    my_label=Label(image=image_list[index-1])
    my_label.grid(row=0,column=0,columnspan=3)
    button_next=Button(root, text='>>', command=lambda:forward(index+1))
    button_back=Button(root, text='<<', command=lambda:back(index-1))
    if index==1:
        button_back=Button(root, text='<<', state=DISABLED  )
    button_back.grid(row=1, column=0)
    button_next.grid(row=1, column=2)
    status=Label(root, text='Image '+str(index)+' of '+str(len(image_list)), bd=1, relief=SUNKEN, anchor=W)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)




button_back= Button(root, text='<<', command=back, state=DISABLED)
button_quit.grid(row=1, column=1)
button_next=Button(root, text='>>',command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_next.grid(row=1, column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)
root.mainloop()
