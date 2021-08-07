from tkinter import *
from PIL import ImageTk, Image
import sqlite3
import datetime
from tkinter import ttk

root=Tk()
root.title('Graphical Hotel Management System')
root.iconbitmap('icon.ico')

#root. attributes('-fullscreen', True)
#root.minsize(1300, 750)
w = 1300 # width for the Tk root
h = 750 # height for the Tk root

# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2) - 80

# set the dimensions of the screen
# and where it is placed



mycolor='#003366'
#width = root.winfo_screenwidth()
#height = root.winfo_screenheight()
#root.geometry("%dx%d" % (width, height))
search_by_date_frame=Frame(root)
search_bet_date_frame=Frame(root)
login_frame=Frame(root)
login_frame.grid(row=1,column=0)
login_frame_img=Frame(root)
login_frame_img.grid(row=0,column=0)
signup_frame=Frame(root)
home_frame=Frame(root,padx=425)
check_in_frame=Frame(root,bg=mycolor,padx=50,pady=50)
user_option_img_frame=Frame(root,padx=425)
user_option_frame=Frame(root,padx=425)
room_status_frame=Frame(root,padx=250,pady=10)
current_booking_frame=Frame(root)
current_booking_frame.grid(row=0,column=0)
select_room_frame=Frame(root,padx=250,pady=10)
select_room_label_frame=Frame(root,padx=10,pady=10)
check_out_frame=Frame(root,padx=250,pady=10)
show_booking_frame=Frame(root)
details_frame=Frame(root)
inventory_frame=Frame(root,padx=425,pady=10)
details_frame.grid(row=0,column=0)
current_stock_frame=Frame(root,background=mycolor,padx=75,pady=75)
update_stock_frame=Frame(root,background=mycolor,padx=75,pady=75)
laundry_box_frame=Frame(root,padx=425,pady=10)
laundry_recieved_frame=Frame(root,background=mycolor,padx=30,pady=75)
send_laundry_frame=Frame(root,background=mycolor,padx=75,pady=75)
show_send_laundry_frame=Frame(root,padx=250)
search_laundry_bet_date_frame=Frame(root)
show_rec_laundry_frame=Frame(root,padx=250)
search_rec_laundry_bet_date_frame=Frame(root,background=mycolor)


welcome_label=Label(login_frame_img,text='Welcome to Hotel Management System',font=('Helvetica',13),pady=10)
welcome_label.grid(row=0,column=0)

login_img=ImageTk.PhotoImage(Image.open('images//login_img.jpg'))
login_img_label=Label(login_frame_img, image=login_img,height=350,width=300)
login_img_label.grid(row=1,column=0)

back_button_img=ImageTk.PhotoImage(Image.open('images//back_button.jpg'))

vac_room_img=PhotoImage(file=r'images//blue_room_status.png')
vac_room_img=vac_room_img.subsample(4,4)

man_room_img=PhotoImage(file=r'images//yellow_room_status.png')
man_room_img=man_room_img.subsample(4,4)

occ_room_img=PhotoImage(file=r'images//red_room_status.png')
occ_room_img=occ_room_img.subsample(4,4)

#login Function
def login():
    signup_frame.grid_forget()
    login_frame.grid(row=0,column=0)
    con=sqlite3.connect('hotel_mgmt.db')
    c=con.cursor()
    c.execute('select oid,* from user')
    res=c.fetchall()
    flag=0
    for record in res:
        if username.get()==record[1]:
            if password.get()==record[2]:
                login_frame.grid_forget()
                login_frame_img.grid_forget()
                flag=1
                home()
    if flag==0:
        error_label=Label(login_frame,text='Wrong username or password')
        error_label.grid(row=5,column=1)
#Signing Up


def back_home(frame_name):

    if frame_name=='check_in_frame':
        check_in_frame.grid_forget()
    if frame_name=='signup_frame':
        signup_frame.grid_forget()
    if frame_name=='select_room_frame':
        select_room_frame.grid_forget()
    if frame_name=='show_booking_frame':
        show_booking_frame.grid_forget()
        search_by_date_frame.grid_forget()
        search_bet_date_frame.grid_forget()
    if frame_name=='user_option_frame':
        user_option_img_frame.grid_forget()
        user_option_frame.grid_forget()
    if frame_name=='room_status_frame':
        room_status_frame.grid_forget()
    if frame_name=='check_out_frame':
        check_out_frame.grid_forget()
    if frame_name=='details_frame':
        details_frame.grid_forget()
    if frame_name=='inventory_frame':
        inventory_frame.grid_forget()
    if frame_name=='laundry_box_frame':
        laundry_box_frame.grid_forget()
    if frame_name=='send_laundry_frame':
        send_laundry_frame.grid_forget()
    if frame_name=='laundry_recieved_frame':
        laundry_recieved_frame.grid_forget()
    if frame_name=='show_rec_laundry_frame':
        show_rec_laundry_frame.grid_forget()
        search_rec_laundry_bet_date_frame.grid_forget()
    if frame_name=='show_send_laundry_frame':
        show_send_laundry_frame.grid_forget()
        search_laundry_bet_date_frame.grid_forget()
    if frame_name=='current_stock_frame':
        current_stock_frame.grid_forget()
    if frame_name=='update_stock_frame':
        update_stock_frame.grid_forget()
    root.configure(background='SystemButtonFace')
    home_frame.grid(row=0,column=0)

def transfer_check_in_data(room_no):
    con=sqlite3.connect('hotel_mgmt.db')
    c=con.cursor()

    c.execute('insert into check_in_data values(:name,:address,:id_no,:age,:city,:phn_no,:gender,:company,:email,:fname,:id_type,:arrival_from,:purpose,:tarrif,:date,:room_no,:no_of_person)',{'name':name_entry.get(),'address':address_entry.get(),'id_no':id_number_entry.get(),'age':age_entry.get(),'city':city_entry.get(),'phn_no':phone_entry.get(),'gender':gender_entry.get(),'company':company_entry.get(),'email':email_entry.get(),'fname':father_entry.get(),'id_type':id_type_entry.get(),'arrival_from':arrival_from_entry.get(),'purpose':purpose_visit_entry.get(),'tarrif':room_tarrif_entry.get(),'date':datetime_entry.get(),'room_no':room_no,'no_of_person':no_of_person_entry.get()})

    con.commit()
    con.close()
    con=sqlite3.connect('hotel_mgmt.db')
    c=con.cursor()
    c.execute('insert into bookings values(:name,:address,:id_no,:age,:city,:phn_no,:gender,:company,:email,:fname,:id_type,:arrival_from,:purpose,:tarrif,:check_in_date,:room_no,:check_out_date,:no_of_person)',{'name':name_entry.get(),'address':address_entry.get(),'id_no':id_number_entry.get(),'age':age_entry.get(),'city':city_entry.get(),'phn_no':phone_entry.get(),'gender':gender_entry.get(),'company':company_entry.get(),'email':email_entry.get(),'fname':father_entry.get(),'id_type':id_type_entry.get(),'arrival_from':arrival_from_entry.get(),'purpose':purpose_visit_entry.get(),'tarrif':room_tarrif_entry.get(),'check_in_date':datetime_entry.get(),'room_no':room_no,'check_out_date':'','no_of_person':no_of_person_entry.get()})
    con.commit()
    con.close()



    select_room_frame.grid_forget()
    select_room_label_frame.grid_forget()
    root.configure(background='SystemButtonFace')
    home_frame.grid(row=0,column=0)


