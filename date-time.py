#pip install holidays
import datetime
from datetime import date, time
import holidays
import birthday_list

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
            if bday.year >= 1990:
                age = year - bday.year
                return name, age
            return name, _
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
    if 


def main():
    now = datetime.datetime.now()
    us_holidays = holidays.US()

    formatted_date = now.strftime("%Y, %m, %d")
    year = int(now.strftime("%Y"))
    month = int(now.strftime("%m"))
    day = int(now.strftime("%d"))
    formatted_time = now.strftime("%H:%M:%S")

    birthdays = birthday_list.get_birthdays()

    if check_birthdays():
        #check birthdays first
        name, age = check_birthdays()

        if name = "Dad":
            #check for dad's birthday
            print_str = "Happy Birthday, Dad!"

        elif age:
            #check for birthdays with ages
            print_str = "It's " + name + "'s " + age + "rd B-day!"


    elif check_national_holidays():
        #check national holidays second
        if check_national_holidays() != "Christmas":
            print_str = "Happy " + check_national_holidays() + ", Dad!"
        else:
            print_str = "Merry Christmas, Dad!"

        return print_str
    
    