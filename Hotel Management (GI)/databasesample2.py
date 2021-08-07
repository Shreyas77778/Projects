from tkinter import *
import sqlite3
from PIL import  ImageTk,Image

root=Tk()
root.title('Database Sample')
root.iconbitmap('icon.ico')
root.geometry('400x400')

#create a database or connect
con=sqlite3.connect('address_book.db')

#create cursor
c=con.cursor()

#create submit function
def submit():
    # Create a database or connect to one
	conn = sqlite3.connect('Hotel_mgmt.db')
	# Create cursor
	c = conn.cursor()

	# Insert Into Table
	c.execute("INSERT INTO stock VALUES (:double_bed_sheets, :single_bed_sheets, :double_duet_cover, :big_pillow, :small_pillow, :cushion_cover,:bed_runner,:towel,:bath_towel)",
			{
				'double_bed_sheets':41,
				'single_bed_sheets':13,
				'double_duet_cover':44,
				'big_pillow':66,
				'small_pillow':42,
				'cushion_cover':38,
				'bed_runner':31,
				'towel':35,
				'bath_towel':48
			})


	#Commit Changes
	conn.commit()

	# Close Connection
	conn.close()

	# Clear The Text Boxes
	fname.delete(0, END)
	lname.delete(0, END)
	address.delete(0, END)
	city.delete(0, END)
	state.delete(0, END)
	zipcode.delete(0, END)
#create query function
def query():
    con=sqlite3.connect('hotel_mgmt.db')
    #create cursor
    c=con.cursor()
    #query the Database
    c.execute("select *,oid from stock ")
    res=c.fetchall()
    print(res)
    print_records=''
    for record in res:
        print_records+=str(record)+'\n'
    query_label=Label(root,text=print_records)
    query_label.grid(row=8,column=0)
    #commit
    con.commit()
    #close connection
    con.close()

#create text boxes
fname=Entry(root, width=30)
fname.grid(row=0,column=1)
lname=Entry(root, width=30)
lname.grid(row=1,column=1)
address=Entry(root, width=30)
address.grid(row=2,column=1)
city=Entry(root, width=30)
city.grid(row=3,column=1)
state=Entry(root, width=30)
state.grid(row=4,column=1)
zipcode=Entry(root, width=30)
zipcode.grid(row=5,column=1)

#create box labels

fname_label=Label(root, text='First Name')
fname_label.grid(row=0,column=0)
lname_label=Label(root,text='last Name')
lname_label.grid(row=1,column=0)
address_label=Label(root, text='address')
address_label.grid(row=2,column=0)
city_label=Label(root,text='city')
city_label.grid(row=3,column=0)
state_label=Label(root,text='state')
state_label.grid(row=4,column=0)
zipcode_label=Label(root,text='zipCode')
zipcode_label.grid(row=5,column=0)

#create submit Button
btn=Button(root, text='add to db',command=submit)
btn.grid(row=6,column=1,padx=10,pady=10,ipadx=100)

#create a query Button
q_btn=Button(root,text='show records', command=query)
q_btn.grid(row=7,column=0,columnspan=2,padx=10,pady=10,ipadx=137)

mainloop()
