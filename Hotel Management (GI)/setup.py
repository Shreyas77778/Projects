import cx_Freeze
import sys
import matplotlib

base=None

if sys.platform=='win32':
    base='Win32GUI'
executables=[cx_Freeze.Executable("HotelManagement.py",base=base,icon='icon.ico')]

cx_Freeze.setup(
name='Hotel',
options={"build.exe":{"packages":{"tkinter","matplotlib"},"include_files":{"icon.ico","images/back_button.jpg","images/blue_room_status.png","images/hotel_logo.jpg","images/login_img.jpg","red_room_status.png","yellow_room_status.png","hotel_mgmt.db"}}},
version="0.01",
description="Hotel Management Application",
executables=executables



)