def check_in_continue():
    root.geometry("1350x700+0+0")
    check_in_frame.grid_forget()
    select_room_label=Label(select_room_frame,text='Select the room',font=('Helvetica',30))
    select_room_label.grid(row=0,column=2,columnspan=3)
    select_room_label_frame.grid(row=0,column=0)
    select_room_frame.grid_forget()
    select_room_label_frame.grid_forget()
    back_button=Button(select_room_frame,image=back_button_img,command=lambda:back_home('select_room_frame'))
    back_button.image=back_button_img
    back_button.grid(row=0,column=0)
    con=sqlite3.connect('hotel_mgmt.db')
    c=con.cursor()
    c.execute('select * from check_in_data')
    res=c.fetchall()

    room_001=Button(select_room_frame,image=vac_room_img,padx=20,pady=20,text='room 001',compound=TOP,command=lambda:transfer_check_in_data('1'),font=('Helvetica',10))
    room_001.image=vac_room_img

    room_002=Button(select_room_frame,image=vac_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 002',compound=TOP,command=lambda:transfer_check_in_data('2'))
    room_002.image=vac_room_img

    room_101=Button(select_room_frame,image=vac_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 101',compound=TOP,command=lambda:transfer_check_in_data('101'))
    room_101.image=vac_room_img

    room_102=Button(select_room_frame,image=vac_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 102',compound=TOP,command=lambda:transfer_check_in_data('102'))
    room_102.image=vac_room_img

    room_103=Button(select_room_frame,image=vac_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 103',compound=TOP,command=lambda:transfer_check_in_data('103'))
    room_103.image=vac_room_img

    room_104=Button(select_room_frame,image=vac_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 104',compound=TOP,command=lambda:transfer_check_in_data('104'))
    room_104.image=vac_room_img

    room_105=Button(select_room_frame,image=vac_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 105',compound=TOP,command=lambda:transfer_check_in_data('105'))
    room_105.image=vac_room_img

    room_106=Button(select_room_frame,image=vac_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 106',compound=TOP,command=lambda:transfer_check_in_data('106'))
    room_106.image=vac_room_img

    room_201=Button(select_room_frame,image=vac_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 201',compound=TOP,command=lambda:transfer_check_in_data('201'))
    room_201.image=vac_room_img

    room_202=Button(select_room_frame,image=vac_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 202',compound=TOP,command=lambda:transfer_check_in_data('202'))
    room_202.image=vac_room_img

    room_203=Button(select_room_frame,image=vac_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 203',compound=TOP,command=lambda:transfer_check_in_data('203'))
    room_203.image=vac_room_img

    room_204=Button(select_room_frame,image=vac_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 204',compound=TOP,command=lambda:transfer_check_in_data('204'))
    room_204.image=vac_room_img

    room_205=Button(select_room_frame,image=vac_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 205',compound=TOP,command=lambda:transfer_check_in_data('205'))
    room_205.image=vac_room_img

    room_206=Button(select_room_frame,image=vac_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 206',compound=TOP,command=lambda:transfer_check_in_data('206'))
    room_206.image=vac_room_img

    room_301=Button(select_room_frame,image=vac_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 301',compound=TOP,command=lambda:transfer_check_in_data('301'))
    room_301.image=vac_room_img

    room_302=Button(select_room_frame,image=vac_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 302',compound=TOP,command=lambda:transfer_check_in_data('302'))
    room_302.image=vac_room_img

    room_303=Button(select_room_frame,image=vac_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 303',compound=TOP,command=lambda:transfer_check_in_data('303'))
    room_303.image=vac_room_img

    room_304=Button(select_room_frame,image=vac_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 304',compound=TOP,command=lambda:transfer_check_in_data('304'))
    room_304.image=vac_room_img



    for number in res:

        if number[15]=='1':
            room_001=Button(select_room_frame,image=occ_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 001',compound=TOP)
            room_001.image=occ_room_img
        if number[15]=='2':
            room_002=Button(select_room_frame,image=occ_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 002',compound=TOP)
            room_002.image=occ_room_img
        if number[15]=='101':
            room_101=Button(select_room_frame,image=occ_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 101',compound=TOP)
            room_101.image=occ_room_img
        if number[15]=='102':
            room_102=Button(select_room_frame,image=occ_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 102',compound=TOP)
            room_102.image=occ_room_img
        if number[15]=='103':
            room_103=Button(select_room_frame,image=occ_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 103',compound=TOP)
            room_103.image=occ_room_img
        if number[15]=='104':
            room_104=Button(select_room_frame,image=occ_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 104',compound=TOP)
            room_104.image=occ_room_img
        if number[15]=='105':
            room_105=Button(select_room_frame,image=occ_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 105',compound=TOP)
            room_105.image=occ_room_img
        if number[15]=='106':
            room_106=Button(select_room_frame,image=occ_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 106',compound=TOP)
            room_106.image=occ_room_img
        if number[15]=='201':
            room_201=Button(select_room_frame,image=occ_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 201',compound=TOP)
            room_201.image=occ_room_img
        if number[15]=='202':
            room_202=Button(select_room_frame,image=occ_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 202',compound=TOP)
            room_202.image=occ_room_img
        if number[15]=='203':
            room_203=Button(select_room_frame,image=occ_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 203',compound=TOP)
            room_104.image=occ_room_img
        if number[15]=='204':
            room_204=Button(select_room_frame,image=occ_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 204',compound=TOP)
            room_204.image=occ_room_img
        if number[15]=='205':
            room_205=Button(select_room_frame,image=occ_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 205',compound=TOP)
            room_205.image=occ_room_img
        if number[15]=='206':
            room_206=Button(select_room_frame,image=occ_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 206',compound=TOP)
            room_206.image=occ_room_img
        if number[15]=='301':
            room_301=Button(select_room_frame,image=occ_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 301',compound=TOP)
            room_301.image=occ_room_img
        if number[15]=='302':
            room_302=Button(select_room_frame,image=occ_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 302',compound=TOP)
            room_302.image=occ_room_img
        if number[15]=='303':
            room_303=Button(select_room_frame,image=occ_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 303',compound=TOP)
            room_303.image=occ_room_img
        if number[15]=='304':
            room_304=Button(select_room_frame,image=occ_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 304',compound=TOP)
            room_304.image=occ_room_img

    room_001.grid(row=1,column=0,padx=15,pady=10)
    room_002.grid(row=1,column=1,padx=15,pady=10)
    room_101.grid(row=2,column=0,padx=15,pady=10)
    room_102.grid(row=2,column=1,padx=15,pady=10)
    room_103.grid(row=2,column=2,padx=15,pady=10)
    room_104.grid(row=2,column=3,padx=15,pady=10)
    room_105.grid(row=2,column=4,padx=15,pady=10)
    room_106.grid(row=2,column=5,padx=15,pady=10)
    room_201.grid(row=3,column=0,padx=15,pady=10)
    room_202.grid(row=3,column=1,padx=15,pady=10)
    room_203.grid(row=3,column=2,padx=15,pady=10)
    room_204.grid(row=3,column=3,padx=15,pady=10)
    room_205.grid(row=3,column=4,padx=15,pady=10)
    room_206.grid(row=3,column=5,padx=15,pady=10)
    room_301.grid(row=4,column=0,padx=15,pady=10)
    room_302.grid(row=4,column=1,padx=15,pady=10)
    room_303.grid(row=4,column=2,padx=15,pady=10)
    room_304.grid(row=4,column=3,padx=15,pady=10)
    select_room_frame.grid(row=1,column=0)

def check_using_contact():
    root.geometry("1350x700+0+0")
    phn_no=contact_check_entry.get()
    con=sqlite3.connect('hotel_mgmt.db')
    c=con.cursor()
    c.execute('select * from bookings where phn_no='+phn_no)
    res=c.fetchall()
    count=0
    for record in res:
        count=count+1


        name_entry.delete(0,END)
        address_entry.delete(0,END)
        id_number_entry.delete(0,END)
        age_entry.delete(0,END)
        city_entry.delete(0,END)
        phone_entry.delete(0,END)
        gender_entry.delete(0,END)
        company_entry.delete(0,END)
        email_entry.delete(0,END)
        father_entry.delete(0,END)
        id_type_entry.delete(0,END)
        arrival_from_entry.delete(0,END)
        purpose_visit_entry.delete(0,END)
        room_tarrif_entry.delete(0,END)


        name_entry.insert(0,record[0])
        address_entry.insert(0,record[1])
        id_number_entry.insert(0,record[2])
        age_entry.insert(0,record[3])
        arrival_from_entry.insert(0,record[4])
        phone_entry.insert(0,record[5])
        gender_entry.insert(0,record[6])
        company_entry.insert(0,record[7])
        email_entry.insert(0,record[8])
        father_entry.insert(0,record[9])
        id_type_entry.insert(0,record[10])
        city_entry.insert(0,record[11])
        purpose_visit_entry.insert(0,record[12])
        room_tarrif_entry.insert(0,record[13])


    visit_freq_label=Label(check_in_frame,text='Visited: '+str(count),bg='lightblue')
    visit_freq_label.grid(row=1,column=4)
def newcheckin():
    root.geometry("1350x700+0+0")
    root.configure(background=mycolor)
    home_frame.grid_forget()
    #home_img=ImageTk.PhotoImage(Image.open('images/hotel_name_add.jpeg'))
    #home_img_label=Label(check_in_frame,image=home_img)
    #home_img_label.image=home_img
    #home_img_label.grid(row=0,column=0,pady=20)
    back_button=Button(check_in_frame,image=back_button_img,bg=mycolor,command=lambda:back_home('check_in_frame'))
    back_button.image=back_button_img
    back_button.grid(row=0,column=0)
    check_in_label=Label(check_in_frame,text='New Check In',padx=10,pady=10,bg=mycolor,font=('Helvetica',35),fg='white')
    check_in_label.grid(row=0,column=3,pady=35)

    contact_check_label=Label(check_in_frame,bg=mycolor,text='Contact Number',padx=10,pady=20,fg='white',font=('Helvetica',15))
    global contact_check_entry
    contact_check_entry=Entry(check_in_frame,width=30,font=('Helvetica',12))
    contact_check_label.grid(row=1,column=0,pady=10)
    contact_check_entry.grid(row=1,column=1,pady=10)
    contact_check_button=Button(check_in_frame,text='Check',command=check_using_contact,font=('Helvetica',12))
    contact_check_button.grid(row=1,column=2)

    name_label=Label(check_in_frame,text='Customer Name',padx=10,pady=10,bg=mycolor,fg='white',font=('Helvetica',12))
    global name_entry
    name_entry=Entry(check_in_frame,width=30,font=('Helvetica',10))
    name_label.grid(row=2,column=0,sticky=W)
    name_entry.grid(row=2,column=1)

    age_label=Label(check_in_frame,text='Customer Age',padx=10,pady=10,bg=mycolor,fg='white',font=('Helvetica',12))
    age_label.grid(row=3,column=0,sticky=W)
    global age_entry
    age_entry=Entry(check_in_frame, width=30,font=('Helvetica',10))
    age_entry.grid(row=3,column=1)

    gender_label=Label(check_in_frame,text='Gender',padx=10,pady=10,bg=mycolor,fg='white',font=('Helvetica',12))
    gender_label.grid(row=4,column=0,sticky=W)
    global gender_entry
    gender_entry=Entry(check_in_frame,width=30,font=('Helvetica',10))
    gender_entry.grid(row=4,column=1)

    father_label=Label(check_in_frame,text='Father Name',padx=10,pady=10,bg=mycolor,fg='white',font=('Helvetica',12))
    father_label.grid(row=5,column=0,sticky=W)
    global father_entry
    father_entry=Entry(check_in_frame,width=30,font=('Helvetica',10))
    father_entry.grid(row=5,column=1)

    purpose_visit_label=Label(check_in_frame,text='Purpose of Visit',padx=10,pady=10,bg=mycolor,fg='white',font=('Helvetica',12))
    global purpose_visit_entry
    purpose_visit_entry=Entry(check_in_frame,width=30,font=('Helvetica',10))
    purpose_visit_label.grid(row=6,column=0,sticky=W)
    purpose_visit_entry.grid(row=6,column=1)

    #side 2
    address_label=Label(check_in_frame,text='Address',padx=10,pady=10,bg=mycolor,fg='white',font=('Helvetica',12))
    address_label.grid(row=2,column=2,sticky=W)
    global address_entry
    address_entry=Entry(check_in_frame,width=30,font=('Helvetica',10))
    address_entry.grid(row=2,column=3)

    city_label=Label(check_in_frame,text='City',padx=10,pady=10,bg=mycolor,fg='white',font=('Helvetica',12))
    global city_entry
    city_entry=Entry(check_in_frame,width=30,font=('Helvetica',10))
    city_label.grid(row=3,column=2,sticky=W)
    city_entry.grid(row=3,column=3)

    company_label=Label(check_in_frame,text='company',padx=10,pady=10,bg=mycolor,fg='white',font=('Helvetica',12))
    company_label.grid(row=4,column=2,sticky=W)
    global company_entry
    company_entry=Entry(check_in_frame,width=30,font=('Helvetica',10))
    company_entry.grid(row=4,column=3)

    id_type_label=Label(check_in_frame,text='ID Type',padx=10,pady=10,bg=mycolor,fg='white',font=('Helvetica',12))
    id_type_label.grid(row=5,column=2,sticky=W)
    global id_type_entry
    id_type_entry=Entry(check_in_frame,width=30,font=('Helvetica',10))
    id_type_entry.grid(row=5,column=3)

    room_tarrif_label=Label(check_in_frame,text='Room tarrif',padx=10,pady=10,bg=mycolor,fg='white',font=('Helvetica',12))
    global room_tarrif_entry
    room_tarrif_entry=Entry(check_in_frame,width=30,font=('Helvetica',10))
    room_tarrif_label.grid(row=6,column=2,sticky=W)
    room_tarrif_entry.grid(row=6,column=3)

    #side 3
    id_number_label=Label(check_in_frame,text='ID number',padx=10,pady=10,bg=mycolor,fg='white',font=('Helvetica',12))
    id_number_label.grid(row=2,column=4,sticky=W)
    global id_number_entry
    id_number_entry=Entry(check_in_frame,width=30,font=('Helvetica',10))
    id_number_entry.grid(row=2,column=5)

    phone_label=Label(check_in_frame,text='phone number',padx=10,pady=10,bg=mycolor,fg='white',font=('Helvetica',12))
    global phone_entry
    phone_entry=Entry(check_in_frame,width=30,font=('Helvetica',10))
    phone_label.grid(row=3,column=4,sticky=W)
    phone_entry.grid(row=3,column=5)

    email_label=Label(check_in_frame,text='Email',padx=10,pady=10,bg=mycolor,fg='white',font=('Helvetica',12))
    global email_entry
    email_entry=Entry(check_in_frame,width=30,font=('Helvetica',10))
    email_label.grid(row=4,column=4,sticky=W)
    email_entry.grid(row=4,column=5)

    arrival_from_label=Label(check_in_frame,text='Arrival From',padx=10,pady=10,bg=mycolor,fg='white',font=('Helvetica',12))
    global arrival_from_entry
    arrival_from_entry=Entry(check_in_frame,width=30,font=('Helvetica',10))
    arrival_from_label.grid(row=5,column=4,sticky=W)
    arrival_from_entry.grid(row=5,column=5)

    datetime_label=Label(check_in_frame,text='Date',padx=10,pady=10,bg=mycolor,fg='white',font=('Helvetica',12))
    global datetime_entry
    datetime_entry=Entry(check_in_frame,width=30,font=('Helvetica',10))
    datetime_entry.insert(0,str(datetime.date.today()))
    datetime_label.grid(row=6,column=4,sticky=W)
    datetime_entry.grid(row=6,column=5)

    no_of_person_label=Label(check_in_frame,text='Number of person',padx=10,pady=10,bg=mycolor,fg='white',font=('Helvetica',12))
    global no_of_person_entry
    no_of_person_entry=Entry(check_in_frame,width=30,font=('Helvetica',10))
    no_of_person_label.grid(row=7,column=2,sticky=W)
    no_of_person_entry.grid(row=7,column=3)

    submit_data_btn=Button(check_in_frame,text='Select Room',command=check_in_continue,font=('Helvetica',12))
    submit_data_btn.grid(row=8,column=2,columnspan=2,ipadx=100,ipady=7,pady=30)


    check_in_frame.grid(row=0,column=0)

def newuser():
    con=sqlite3.connect('hotel_mgmt.db')
    c=con.cursor()
    c.execute("INSERT INTO user VALUES (:username, :password, :name)",{'username': username.get(),'password': password.get(),'name': name.get()})
    con.commit()
    con.close()
    #clear the Boxes
    username.delete(0,END)
    password.delete(0,END)
    name.delete(0,END)
    signup_frame.grid_forget()
    user_option_img_frame.grid(row=0,column=0)
    user_option_frame.grid(row=1,column=0)
#sign up function
def signup():
    global login_img_label
    login_frame.grid_forget()
    user_option_img_frame.grid_forget()
    user_option_frame.grid_forget()
    login_img=ImageTk.PhotoImage(Image.open('images//login_img.jpg'))
    login_img_label=Label(signup_frame, image=login_img)
    login_img_label.image=login_img
    login_img_label.grid(row=0,column=1)
    back_button=Button(signup_frame,image=back_button_img,command=lambda:back_home('signup_frame'))
    back_button.image=back_button_img
    back_button.grid(row=0,column=0)

    username_label=Label(signup_frame,text='Username')
    username_label.grid(row=1,column=0)
    global username
    username=Entry(signup_frame)
    username.grid(row=1,column=1)

    password_label=Label(signup_frame,text='Password')
    password_label.grid(row=2,column=0)
    global password
    password=Entry(signup_frame,show='*')
    password.grid(row=2,column=1)

    name_label=Label(signup_frame,text='Name')
    name_label.grid(row=3,column=0)
    global name
    name=Entry(signup_frame)
    name.grid(row=3,column=1)


    signup_btn=Button(signup_frame,text='register',command=newuser)
    signup_btn.grid(row=4,column=1)

    signup_frame.grid(row=0,column=0)


def delete_user_rec():
    con=sqlite3.connect('hotel_mgmt.db')
    c=con.cursor()
    c.execute('delete from user where oid='+rec.get())
    con.commit()
    con.close()

def show_users():
    con=sqlite3.connect('hotel_mgmt.db')
    c=con.cursor()
    res=c.execute('select oid,* from user')
    #print_records=''
    res=c.fetchall()
    table=ttk.Treeview(user_option_frame,selectmode='browse',height=5)
    table.grid(row=8,column=0)
    table['columns']=('1','2')
    table['show']='headings'
    table.heading('1',text='Number id')
    table.column("1",minwidth=0,width=100,anchor='c')
    table.heading('2',text='Name',anchor='c')
    table.column("2",minwidth=0,width=100,anchor='c')
    print_records=''
    for record in res:
        count=1
        print_records+=str(record)+'\n'
        table.insert("", 'end', text =str(count),values =(record[0],record[3]))
        count+=1
    global query_label

    #query_label=Label(user_option_frame,text=print_records)
    #for record in res:
    #    print_records +=str(record[0])+'\t'+record[1]+' '+record[2]+' '+record[3]+'\n'
    #user_option_frame.grid_forget()
    #user_option_frame.grid(row=1,column=0)
    #show_rec_label=Label(user_option_frame,text=print_records)
    #show_rec_label.grid(row=8,column=0)

    con.commit()
    con.close()

def change():
    con=sqlite3.connect('hotel_mgmt.db')
    c=con.cursor()
    c.execute('update user set password=:password where oid='+rec.get(),{'password':new_pass.get()})
    pass_label=Label(user_option_frame,text='Password Changed Successfully')
    pass_label.grid(row=7,column=0)
    con.commit()
    con.close()


def change_pass():
    global new_pass_label
    new_pass_label=Label(user_option_frame,text='Enter New Password')
    new_pass_label.grid(row=5,column=0)
    global new_pass
    new_pass=Entry(user_option_frame,width=30)
    new_pass.grid(row=5,column=1)
    change_button=Button(user_option_frame,text='change',command=change)
    change_button.grid(row=6,column=1)

def useroptions():
    root.geometry("1350x700+0+0")
    home_frame.grid_forget()
    user_option_frame.grid_forget()


    #setting the image
    back_button=Button(user_option_img_frame,image=back_button_img,command=lambda:back_home('user_option_frame'))
    back_button.image=back_button_img
    back_button.grid(row=0,column=0)
    user_option_label=Label(user_option_img_frame,text='User Options',font=('Helvetica',18),padx=10,pady=10)
    user_option_label.grid(row=0,column=1)
    user_option_home_img=ImageTk.PhotoImage(Image.open('images//hotel_logo.jpg'))
    user_option_img_label=Label(user_option_img_frame,image=user_option_home_img)
    user_option_img_label.image=user_option_home_img
    user_option_img_label.grid(row=1,column=0,columnspan=3)
    user_option_img_frame.grid(row=0,column=0)

    #setting the widgets

    signup_btn=Button(user_option_frame,text='New User',command=signup)
    signup_btn.grid(row=0,column=0,pady=10,ipadx=22)

    del_rec_btn=Button(user_option_frame,text='delete',command=delete_user_rec)
    global rec
    rec=Entry(user_option_frame,width=15)

    del_rec_btn.grid(row=3,column=0,pady=10,ipadx=33)
    del_rec_entry_label=Label(user_option_frame,text='Enter the Number ID of record to \n delete or change password :-',relief='groove')
    del_rec_entry_label.grid(row=4,column=0,pady=10,ipadx=10)
    rec.grid(row=5,column=0,padx=5,pady=10)

    chnange_pass_btn=Button(user_option_frame,text='Change Password',command=change_pass)
    chnange_pass_btn.grid(row=2,column=0,pady=10)


    show_rec=Button(user_option_frame,text='Show users',command=show_users)
    show_rec.grid(row=1,column=0,pady=10,ipadx=17)

    user_option_frame.grid(row=1,column=0)

def search_by_day():
    root.geometry("1350x700+0+0")
    date=day_entry.get()
    search_by_date_frame.grid_forget()
    search_bet_date_frame.grid_forget()
    show_booking_frame.grid_forget()
    date="'"+date+"'"
    con=sqlite3.connect('Hotel_mgmt.db')
    c=con.cursor()
    c.execute('select * from bookings where check_in_date='+date)
    res=c.fetchall()
    table=ttk.Treeview(search_bet_date_frame,selectmode='browse')

    table.grid(row=2,column=0,sticky = ('N,S,W,E'))
    table['columns']=('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18')
    table['show']='headings'
    table.heading('1',text='Name')
    table.column("1",minwidth=0,width=80,anchor='c')
    table.heading('2',text='Address')
    table.column("2",minwidth=0,width=120,anchor='c')
    table.heading('3',text='ID_No')
    table.column("3",minwidth=0,width=100,anchor='c')
    table.heading('4',text='Age')
    table.column("4",minwidth=0,width=50,anchor='c')
    table.heading('5',text='Arrival from')
    table.column("5",minwidth=0,width=80,anchor='c')
    table.heading('6',text='Phone Number')
    table.column("6",minwidth=0,width=100,anchor='c')
    table.heading('7',text='Gender')
    table.column("7",minwidth=0,width=50,anchor='c')
    table.heading('8',text='Company')
    table.column("8",minwidth=0,width=100,anchor='c')
    table.heading('9',text='E-Mail')
    table.column("9",minwidth=0,width=100,anchor='c')
    table.heading('10',text='Fathers name')
    table.column("10",minwidth=0,width=90,anchor='c')
    table.heading('11',text='ID Type')
    table.column("11",minwidth=0,width=100,anchor='c')
    table.heading('12',text='City')
    table.column("12",minwidth=0,width=80,anchor='c')
    table.heading('13',text='Purpose')
    table.column("13",minwidth=0,width=100,anchor='c')
    table.heading('14',text='Check in Date')
    table.column("14",minwidth=0,width=100,anchor='c')
    table.heading('15',text='Check out Date')
    table.column("15",minwidth=0,width=100,anchor='c')
    table.heading('16',text='Persons')
    table.column("16",minwidth=0,width=50,anchor='c')
    table.heading('17',text='Room no')
    table.column("17",minwidth=0,width=50,anchor='c')
    table.heading('18',text='Tarrif')
    table.column("18",minwidth=0,width=50,anchor='c')


    print_records=''
    for record in res:
        count=1
        print_records+=str(record)+'\n'
        table.insert("", 'end', text =str(count),values =(record[0], record[1], record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10],record[11],record[12],record[14],record[16],record[17],record[15],record[13]))
        count+=1
    global query_label

    search_bet_date_frame.grid(row=1,column=0,columnspan=18)
    show_booking_frame.grid(row=0,column=0)
    con.commit()
    con.close()

def search_bet_dates():
    root.geometry("1350x700+0+0")
    date1=day_between_1.get()
    date2=day_between_2.get()
    show_booking_frame.grid_forget()
    search_by_date_frame.grid_forget()
    search_bet_date_frame.grid_forget()
    date1="'"+date1+"'"
    date2="'"+date2+"'"
    con=sqlite3.connect('Hotel_mgmt.db')
    c=con.cursor()
    c.execute('select * from bookings where check_in_date between'+date1+'and'+date2)
    res=c.fetchall()
    table=ttk.Treeview(search_bet_date_frame,selectmode='browse')

    table.grid(row=2,column=0,sticky = ('N,S,W,E'))
    table['columns']=('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18')
    table['show']='headings'
    table.heading('1',text='Name')
    table.column("1",minwidth=0,width=80,anchor='c')
    table.heading('2',text='Address')
    table.column("2",minwidth=0,width=120,anchor='c')
    table.heading('3',text='ID_No')
    table.column("3",minwidth=0,width=100,anchor='c')
    table.heading('4',text='Age')
    table.column("4",minwidth=0,width=50,anchor='c')
    table.heading('5',text='Arrival from')
    table.column("5",minwidth=0,width=80,anchor='c')
    table.heading('6',text='Phone Number')
    table.column("6",minwidth=0,width=100,anchor='c')
    table.heading('7',text='Gender')
    table.column("7",minwidth=0,width=50,anchor='c')
    table.heading('8',text='Company')
    table.column("8",minwidth=0,width=100,anchor='c')
    table.heading('9',text='E-Mail')
    table.column("9",minwidth=0,width=100,anchor='c')
    table.heading('10',text='Fathers name')
    table.column("10",minwidth=0,width=90,anchor='c')
    table.heading('11',text='ID Type')
    table.column("11",minwidth=0,width=100,anchor='c')
    table.heading('12',text='City')
    table.column("12",minwidth=0,width=80,anchor='c')
    table.heading('13',text='Purpose')
    table.column("13",minwidth=0,width=100,anchor='c')
    table.heading('14',text='Check in Date')
    table.column("14",minwidth=0,width=100,anchor='c')
    table.heading('15',text='Check out Date')
    table.column("15",minwidth=0,width=100,anchor='c')
    table.heading('16',text='Persons')
    table.column("16",minwidth=0,width=50,anchor='c')
    table.heading('17',text='Room no')
    table.column("17",minwidth=0,width=50,anchor='c')
    table.heading('18',text='Tarrif')
    table.column("18",minwidth=0,width=50,anchor='c')
    print_records=''
    for record in res:
        count=1
        print_records+=str(record)+'\n'
        table.insert("", 'end', text =str(count),values =(record[0], record[1], record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10],record[11],record[12],record[14],record[16],record[17],record[15],record[13]))
        count+=1
    global query_label

    #query_label=Label(search_by_date_frame,text=print_records)
    search_bet_date_frame.grid(row=1,column=0,columnspan=18)
    show_booking_frame.grid(row=0,column=0)



    con.commit()
    con.close()

def show_booking():
    root.geometry("1350x700+0+0")
    home_frame.grid_forget()
    show_booking_frame.grid_forget()
    back_button=Button(show_booking_frame,image=back_button_img,command=lambda:back_home('show_booking_frame'))
    back_button.image=back_button_img
    back_button.grid(row=0,column=0,pady=5)
    show_booking_label=Label(show_booking_frame,text='Bookings',font=('Helvetica',20),height=2)
    show_booking_label.grid(row=0,column=1,columnspan=20,ipadx=30)

    date=datetime.date.today()
    global day_entry
    day_entry=Entry(show_booking_frame)
    day_entry.insert(0,date)
    global day_btn
    day_btn=Button(show_booking_frame,text='Search by day',command=search_by_day)
    global day_between_1
    day_between_1=Entry(show_booking_frame)
    global day_between_2
    day_between_2=Entry(show_booking_frame)
    day_between_2.insert(0,date)
    global day_between_btn
    day_between_btn=Button(show_booking_frame,text='Search Between Dates',command=search_bet_dates)
    day_entry.grid(row=1,column=0,sticky='W',padx=30,pady=10)
    day_btn.grid(row=1,column=1,sticky='W',padx=30,pady=10)
    day_between_1.grid(row=1,column=6,sticky='E',padx=30,pady=10)
    day_between_2.grid(row=1,column=7,sticky='E',padx=30,pady=10)
    day_between_btn.grid(row=1,column=8,sticky='E',padx=30,pady=10)
    show_booking_frame.grid(row=0,column=0,ipady=150,ipadx=100)

def room_status():
    root.geometry("1350x700+0+0")
    home_frame.grid_forget()
    back_button=Button(room_status_frame,image=back_button_img,command=lambda:back_home('room_status_frame'))
    back_button.image=back_button_img
    select_room_label=Label(room_status_frame,text='Room Status',font=('Helvetica',15),height=2)
    select_room_label.grid(row=0,column=2,columnspan=2)
    select_room_frame.grid_forget()

    con=sqlite3.connect('hotel_mgmt.db')
    c=con.cursor()
    c.execute('select * from check_in_data')
    res=c.fetchall()

    room_001=Button(room_status_frame,image=vac_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 001',compound=TOP)
    room_001.image=vac_room_img

    room_002=Button(room_status_frame,image=vac_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 002',compound=TOP)
    room_002.image=vac_room_img

    room_101=Button(room_status_frame,image=vac_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 101',compound=TOP)
    room_101.image=vac_room_img

    room_102=Button(room_status_frame,image=vac_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 102',compound=TOP)
    room_102.image=vac_room_img

    room_103=Button(room_status_frame,image=vac_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 103',compound=TOP)
    room_103.image=vac_room_img

    room_104=Button(room_status_frame,image=vac_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 104',compound=TOP)
    room_104.image=vac_room_img

    room_105=Button(room_status_frame,image=vac_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 105',compound=TOP)
    room_105.image=vac_room_img

    room_106=Button(room_status_frame,image=vac_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 106',compound=TOP)
    room_106.image=vac_room_img

    room_201=Button(room_status_frame,image=vac_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 201',compound=TOP)
    room_201.image=vac_room_img

    room_202=Button(room_status_frame,image=vac_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 202',compound=TOP)
    room_202.image=vac_room_img

    room_203=Button(room_status_frame,image=vac_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 203',compound=TOP)
    room_203.image=vac_room_img

    room_204=Button(room_status_frame,image=vac_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 204',compound=TOP)
    room_204.image=vac_room_img

    room_205=Button(room_status_frame,image=vac_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 205',compound=TOP)
    room_205.image=vac_room_img

    room_206=Button(room_status_frame,image=vac_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 206',compound=TOP)
    room_206.image=vac_room_img

    room_301=Button(room_status_frame,image=vac_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 301',compound=TOP)
    room_301.image=vac_room_img

    room_302=Button(room_status_frame,image=vac_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 302',compound=TOP)
    room_302.image=vac_room_img

    room_303=Button(room_status_frame,image=vac_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 303',compound=TOP)
    room_303.image=vac_room_img

    room_304=Button(room_status_frame,image=vac_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 304',compound=TOP)
    room_304.image=vac_room_img

    for number in res:
        if number[15]=='1':
            room_001=Button(room_status_frame,image=occ_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 001',compound=TOP,command=lambda:details('1'))
            room_001.image=occ_room_img
        if number[15]=='2':
            room_002=Button(room_status_frame,image=occ_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 002',compound=TOP,command=lambda:details('2'))
            room_002.image=occ_room_img
        if number[15]=='101':
            room_101=Button(room_status_frame,image=occ_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 101',compound=TOP,command=lambda:details('101'))
            room_101.image=occ_room_img
        if number[15]=='102':
            room_102=Button(room_status_frame,image=occ_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 102',compound=TOP,command=lambda:details('102'))
            room_102.image=occ_room_img
        if number[15]=='103':
            room_103=Button(room_status_frame,image=occ_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 103',compound=TOP,command=lambda:details('103'))
            room_103.image=occ_room_img
        if number[15]=='104':
            room_104=Button(room_status_frame,image=occ_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 104',compound=TOP,command=lambda:details('104'))
            room_104.image=occ_room_img
        if number[15]=='105':
            room_105=Button(room_status_frame,image=occ_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 105',compound=TOP,command=lambda:details('105'))
            room_105.image=occ_room_img
        if number[15]=='106':
            room_106=Button(room_status_frame,image=occ_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 106',compound=TOP,command=lambda:details('106'))

            room_106.image=occ_room_img
        if number[15]=='201':
            room_201=Button(room_status_frame,image=occ_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 201',compound=TOP,command=lambda:details('201'))
            room_201.image=occ_room_img
        if number[15]=='202':
            room_202=Button(room_status_frame,image=occ_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 202',compound=TOP,command=lambda:details('202'))
            room_202.image=occ_room_img
        if number[15]=='203':
            room_203=Button(room_status_frame,image=occ_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 203',compound=TOP,command=lambda:details('203'))
            room_104.image=occ_room_img
        if number[15]=='204':
            room_204=Button(room_status_frame,image=occ_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 204',compound=TOP,command=lambda:details('204'))
            room_204.image=occ_room_img
        if number[15]=='205':
            room_205=Button(room_status_frame,image=occ_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 205',compound=TOP,command=lambda:details('205'))
            room_205.image=occ_room_img
        if number[15]=='206':
            room_206=Button(room_status_frame,image=occ_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 206',compound=TOP,command=lambda:details('206'))
            room_206.image=occ_room_img
        if number[15]=='301':
            room_301=Button(room_status_frame,image=occ_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 301',compound=TOP,command=lambda:details('301'))
            room_301.image=occ_room_img
        if number[15]=='302':
            room_302=Button(room_status_frame,image=occ_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 302',compound=TOP,command=lambda:details('302'))
            room_302.image=occ_room_img
        if number[15]=='303':
            room_303=Button(room_status_frame,image=occ_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 303',compound=TOP,command=lambda:details('303'))
            room_303.image=occ_room_img
        if number[15]=='304':
            room_304=Button(room_status_frame,image=occ_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 304',compound=TOP,command=lambda:details('304'))
            room_304.image=occ_room_img

    room_001.grid(row=1,column=0,padx=15,pady=10)
    room_002.grid(row=1,column=1,padx=15,pady=10)
    room_101.grid(row=2,column=0,padx=15,pady=10)
    room_102.grid(row=2,column=1,padx=15,pady=10)
    room_103.grid(row=2,column=2,padx=15,pady=10)
    room_104.grid(row=2,column=3,padx=15,pady=10)
    room_105.grid(row=2,column=4,padx=15,pady=10)
    room_106.grid(row=2,column=5,padx=15,pady=10)
    room_201.grid(row=3,column=0,padx=15,pady=10)
    room_202.grid(row=3,column=1,padx=15,pady=10)
    room_203.grid(row=3,column=2,padx=15,pady=10)
    room_204.grid(row=3,column=3,padx=15,pady=10)
    room_205.grid(row=3,column=4,padx=15,pady=10)
    room_206.grid(row=3,column=5,padx=15,pady=10)
    room_301.grid(row=4,column=0,padx=15,pady=10)
    room_302.grid(row=4,column=1,padx=15,pady=10)
    room_303.grid(row=4,column=2,padx=15,pady=10)
    room_304.grid(row=4,column=3,padx=15,pady=10)
    back_button.grid(row=0,column=0)

    room_status_frame.grid(row=0,column=0)

def details(room):
    root.geometry("1350x700+0+0")
    room_status_frame.grid_forget()
    con=sqlite3.connect('hotel_mgmt.db')
    details_frame.grid_forget()
    c=con.cursor()
    c.execute('select * from check_in_data where room_no='+room)
    res=c.fetchall()
    result=''
    for record in res:
         result+=str('Name:   '+record[0]+'\n\n'+"Address:   "+record[1]+'\n\n'+"ID type:  "+record[10]+"\n\n"+'ID:  '+record[2]+'\n\n'+'Age:  '+record[3]+"\n\n"+"City:  "+record[4]+'\n\n'+'Phn_no:  '+record[5]+'\n\n'+"Gender:  "+record[6]+'\n\n'+"Company:  "+record[7]+"\n\n"+'Email:  '+record[8]+'\n\n'+'Father Name:  '+record[9]+'\n\n'+"Arrival from:  "+record[11]+'\n\n'+"Purpose:  "+record[12]+"\n\n"+'Tarrif:  '+record[13]+'\n\n'+'Date:  '+record[14]+'\n\n'+"Room_no:  "+record[15]+'\n\n'+'No. of person :'+record[16])+'\n\n'

    show_rec_label=Label(details_frame,text=result)
    show_rec_label.grid(row=1,column=0,columnspan=5)
    back_button=Button(details_frame,image=back_button_img,command=lambda:back_home('details_frame'))
    back_button.image=back_button_img
    back_button.grid(row=0,column=0)
    details_frame.grid(row=0,column=0)
    con.commit()
    con.close()

def view_laundry_box():
    return
def current_stock():
    root.geometry("1350x700+0+0")
    root.configure(bg=mycolor)
    inventory_frame.grid_forget()
    label=Label(current_stock_frame,text='Current Stock',font=('Helvetica',30),pady=10,bg=mycolor,fg='white')
    label.grid(row=0,column=2)
    con=sqlite3.connect('Hotel_mgmt.db')
    c=con.cursor()
    c.execute('select * from stock')
    back_button=Button(current_stock_frame,image=back_button_img,command=lambda:back_home('current_stock_frame'),bg=mycolor)
    back_button.image=back_button_img
    back_button.grid(row=0,column=0)
    res=c.fetchall()
    print_records=''
    for record in res:
        double_bed_sheets=record[0]
        single_bed_sheets=record[1]
        double_duet_cover=record[2]
        big_pillow=record[3]
        small_pillow=record[4]
        cushion_cover=record[5]
        bed_runner=record[6]
        towel=record[7]
        bath_towel=record[8]
    con.commit()
    con.close()
    double_bed_sheets_label=Label(current_stock_frame,text='Double Bed Sheets',bg=mycolor,fg='white',font=('Helvetica',15))
    double_bed_sheets_entry=Entry(current_stock_frame,width=30,font=('Helvetica',10))
    double_bed_sheets_label.grid(row=1,column=0,padx=5,pady=5)
    double_bed_sheets_entry.grid(row=1,column=1,padx=5,pady=5)
    double_bed_sheets_entry.insert(0,double_bed_sheets)

    single_bed_sheets_label=Label(current_stock_frame,text='Single Bed Sheets',bg=mycolor,fg='white',font=('Helvetica',15))
    single_bed_sheets_entry=Entry(current_stock_frame,width=30,font=('Helvetica',10))
    single_bed_sheets_label.grid(row=2,column=0,padx=5,pady=5)
    single_bed_sheets_entry.grid(row=2,column=1,padx=5,pady=5)
    single_bed_sheets_entry.insert(0,single_bed_sheets)

    double_duet_cover_label=Label(current_stock_frame,text='Double Duet Cover',bg=mycolor,fg='white',font=('Helvetica',15))
    double_duet_cover_entry=Entry(current_stock_frame,width=30,font=('Helvetica',10))
    double_duet_cover_label.grid(row=1,column=2,padx=5,pady=5)
    double_duet_cover_entry.grid(row=1,column=3,padx=5,pady=5)
    double_duet_cover_entry.insert(0,double_duet_cover)

    big_pillows_label=Label(current_stock_frame,text='Big Pillows',bg=mycolor,fg='white',font=('Helvetica',15))
    big_pillows_entry=Entry(current_stock_frame,width=30,font=('Helvetica',10))
    big_pillows_label.grid(row=2,column=2,padx=5,pady=5)
    big_pillows_entry.grid(row=2,column=3,padx=5,pady=5)
    big_pillows_entry.insert(0,big_pillow)

    small_pillows_label=Label(current_stock_frame,text='Small Pillows',bg=mycolor,fg='white',font=('Helvetica',15))
    small_pillows_entry=Entry(current_stock_frame,width=30,font=('Helvetica',10))
    small_pillows_label.grid(row=3,column=0,padx=5,pady=5)
    small_pillows_entry.grid(row=3,column=1,padx=5,pady=5)
    small_pillows_entry.insert(0,small_pillow)

    cushion_cover_label=Label(current_stock_frame,text='Cushion Covers',bg=mycolor,fg='white',font=('Helvetica',15))
    cushion_cover_entry=Entry(current_stock_frame,width=30,font=('Helvetica',10))
    cushion_cover_label.grid(row=3,column=2,padx=5,pady=5)
    cushion_cover_entry.grid(row=3,column=3,padx=5,pady=5)
    cushion_cover_entry.insert(0,cushion_cover)

    bed_runner_label=Label(current_stock_frame,text='Bed Runners',bg=mycolor,fg='white',font=('Helvetica',15))
    bed_runner_entry=Entry(current_stock_frame,width=30,font=('Helvetica',10))
    bed_runner_label.grid(row=1,column=4,padx=5,pady=5)
    bed_runner_entry.grid(row=1,column=5,padx=5,pady=5)
    bed_runner_entry.insert(0,bed_runner)

    towel_label=Label(current_stock_frame,text='Towels',bg=mycolor,fg='white',font=('Helvetica',15))
    towel_entry=Entry(current_stock_frame,width=30,font=('Helvetica',10))
    towel_entry.grid(row=2,column=5,padx=5,pady=5)
    towel_label.grid(row=2,column=4,padx=5,pady=5)
    towel_entry.insert(0,towel)

    bath_towel_label=Label(current_stock_frame,text='Bath Towel',bg=mycolor,fg='white',font=('Helvetica',15))
    bath_towel_entry=Entry(current_stock_frame,width=30,font=('Helvetica',10))
    bath_towel_entry.grid(row=3,column=5,padx=5,pady=5)
    bath_towel_label.grid(row=3,column=4,padx=5,pady=5)
    bath_towel_entry.insert(0,bath_towel)
    current_stock_frame.grid()

def update_stock():
    con=sqlite3.connect('Hotel_mgmt.db')
    c=con.cursor()
    c.execute("INSERT INTO stock VALUES (:double_bed_sheets, :single_bed_sheets, :double_duet_cover, :big_pillow, :small_pillow, :cushion_cover,:bed_runner,:towel,:bath_towel)",{'double_bed_sheets':double_bed_sheets_entry.get(),'single_bed_sheets':single_bed_sheets_entry.get(),'double_duet_cover':double_duet_cover_entry.get(),'big_pillow':big_pillows_entry.get(),'small_pillow':small_pillows_entry.get(),'cushion_cover':cushion_cover_entry.get(),'bed_runner':bed_runner_entry.get(),'towel':towel_entry.get(),'bath_towel':bath_towel_entry.get()})
    con.commit()
    con.close()
    update_stock_frame.grid_forget()
    home_frame.grid()

def edit_stock():
    root.geometry("1350x700+0+0")
    root.configure(bg=mycolor)
    inventory_frame.grid_forget()
    label=Label(update_stock_frame,text='Edit Stock',font=('Helvetica',30),pady=10,bg=mycolor,fg='white')
    label.grid(row=0,column=2)
    con=sqlite3.connect('Hotel_mgmt.db')
    c=con.cursor()
    c.execute('select * from stock')
    back_button=Button(update_stock_frame,image=back_button_img,command=lambda:back_home('update_stock_frame'),bg=mycolor)
    back_button.image=back_button_img
    back_button.grid(row=0,column=0)
    res=c.fetchall()
    print_records=''
    for record in res:
        global double_bed_sheets
        double_bed_sheets=record[0]
        global single_bed_sheets
        single_bed_sheets=record[1]
        global double_duet_cover
        double_duet_cover=record[2]
        global big_pillow
        big_pillow=record[3]
        global small_pillow
        small_pillow=record[4]
        global cushion_cover
        cushion_cover=record[5]
        global bed_runner
        bed_runner=record[6]
        global towel
        towel=record[7]
        global bath_towel
        bath_towel=record[8]
    con.commit()
    con.close()

    global double_bed_sheets_entry
    double_bed_sheets_label=Label(update_stock_frame,text='Double Bed Sheets',bg=mycolor,fg='white',font=('Helvetica',15))
    double_bed_sheets_entry=Entry(update_stock_frame,width=30,font=('Helvetica',10))
    double_bed_sheets_label.grid(row=1,column=0,padx=5,pady=5)
    double_bed_sheets_entry.grid(row=1,column=1,padx=5,pady=5)
    double_bed_sheets_entry.insert(0,double_bed_sheets)

    global single_bed_sheets_entry
    single_bed_sheets_label=Label(update_stock_frame,text='Single Bed Sheets',bg=mycolor,fg='white',font=('Helvetica',15))
    single_bed_sheets_entry=Entry(update_stock_frame,width=30,font=('Helvetica',10))
    single_bed_sheets_label.grid(row=2,column=0,padx=5,pady=5)
    single_bed_sheets_entry.grid(row=2,column=1,padx=5,pady=5)
    single_bed_sheets_entry.insert(0,single_bed_sheets)

    global double_duet_cover_entry
    double_duet_cover_label=Label(update_stock_frame,text='Double Duet Cover',bg=mycolor,fg='white',font=('Helvetica',15))
    double_duet_cover_entry=Entry(update_stock_frame,width=30,font=('Helvetica',10))
    double_duet_cover_label.grid(row=1,column=2,padx=5,pady=5)
    double_duet_cover_entry.grid(row=1,column=3,padx=5,pady=5)
    double_duet_cover_entry.insert(0,double_duet_cover)

    global big_pillows_entry
    big_pillows_label=Label(update_stock_frame,text='Big Pillows',bg=mycolor,fg='white',font=('Helvetica',15))
    big_pillows_entry=Entry(update_stock_frame,width=30,font=('Helvetica',10))
    big_pillows_label.grid(row=2,column=2,padx=5,pady=5)
    big_pillows_entry.grid(row=2,column=3,padx=5,pady=5)
    big_pillows_entry.insert(0,big_pillow)

    global small_pillows_entry
    small_pillows_label=Label(update_stock_frame,text='Small Pillows',bg=mycolor,fg='white',font=('Helvetica',15))
    small_pillows_entry=Entry(update_stock_frame,width=30,font=('Helvetica',10))
    small_pillows_label.grid(row=3,column=0,padx=5,pady=5)
    small_pillows_entry.grid(row=3,column=1,padx=5,pady=5)
    small_pillows_entry.insert(0,small_pillow)

    global cushion_cover_entry
    cushion_cover_label=Label(update_stock_frame,text='Cushion Covers',bg=mycolor,fg='white',font=('Helvetica',15))
    cushion_cover_entry=Entry(update_stock_frame,width=30,font=('Helvetica',10))
    cushion_cover_entry.grid(row=3,column=3,padx=5,pady=5)
    cushion_cover_label.grid(row=3,column=2,padx=5,pady=5)
    cushion_cover_entry.insert(0,cushion_cover)

    global bed_runner_entry
    bed_runner_label=Label(update_stock_frame,text='Bed Runners',bg=mycolor,fg='white',font=('Helvetica',15))
    bed_runner_entry=Entry(update_stock_frame,width=30,font=('Helvetica',10))
    bed_runner_label.grid(row=1,column=4,padx=5,pady=5)
    bed_runner_entry.grid(row=1,column=5,padx=5,pady=5)
    bed_runner_entry.insert(0,bed_runner)

    global towel_entry
    towel_label=Label(update_stock_frame,text='Towels',bg=mycolor,fg='white',font=('Helvetica',15))
    towel_entry=Entry(update_stock_frame,width=30,font=('Helvetica',10))
    towel_label.grid(row=2,column=4,padx=5,pady=5)
    towel_entry.grid(row=2,column=5,padx=5,pady=5)
    towel_entry.insert(0,towel)

    global bath_towel_entry
    bath_towel_label=Label(update_stock_frame,text=' Bath Towel',bg=mycolor,fg='white',font=('Helvetica',15))
    bath_towel_entry=Entry(update_stock_frame,width=30,font=('Helvetica',10))
    bath_towel_label.grid(row=3,column=4,padx=5,pady=5)
    bath_towel_entry.grid(row=3,column=5,padx=5,pady=5)
    bath_towel_entry.insert(0,bath_towel)

    edit_stock_btn=Button(update_stock_frame,text='Update',command=update_stock,font=('Helvetica',10))
    edit_stock_btn.grid(row=4,column=2,ipadx=20,pady=5)

    update_stock_frame.grid(row=0,column=0)
    con.close()

def send_complete():
    con=sqlite3.connect('hotel_mgmt.db')
    c=con.cursor()
    c.execute('insert into sent_laundry values(:double_bed_sheets,:single_bed_sheets,:double_duet_cover,:cushion_cover,:bed_runner,:towel,:bath_towel,:date)',{'double_bed_sheets':double_bed_sheets_entry.get(),'single_bed_sheets':single_bed_sheets_entry.get(),'double_duet_cover':double_duet_cover_entry.get(),'cushion_cover':cushion_cover_entry.get(),'bed_runner':bed_runner_entry.get(),'towel':towel_entry.get(),'bath_towel':bath_towel_entry.get(),'date':str(datetime.date.today())})
    con.commit()
    con.close()
    send_laundry_frame.grid_forget()
    root.configue(background='SystemButtonFace')
    home_frame.grid(row=0,column=0)

def send_laundry():
    root.geometry("1350x700+0+0")
    laundry_box_frame.grid_forget()
    label=Label(send_laundry_frame,text='Send Laundry',font=('Helvetica',30),pady=10,bg=mycolor,fg='white')
    label.grid(row=0,column=2)
    back_button=Button(send_laundry_frame,image=back_button_img,command=lambda:back_home('send_laundry_frame'),bg=mycolor)
    back_button.image=back_button_img
    back_button.grid(row=0,column=0,pady=5)
    root.configure(bg=mycolor)
    global double_bed_sheets_entry
    double_bed_sheets_label=Label(send_laundry_frame,text='Double Bed Sheets',bg=mycolor,fg='white',font=('Helvetica',15))
    double_bed_sheets_entry=Entry(send_laundry_frame,width=30,font=('Helvetica',10))
    double_bed_sheets_label.grid(row=1,column=0,padx=5,pady=5)
    double_bed_sheets_entry.grid(row=1,column=1,padx=5,pady=5)

    global single_bed_sheets_entry
    single_bed_sheets_label=Label(send_laundry_frame,text='Single Bed Sheets',bg=mycolor,fg='white',font=('Helvetica',15))
    single_bed_sheets_entry=Entry(send_laundry_frame,width=30,font=('Helvetica',10))
    single_bed_sheets_label.grid(row=2,column=0,padx=5,pady=5)
    single_bed_sheets_entry.grid(row=2,column=1,padx=5,pady=5)

    global double_duet_cover_entry
    double_duet_cover_label=Label(send_laundry_frame,text='Double Duet Cover',bg=mycolor,fg='white',font=('Helvetica',15))
    double_duet_cover_entry=Entry(send_laundry_frame,width=30,font=('Helvetica',10))
    double_duet_cover_label.grid(row=1,column=2,padx=5,pady=5)
    double_duet_cover_entry.grid(row=1,column=3,padx=5,pady=5)

    cushion_cover_label=Label(send_laundry_frame,text='Cushion Covers',bg=mycolor,fg='white',font=('Helvetica',15))
    global cushion_cover_entry
    cushion_cover_entry=Entry(send_laundry_frame,width=30,font=('Helvetica',10))
    cushion_cover_label.grid(row=3,column=2,padx=5,pady=5)
    cushion_cover_entry.grid(row=3,column=3,padx=5,pady=5)

    bed_runner_label=Label(send_laundry_frame,text='Bed Runners',bg=mycolor,fg='white',font=('Helvetica',15))
    global bed_runner_entry
    bed_runner_entry=Entry(send_laundry_frame,width=30,font=('Helvetica',10))
    bed_runner_label.grid(row=1,column=4,padx=5,pady=5)
    bed_runner_entry.grid(row=1,column=5,padx=5,pady=5)

    global towel_entry
    towel_label=Label(send_laundry_frame,text='Towels',bg=mycolor,fg='white',font=('Helvetica',15))
    towel_entry=Entry(send_laundry_frame,width=30,font=('Helvetica',10))
    towel_label.grid(row=2,column=4,padx=5,pady=5)
    towel_entry.grid(row=2,column=5,padx=5,pady=5)

    global bath_towel_entry
    bath_towel_label=Label(send_laundry_frame,text='Bath Towel',bg=mycolor,fg='white',font=('Helvetica',15))
    bath_towel_entry=Entry(send_laundry_frame,width=30,font=('Helvetica',10))
    bath_towel_label.grid(row=2,column=2,padx=5,pady=5)
    bath_towel_entry.grid(row=2,column=3,padx=5,pady=5)

    send_laundry_btn=Button(send_laundry_frame,text='Save',command=send_complete,font=('Helvetica',10))
    send_laundry_btn.grid(row=4,column=2,padx=10,pady=5,ipadx=30)
    send_laundry_frame.grid(row=0,column=0)


def recieve_complete():
    con=sqlite3.connect('Hotel_mgmt.db')
    c=con.cursor()
    c.execute('insert into laundry values(:double_bed_sheets,:single_bed_sheets,:double_duet_cover,:cushion_cover,:bed_runner,:towel,:bath_towel,:date)',{'double_bed_sheets':double_bed_sheets_entry.get(),'single_bed_sheets':single_bed_sheets_entry.get(),'double_duet_cover':double_duet_cover_entry.get(),'cushion_cover':cushion_cover_entry.get(),'bed_runner':bed_runner_entry.get(),'towel':towel_entry.get(),'bath_towel':bath_towel_entry.get(),'date':datetime.date.today()})
    con.commit()
    con.close()
    laundry_recieved_frame.grid_forget()
    root.configure(background='SystemButtonFace')
    home_frame.grid(row=0,column=0)

def laundry_recieved():
    root.geometry("1350x700+0+0")
    root.configure(bg=mycolor)
    laundry_box_frame.grid_forget()
    label=Label(laundry_recieved_frame,text='Recieved Laundry',font=('Helvetica',30),pady=10,bg=mycolor,fg='white')
    label.grid(row=0,column=2)
    back_button=Button(laundry_recieved_frame,image=back_button_img,command=lambda:back_home('laundry_recieved_frame'),bg=mycolor)
    back_button.image=back_button_img
    back_button.grid(row=0,column=0)

    global double_bed_sheets_entry
    double_bed_sheets_label=Label(laundry_recieved_frame,text='Double Bed Sheets',bg=mycolor,fg='white',font=('Helvetica',15))
    double_bed_sheets_entry=Entry(laundry_recieved_frame,width=30,font=('Helvetica',10))
    double_bed_sheets_label.grid(row=1,column=0,padx=5,pady=5)
    double_bed_sheets_entry.grid(row=1,column=1,padx=5,pady=5)

    global single_bed_sheets_entry
    single_bed_sheets_label=Label(laundry_recieved_frame,text='Single Bed Sheets',bg=mycolor,fg='white',font=('Helvetica',15))
    single_bed_sheets_entry=Entry(laundry_recieved_frame,width=30,font=('Helvetica',10))
    single_bed_sheets_label.grid(row=2,column=0,padx=5,pady=5)
    single_bed_sheets_entry.grid(row=2,column=1,padx=5,pady=5)

    global double_duet_cover_entry
    double_duet_cover_label=Label(laundry_recieved_frame,text='Double Duet Cover',bg=mycolor,fg='white',font=('Helvetica',15))
    double_duet_cover_entry=Entry(laundry_recieved_frame,width=30,font=('Helvetica',10))
    double_duet_cover_label.grid(row=1,column=2,padx=5,pady=5)
    double_duet_cover_entry.grid(row=1,column=3,padx=5,pady=5)

    global cushion_cover_entry
    cushion_cover_label=Label(laundry_recieved_frame,text='Cushion Covers',bg=mycolor,fg='white',font=('Helvetica',15))
    cushion_cover_entry=Entry(laundry_recieved_frame,width=30,font=('Helvetica',10))
    cushion_cover_label.grid(row=3,column=2,padx=5,pady=5)
    cushion_cover_entry.grid(row=3,column=3,padx=5,pady=5)

    global bed_runner_entry
    bed_runner_label=Label(laundry_recieved_frame,text='Bed Runners',bg=mycolor,fg='white',font=('Helvetica',15))
    bed_runner_entry=Entry(laundry_recieved_frame,width=30,font=('Helvetica',10))
    bed_runner_label.grid(row=1,column=4,padx=5,pady=5)
    bed_runner_entry.grid(row=1,column=5,padx=5,pady=5)

    global towel_entry
    towel_label=Label(laundry_recieved_frame,text='Towels',bg=mycolor,fg='white',font=('Helvetica',15))
    towel_entry=Entry(laundry_recieved_frame,width=30,font=('Helvetica',10))
    towel_label.grid(row=2,column=4,padx=5,pady=5)
    towel_entry.grid(row=2,column=5,padx=5,pady=5)

    global bath_towel_entry
    bath_towel_label=Label(laundry_recieved_frame,text=' Bath Towel',bg=mycolor,fg='white',font=('Helvetica',15))
    bath_towel_entry=Entry(laundry_recieved_frame,width=30,font=('Helvetica',10))
    bath_towel_label.grid(row=2,column=2,padx=5,pady=5)
    bath_towel_entry.grid(row=2,column=3,padx=5,pady=5)


    laundry_recieved_btn=Button(laundry_recieved_frame,text='Save',command=recieve_complete,font=('Helvetica',15))
    laundry_recieved_btn.grid(row=4,column=2,ipadx=30,padx=10,pady=5)
    laundry_recieved_frame.grid(row=0,column=0)

def search_laundry_bet_dates():
    date1=day_between_1.get()
    date2=day_between_2.get()
    laundry_box_frame.grid_forget()
    root.geometry("1350x700+0+0")
    search_laundry_bet_date_frame.grid_forget()
    date1="'"+date1+"'"
    date2="'"+date2+"'"
    con=sqlite3.connect('Hotel_mgmt.db')
    c=con.cursor()
    c.execute('select * from sent_laundry where date between'+date1+'and'+date2)
    res=c.fetchall()
    table=ttk.Treeview(search_laundry_bet_date_frame,selectmode='browse')

    table.grid(row=2,column=0,sticky = ('N,S,W,E'))
    table['columns']=('1','2','3','4','5','6','7','8')
    table['show']='headings'
    table.heading('1',text='Double Bed Sheet')
    table.column("1",minwidth=0,width=80,anchor='c')
    table.heading('2',text='Single bed Sheet')
    table.column("2",minwidth=0,width=120,anchor='c')
    table.heading('3',text='Double Duet Cover')
    table.column("3",minwidth=0,width=100,anchor='c')
    table.heading('4',text='Cushion Cover')
    table.column("4",minwidth=0,width=50,anchor='c')
    table.heading('5',text='Bed Runner')
    table.column("5",minwidth=0,width=80,anchor='c')
    table.heading('6',text='Towel')
    table.column("6",minwidth=0,width=100,anchor='c')
    table.heading('7',text='Bath Towel')
    table.column("7",minwidth=0,width=50,anchor='c')
    table.heading('8',text='Date')
    table.column("8",minwidth=0,width=100,anchor='c')
    print_records=''
    for record in res:
        count=1
        print_records+=str(record)+'\n'
        table.insert("", 'end', text =str(count),values =(record[0], record[1], record[2],record[3],record[4],record[5],record[6],record[7]))
        count+=1

    #query_label=Label(search_by_date_frame,text=print_records)
    search_laundry_bet_date_frame.grid(row=1,column=0,columnspan=18)
    show_send_laundry_frame.grid(row=0,column=0)

    con.commit()
    con.close()

def show_sent_laundry():
    laundry_box_frame.grid_forget()
    show_send_laundry_frame.grid_forget()
    root.geometry("1350x700+0+0")
    label=Label(show_send_laundry_frame,text='Send Laundry',font=('Helvetica',30),pady=10)
    label.grid(row=0,column=7)
    back_button=Button(show_send_laundry_frame,image=back_button_img,command=lambda:back_home('show_send_laundry_frame'))
    back_button.image=back_button_img
    back_button.grid(row=0,column=0)
    global day_between_1
    day_between_1=Entry(show_send_laundry_frame)
    global day_between_2
    day_between_2=Entry(show_send_laundry_frame)
    date=datetime.date.today()
    day_between_2.insert(0,date)
    global day_between_btn
    day_between_btn=Button(show_send_laundry_frame,text='Search Between Dates',command=search_laundry_bet_dates)
    day_between_1.grid(row=1,column=6,sticky='E',padx=30,pady=10)
    day_between_2.grid(row=1,column=7,sticky='E',padx=30,pady=10)
    day_between_btn.grid(row=1,column=8,sticky='E',padx=30,pady=10)
    show_send_laundry_frame.grid(row=0,column=0,ipady=50,ipadx=100)

def search_rec_laundry_bet_dates():
    date1=day_between_1.get()
    date2=day_between_2.get()
    laundry_box_frame.grid_forget()
    root.geometry("1350x700+0+0")

    search_rec_laundry_bet_date_frame.grid_forget()
    date1="'"+date1+"'"
    date2="'"+date2+"'"
    con=sqlite3.connect('Hotel_mgmt.db')
    c=con.cursor()
    c.execute('select * from laundry where date between'+date1+'and'+date2)
    res=c.fetchall()
    table=ttk.Treeview(search_rec_laundry_bet_date_frame,selectmode='browse')

    table.grid(row=2,column=0,sticky = ('N,S,W,E'))
    table['columns']=('1','2','3','4','5','6','7','8')
    table['show']='headings'
    table.heading('1',text='Double Bed Sheet')
    table.column("1",minwidth=0,width=80,anchor='c')
    table.heading('2',text='Single bed Sheet')
    table.column("2",minwidth=0,width=120,anchor='c')
    table.heading('3',text='Double Duet Cover')
    table.column("3",minwidth=0,width=100,anchor='c')
    table.heading('4',text='Cushion Cover')
    table.column("4",minwidth=0,width=50,anchor='c')
    table.heading('5',text='Bed Runner')
    table.column("5",minwidth=0,width=80,anchor='c')
    table.heading('6',text='Towel')
    table.column("6",minwidth=0,width=100,anchor='c')
    table.heading('7',text='Bath Towel')
    table.column("7",minwidth=0,width=50,anchor='c')
    table.heading('8',text='Date')
    table.column("8",minwidth=0,width=100,anchor='c')
    print_records=''
    for record in res:
        count=1
        print_records+=str(record)+'\n'
        table.insert("", 'end', text =str(count),values =(record[0], record[1], record[2],record[3],record[4],record[5],record[6],record[7]))
        count+=1

    #query_label=Label(search_by_date_frame,text=print_records)
    search_rec_laundry_bet_date_frame.grid(row=1,column=0,columnspan=18)
    show_rec_laundry_frame.grid(row=0,column=0)

    con.commit()
    con.close()


def show_rec_laundry():
    laundry_box_frame.grid_forget()
    label=Label(show_rec_laundry_frame,text='Recieved Laundry',font=('Helvetica',30),pady=10)
    label.grid(row=0,column=3)
    root.geometry("1350x700+0+0")
    back_button=Button(show_rec_laundry_frame,image=back_button_img,command=lambda:back_home('show_rec_laundry_frame'))
    back_button.image=back_button_img
    back_button.grid(row=0,column=0)
    global day_between_1
    day_between_1=Entry(show_rec_laundry_frame)
    global day_between_2
    day_between_2=Entry(show_rec_laundry_frame)
    date=datetime.date.today()
    day_between_2.insert(0,date)
    global day_between_btn
    day_between_btn=Button(show_rec_laundry_frame,text='Search Between Dates',command=search_rec_laundry_bet_dates)
    day_between_1.grid(row=1,column=2,sticky='E',padx=30,pady=10)
    day_between_2.grid(row=1,column=3,sticky='E',padx=30,pady=10)
    day_between_btn.grid(row=1,column=4,sticky='E',padx=30,pady=10)
    show_rec_laundry_frame.grid(row=0,column=0,ipady=50,ipadx=100)

def laundry_box():
    inventory_frame.grid_forget()
    label=Label(laundry_box_frame,text='Laundry Box',font=('Helvetica',16),pady=10)
    label.grid(row=0,column=1)
    root.geometry("1350x700+0+0")
    home_img=ImageTk.PhotoImage(Image.open('images//hotel_logo.jpg'))
    home_img_label=Label(laundry_box_frame,image=home_img)
    home_img_label.image=home_img
    home_img_label.grid(row=1,column=0,columnspan=3)
    back_button=Button(laundry_box_frame,image=back_button_img,command=lambda:back_home('laundry_box_frame'))
    back_button.image=back_button_img
    back_button.grid(row=0,column=0)
    send_for_laundry_btn=Button(laundry_box_frame,text='Send For Laundry',command=send_laundry)
    send_for_laundry_btn.grid(row=2,column=1,padx=10,pady=8,ipadx=17)
    laundry_recieved_btn=Button(laundry_box_frame,text='Laundry Recieved',command=laundry_recieved)
    laundry_recieved_btn.grid(row=3,column=1,padx=10,pady=8,ipadx=18)
    show_sent_laundry_btn=Button(laundry_box_frame,text='Show sent Laundry',command=show_sent_laundry)
    show_sent_laundry_btn.grid(row=4,column=1,padx=10,pady=8,ipadx=16)
    show_rec_laundry_btn=Button(laundry_box_frame,text='Show Recieved Laundry',command=show_rec_laundry)
    show_rec_laundry_btn.grid(row=5,column=1,padx=10,pady=8)
    laundry_box_frame.grid(row=0,column=0)

def inventory():
    home_frame.grid_forget()
    inventory_frame.grid(row=0,column=0)
    label=Label(inventory_frame,text='Inventory',font=('Helvetica',16),pady=10)
    label.grid(row=0,column=1)
    root.geometry("1350x700+0+0")
    home_img=ImageTk.PhotoImage(Image.open('images//hotel_logo.jpg'))
    home_img_label=Label(inventory_frame,image=home_img)
    home_img_label.image=home_img
    home_img_label.grid(row=1,column=0,pady=20,columnspan=3)
    back_button=Button(inventory_frame,image=back_button_img,command=lambda:back_home('inventory_frame'))
    back_button.image=back_button_img
    back_button.grid(row=0,column=0)
    laundry_box_btn=Button(inventory_frame,text='Laundry Box',command=laundry_box)
    laundry_box_btn.grid(row=2,column=1,ipadx=30,padx=10,pady=10)
    view_current_stock=Button(inventory_frame,text='Current Stock',command=current_stock)
    view_current_stock.grid(row=3,column=1,ipadx=30,padx=10,pady=10)
    edit_stock_btn=Button(inventory_frame,text='Edit Stock',command=edit_stock)
    edit_stock_btn.grid(row=4,column=1,ipadx=40,padx=10,pady=10)
    home_frame.grid_forget()
    inventory_frame.grid(row=0,column=0,ipady=40)



def check_out_complete(room_no):
    #getting data from check in Table
    con=sqlite3.connect('hotel_mgmt.db')
    c=con.cursor()
    c.execute('select *,oid from check_in_data where room_no='+room_no)
    res=c.fetchall()
    result=[]
    for record in res:
        result.append(record[0])
        result.append(record[1])
        result.append(record[2])
        result.append(record[3])
        result.append(record[4])
        result.append(record[5])
        result.append(record[6])
        result.append(record[7])
        result.append(record[8])
        result.append(record[9])
        result.append(record[10])
        result.append(record[11])
        result.append(record[12])
        result.append(record[13])
        result.append(record[14])
        result.append(record[15])
        result.append(record[16])
        result.append(record[17])
    con.commit()
    con.close()

    con=sqlite3.connect('hotel_mgmt.db')
    c=con.cursor()
    check_out=datetime.date.today()
    #c.execute('insert into bookings values(:name,:address,:id_no,:age,:city,:phn_no,:gender,:company,:email,:fname,:id_type,:arrival_from,:purpose,:tarrif,:check_in_date,:room_no,:check_out_date,:no_of_person)',{'name':result[0],'address':result[1],'id_no':result[2],'age':result[3],'city':result[4],'phn_no':result[5],'gender':result[6],'company':result[7],'email':result[8],'fname':result[9],'id_type':result[10],'arrival_from':result[11],'purpose':result[12],'tarrif':result[13],'check_in_date':result[14],'room_no':result[15],'check_out_date':check_out_date,'no_of_person':result[16]})


    c.execute('update bookings set check_out_date=:check_out where phn_no=:number and check_in_date=:check_in',{'check_out':check_out,'number':result[5],'check_in':result[14]})
    con.commit()
    con.close()
    con=sqlite3.connect('hotel_mgmt.db')
    c=con.cursor()
    c.execute('delete from check_in_data where room_no='+room_no)
    con.commit()
    con.close()
    check_out_frame.grid_forget()
    home_frame.grid(row=0,column=0)

def check_out():
    home_frame.grid_forget()
    back_button=Button(check_out_frame,image=back_button_img,command=lambda:back_home('check_out_frame'))
    root.geometry("1350x700+0+0")
    back_button.image=back_button_img
    select_room_label=Label(check_out_frame,text='Click on the room to check out',font=('Helvetica',25))
    select_room_label.grid(row=0,column=1,columnspan=4)

    select_room_frame.grid_forget()

    con=sqlite3.connect('hotel_mgmt.db')
    c=con.cursor()
    c.execute('select * from check_in_data')
    res=c.fetchall()

    room_001=Button(check_out_frame,image=vac_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 001',compound=TOP)
    room_001.image=vac_room_img

    room_002=Button(check_out_frame,image=vac_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 002',compound=TOP)
    room_002.image=vac_room_img

    room_101=Button(check_out_frame,image=vac_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 101',compound=TOP)
    room_101.image=vac_room_img

    room_102=Button(check_out_frame,image=vac_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 102',compound=TOP)
    room_102.image=vac_room_img

    room_103=Button(check_out_frame,image=vac_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 103',compound=TOP)
    room_103.image=vac_room_img

    room_104=Button(check_out_frame,image=vac_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 104',compound=TOP)
    room_104.image=vac_room_img

    room_105=Button(check_out_frame,image=vac_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 105',compound=TOP)
    room_105.image=vac_room_img

    room_106=Button(check_out_frame,image=vac_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 106',compound=TOP)
    room_106.image=vac_room_img

    room_201=Button(check_out_frame,image=vac_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 201',compound=TOP)
    room_201.image=vac_room_img

    room_202=Button(check_out_frame,image=vac_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 202',compound=TOP)
    room_202.image=vac_room_img

    room_203=Button(check_out_frame,image=vac_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 203',compound=TOP)
    room_203.image=vac_room_img

    room_204=Button(check_out_frame,image=vac_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 204',compound=TOP)
    room_204.image=vac_room_img

    room_205=Button(check_out_frame,image=vac_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 205',compound=TOP)
    room_205.image=vac_room_img

    room_206=Button(check_out_frame,image=vac_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 206',compound=TOP)
    room_206.image=vac_room_img

    room_301=Button(check_out_frame,image=vac_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 301',compound=TOP)
    room_301.image=vac_room_img

    room_302=Button(check_out_frame,image=vac_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 302',compound=TOP)
    room_302.image=vac_room_img

    room_303=Button(check_out_frame,image=vac_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 303',compound=TOP)
    room_303.image=vac_room_img

    room_304=Button(check_out_frame,image=vac_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 304',compound=TOP)
    room_304.image=vac_room_img

    for number in res:
        if number[15]=='1':
            room_001=Button(check_out_frame,image=occ_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 001',compound=TOP,command=lambda:check_out_complete('1'))
            room_001.image=occ_room_img
        if number[15]=='2':
            room_002=Button(check_out_frame,image=occ_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 002',compound=TOP,command=lambda:check_out_complete('2'))
            room_002.image=occ_room_img
        if number[15]=='101':
            room_101=Button(check_out_frame,image=occ_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 101',compound=TOP,command=lambda:check_out_complete('101'))
            room_101.image=occ_room_img
        if number[15]=='102':
            room_102=Button(check_out_frame,image=occ_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 102',compound=TOP,command=lambda:check_out_complete('102'))
            room_102.image=occ_room_img
        if number[15]=='103':
            room_103=Button(check_out_frame,image=occ_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 103',compound=TOP,command=lambda:check_out_complete('103'))
            room_103.image=occ_room_img
        if number[15]=='104':
            room_104=Button(check_out_frame,image=occ_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 104',compound=TOP,command=lambda:check_out_complete('104'))
            room_104.image=occ_room_img
        if number[15]=='105':
            room_105=Button(check_out_frame,image=occ_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 105',compound=TOP,command=lambda:check_out_complete('105'))
            room_105.image=occ_room_img
        if number[15]=='106':
            room_106=Button(check_out_frame,image=occ_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 106',compound=TOP,command=lambda:check_out_complete('106'))
            room_106.image=occ_room_img
        if number[15]=='201':
            room_201=Button(check_out_frame,image=occ_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 201',compound=TOP,command=lambda:check_out_complete('201'))
            room_201.image=occ_room_img
        if number[15]=='202':
            room_202=Button(check_out_frame,image=occ_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 202',compound=TOP,command=lambda:check_out_complete('202'))
            room_202.image=occ_room_img
        if number[15]=='203':
            room_203=Button(check_out_frame,image=occ_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 203',compound=TOP,command=lambda:check_out_complete('203'))
            room_104.image=occ_room_img
        if number[15]=='204':
            room_204=Button(check_out_frame,image=occ_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 204',compound=TOP,command=lambda:check_out_complete('204'))
            room_204.image=occ_room_img
        if number[15]=='205':
            room_205=Button(check_out_frame,image=occ_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 205',compound=TOP,command=lambda:check_out_complete('205'))
            room_205.image=occ_room_img
        if number[15]=='206':
            room_206=Button(check_out_frame,image=occ_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 206',compound=TOP,command=lambda:check_out_complete('206'))
            room_206.image=occ_room_img
        if number[15]=='301':
            room_301=Button(check_out_frame,image=occ_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 301',compound=TOP,command=lambda:check_out_complete('301'))
            room_301.image=occ_room_img
        if number[15]=='302':
            room_302=Button(check_out_frame,image=occ_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 302',compound=TOP,command=lambda:check_out_complete('302'))
            room_302.image=occ_room_img
        if number[15]=='303':
            room_303=Button(check_out_frame,image=occ_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 303',compound=TOP,command=lambda:check_out_complete('303'))
            room_303.image=occ_room_img
        if number[15]=='304':
            room_304=Button(check_out_frame,image=occ_room_img,padx=20,pady=20,font=('Helvetica',10),text='room 304',compound=TOP,command=lambda:check_out_complete('304'))
            room_304.image=occ_room_img

    room_001.grid(row=1,column=0,padx=15,pady=10)
    room_002.grid(row=1,column=1,padx=15,pady=10)
    room_101.grid(row=2,column=0,padx=15,pady=10)
    room_102.grid(row=2,column=1,padx=15,pady=10)
    room_103.grid(row=2,column=2,padx=15,pady=10)
    room_104.grid(row=2,column=3,padx=15,pady=10)
    room_105.grid(row=2,column=4,padx=15,pady=10)
    room_106.grid(row=2,column=5,padx=15,pady=10)
    room_201.grid(row=3,column=0,padx=15,pady=10)
    room_202.grid(row=3,column=1,padx=15,pady=10)
    room_203.grid(row=3,column=2,padx=15,pady=10)
    room_204.grid(row=3,column=3,padx=15,pady=10)
    room_205.grid(row=3,column=4,padx=15,pady=10)
    room_206.grid(row=3,column=5,padx=15,pady=10)
    room_301.grid(row=4,column=0,padx=15,pady=10)
    room_302.grid(row=4,column=1,padx=15,pady=10)
    room_303.grid(row=4,column=2,padx=15,pady=10)
    room_304.grid(row=4,column=3,padx=15,pady=10)
    back_button.grid(row=0,column=0)

    check_out_frame.grid(row=0,column=0)


def home():
    home_img=ImageTk.PhotoImage(Image.open('images//hotel_logo.jpg'))
    home_img_label=Label(home_frame,image=home_img)
    home_img_label.image=home_img
    home_img_label.grid(row=0,column=0,pady=20)
    root.geometry("1350x700+0+0")
    root.configure(background='SystemButtonFace')
    new_booking_btn=Button(home_frame,text='New Check In',command=newcheckin)
    new_booking_btn.grid(row=1,column=0,padx=10,pady=10,columnspan=2,ipadx=8,ipady=2)

    user_option_btn=Button(home_frame,text='User Options',command=useroptions)
    user_option_btn.grid(row=2,column=0,padx=10,pady=10,columnspan=2,ipadx=12,ipady=2)

    search_booking_btn=Button(home_frame,text='Show Bookings', command=show_booking)
    search_booking_btn.grid(row=4,column=0,padx=10,pady=10,columnspan=2,ipadx=2,ipady=2)

    room_status_btn=Button(home_frame,text='Room Status', command=room_status)
    room_status_btn.grid(row=5,column=0,padx=10,pady=10,columnspan=2,ipadx=13)

    inventory_btn=Button(home_frame,text='Manage Inventory',command=inventory)
    inventory_btn.grid(row=6,column=0,padx=10,pady=10,columnspan=2)

    check_out_btn=Button(home_frame,text='Check Out',command=check_out)
    check_out_btn.grid(row=7,column=0,padx=10,pady=10,columnspan=2,ipadx=18)


    home_frame.grid(row=0,column=0)
#creating or connecting to Database
con=sqlite3.connect('hotel_mgmt.db')

#create cursor
c=con.cursor()

#creating Table
#c.execute("""
#create table user(userid text, password text, name text)
#""")

#Login Frame
username_label=Label(login_frame,text='User Name:')
username_label.grid(row=0,column=0,pady=3)
password_label=Label(login_frame,text='Password:')
password_label.grid(row=1,column=0,pady=3)

username=Entry(login_frame,width=30)
username.grid(row=0,column=1)
password=Entry(login_frame,width=30,show='*')
password.grid(row=1,column=1)

login_btn=Button(login_frame, text='Login', command=login,width=15)
login_btn.grid(row=2,column=1, columnspan=2, padx=10,pady=5)

con.commit()
con.close()
mainloop()
