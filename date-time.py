#pip install holidays
import datetime
from datetime import date, time
import holidays
import birthday_list


def check_national_holidays(us_holidays, year,month,day):
    #checks if today is a US holiday
    if date(year,month,day) in us_holidays:
        #rename some of the holidays to shortened versions

        if us_holidays.get(year,month,day) == "Martin Luther King Jr. Day":
            return "MLK Jr. Day"
        if us_holidays.get(year,month,day) == "Juneteenth National Independence Day":
            return "Juneteenth"
        if us_holidays.get(year,month,day) == "Independence Day (observed)":
            return False
        
        return us_holidays.get(year,month,day)
    
    #add in some holidays not included
    elif (month,day) == (12,31):
        return "New Year's Eve"
    elif (month,day) == (12,24):
        return "Christmas Eve"
    elif (month,day) == (2,14):
        return "Valentine's Day"
    elif (month,day) == (3,17):
        return "St. Patrick's Day"
    elif (month,day) == (5,5):
        return "Cinco de Mayo"
    elif (month,day) == (10,31):
        return "Halloween"
    
    #holidays that change year to year (easter, mother's day, father's day)
    elif year == 2027:
        if (month,day) == (3,28):
            "Easter"
        elif (month,day) == (6,20):
            "Father's Day"
        elif (month,day) == (5,9):
            "Mother's Day"

    elif year == 2028:
        if (month,day) == (4,16):
            "Easter"
        elif (month,day) == (6,18):
            "Father's Day"
        elif (month,day) == (5,14):
            "Mother's Day"

    elif year == 2029:
        if (month,day) == (4,1):
            "Easter"
        elif (month,day) == (6,17):
            "Father's Day"
        elif (month,day) == (5,13):
            "Mother's Day"

    elif year == 2030:
        if (month,day) == (4,21):
            "Easter"
        elif (month,day) == (6,16):
            "Father's Day"
        elif (month,day) == (5,12):
            "Mother's Day"

    else:
        return False

def check_birthdays(birthdays,year,month,day):
    #checks if today is anyone's birthday
    for name, bday in birthdays.items():
        if (bday.month, bday.day) == (month, day):
            age = year - bday.year
            return name, age
    return False

def check_time(now):
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
    now = datetime.datetime.now()

    formatted_date = now.strftime("%Y, %m, %d")
    year = int(now.strftime("%Y"))
    month = int(now.strftime("%m"))
    day = int(now.strftime("%d"))
    formatted_time = now.strftime("%H:%M:%S")

    birthdays = birthday_list.get_birthdays()
    us_holidays = holidays.US(years=year)

   

    if check_birthdays(birthdays, year,month,day):
        #check birthdays first
        name, age = check_birthdays(birthdays, year,month,day)
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

    elif check_national_holidays(us_holidays, year,month,day):
        #check national holidays second
        if check_national_holidays(us_holidays, year,month,day) != "Christmas":
            print_str = "Happy " + check_national_holidays(us_holidays, year,month,day) + ", Dad!"
        else:
            print_str = "Merry Christmas, Dad!"

        return print_str
    
    else:
        print_str = "Good " + check_time(now) + ", Dad"
        return print_str
    


if __name__ == "__main__":

    print(main())