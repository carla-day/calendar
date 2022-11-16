# Import Required Library
from tkinter import *
from tkcalendar import Calendar
from datetime import datetime
import holidays


# Create Object
root = Tk()
#get date
day = datetime.now()

# Set size
root.geometry("500x400")

# Add Calendar
cal = Calendar(root, selectmode = 'day',
			year = 2022, month = 11,
			day = 15, date_pattern = "mm-dd-Y")

cal.pack(pady = 20)

def grad_date():
    ''' if cal.get_date() in holidays:
        date.config(text = cal.get_date() + " is " + holidays.get(cal.get_date))
    else:
        date.config(text = "Selected Date is not a Holiday") '''
    
    print(type(cal.get_date))




# Add Button and Label
Button(root, text = "Is it a Holiday?",
	command = grad_date).pack(pady = 20)

date = Label(root, text = "")
date.pack(pady = 20)

# Execute Tkinter
root.mainloop()

