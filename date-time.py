#pip install holidays
import datetime
from datetime import date, time
import holidays
import birthday_list

now = datetime.datetime.now()
us_holidays = holidays.US()

formatted_date = now.strftime("%Y, %m, %d")
year = int(now.strftime("%Y"))
month = int(now.strftime("%m"))
day = int(now.strftime("%d"))
formatted_time = now.strftime("%H:%M:%S")

birthdays = birthday_list.get_birthdays()


def check_national_holidays():
    #checks if today is a US holiday
    if date(year,month,day) in us_holidays:
        return us_holidays.get(year,month,day)
    else:
        return False

def check_birthdays():
    #checks if today is anyone's birthday
    for name, bday in birthdays.items():
        if (bday.month, bday.day) == (month, day):
            age = year - bday.year
            return name, age
    return False

def check_time():
    if now.time() >= time(5,0,0) and now.time() < time(12,0,0):
        #between 5am and noon
        return "Morning"

    elif now.time() >= time(12,0,0) and now.time() < time(5,0,0):
        #between noon and 5pm
        return "Afternoon"

    elif now.time() >= time(5,0,0) and now.time() < time(9,0,0):
        #between 5pm and 9pm
        return "Evening"
    
    elif now.time() >= time(9,0,0) and now.time() < time(5,0,0):
        #between 9pm and 5am
        return "Night"

def get_age_suffix(age):
    remainder = age % 10
    if remainder == 1:
        return "st"
    if remainder == 2:
        return "nd"
    if remainder == 3:
        return "rd"
    else:
        return "th"


def main():

    if check_birthdays():
        #check birthdays first
        name, age = check_birthdays()
        if name == "Dad":
            #check for dad's birthday
            print_str = "Happy Birthday, Dad!"

        elif age < 50:
            #check for birthdays with ages
            suffix = get_age_suffix(age)
            print_str = "It's " + name + "'s " + str(age) + suffix + " B-day!"

        else:
            print_str = "It's " + name + "'s B-day!"
        
        return print_str

    elif check_national_holidays():
        #check national holidays second
        if check_national_holidays() != "Christmas":
            print_str = "Happy " + check_national_holidays() + ", Dad!"
        else:
            print_str = "Merry Christmas, Dad!"

        return print_str
    
    else:
        print_str = "Good " + check_time() + ", Dad"
        return print_str
    
print(main())