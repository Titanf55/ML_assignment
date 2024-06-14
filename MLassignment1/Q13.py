from datetime import datetime
import calendar

user_date=input("enter your birth date ")
y = datetime.today().year
# m= datetime.today().month
# d = datetime.today().day

date_formats = ['%Y-%m-%d', '%m/%d/%Y', '%d-%m-%Y', '%Y.%m.%d']

for format_str in date_formats:
    try:
        birthdate= datetime.strptime(user_date, format_str).date()
        #Extract day and month if date was not written
        day = birthdate.day
        month = birthdate.month
        year=birthdate.year
        print("Day:", day)
        print("Month:", month)
        print("Month:", year)
        break  
    except ValueError:
        pass  
else:
    print("Invalid date format. Please enter date in one of the supported formats:", date_formats)
#birthdate = datetime.strptime(user_date,date_formats).date()
# def days_in_month(year, month):
#      return calendar.monthrange(year, month)[1]
#[1] after calendar.monthrange(year, month), you are accessing the second element 
# of the tuple, which stores the number of days in the specified month.
# print(f"Number of days in {calendar.month_name[month]}, {year}: {num_days}")
#print( days_in_month(year, month))

def days_until_birthday(birthdate):

    today = datetime.today().date()
    next_birthday = birthdate.replace(year=today.year)

    # If birthday has already occurred this year, calculate for next year
    if next_birthday < today:
        next_birthday = next_birthday.replace(year=today.year + 1)

    days_until = (next_birthday - today).days
    return days_until



days_left = days_until_birthday(birthdate)
print("Days left until your birthday:", days_left)

def age(year):
    Age=y-year
    return Age

print("your age is",age(year))

