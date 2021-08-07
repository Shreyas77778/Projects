from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root=Tk()
root.title('Database Sample')
root.iconbitmap('icon.ico')
root.geometry('400x400')

#create a database or connect
con=sqlite3.connect('hotel_mgmt.db')

#create cursor
c=con.cursor()


c.execute("delete from bookings");
#c.execute('drop table bookings')
#commit changes
con.commit()

#close connection
con.close()

root.mainloop()
