# Import Required Library
from tkinter import *
from tkcalendar import Calendar
from datetime import datetime
import holidays
import new_days
# Create Object
root = Tk()
#get date
day = datetime.now()
# Set size
root.geometry("700x1000")
root.title("Check for Holidays")

# Add Calendar
cal = Calendar(root, selectmode = 'day', year = day.year, 
month = day.month, day = day.day, date_pattern = "mm-dd-Y")

cal.pack(pady=20)

def grad_date():
    cal_str = str(cal.get_date())
    no_holiday = True
    
    if (cal_str in holidays.US()):
        date.config(text = cal.get_date() + " is " + holidays.US().get(cal_str))
        no_holiday = True
    if len(new_days.new_holidays)== 0:
        print("Stuck in length")
        no_holiday =False
    if(len(new_days.new_holidays)>0):

        for i in new_days.new_holidays:
            if i['day'] == cal_str:
                print("FOUND MATCHING STRING")
                date.config(text = cal.get_date() + " is " + i['holiday'])
                no_holiday =True
                break
            else:
                no_holiday = False
           
    #if the date is in holidays import or created holidays dict
    if (no_holiday == False) and (cal_str not in holidays.US()):
        date.config(text = "Selected date is not a holiday")
        print(new_days.new_holidays)


# Add Button and Label
Button(root, text = "Is it a holiday?",
	command = grad_date, width=10, height=2).pack(pady = 1)

#create text box
text = Text(root, width= 20, height=2 )
text.pack(pady=1)

#clear function
def clear():
    text.delete(1.0, END)

#add date function
def add_holiday():
    new_date= str(cal.get_date())

    holiday= text.get(1.0, END)
    new_days.new_holidays.append({"day": new_date, "holiday": holiday})


add_btn = Button(root, text = "Add Holiday", width=10, height=2,
	command = add_holiday)

clear_btn = Button(root, text="Clear Text", width=10, height=2,
command=clear)

add_btn.pack(pady=1)

clear_btn.pack(pady=1)


date = Label(root, text = "")
date.pack(pady = 20)


# add a line to remove duplicates from the list for cleaner code


# Execute Tkinter
root.mainloop()

