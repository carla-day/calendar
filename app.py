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
cal = Calendar(root, selectmode = 'day', year = day.year, 
month = day.month, day = day.day, date_pattern = "mm-dd-Y")

cal.pack(pady=20)

def grad_date():
    cal_str = str(cal.get_date())
    no_holiday = True
    if (cal_str in holidays.US()):
        day.config(text = cal.get_date() + " is " + holidays.US().get(cal_str))
    
    for i in new_holidays:
        if i['day'] == cal_str:
            day.config(text = cal.get_date() + " is " + i['holiday'])
        else:
            no_holiday = False

    #if the date is in holidays import or created holidays dict
    
    if (no_holiday == False) and (cal_str not in holidays.US()):
        day.config(text = "Selected date is not a holiday")
#empty dict
new_holidays = []

# Add Button and Label
Button(root, text = "Is it a holiday?",
	command = grad_date).pack(pady = 20)

#create text box
text = Text(root, width=10, height=1)
text.pack(pady=20)

#clear function
def clear():
    text.delete(1.0, END)

#add date function
def add_holiday():
    new_date= str(cal.get_date)
    holiday= text.get(1.0, END)
    new_holidays.append({"date": new_date, "holiday": holiday})

btn_frame = Frame(root)
btn_frame.pack()

add_btn = Button(btn_frame, text = "Add Holiday",
	command = add_holiday)
add_btn.pack(pady = 20)

clear_btn = Button(btn_frame, text="Clear Text",
command=clear)
clear_btn.pack(pady = 20)

date = Label(root, text = "")
date.pack(pady = 20)

# Execute Tkinter
root.mainloop()

