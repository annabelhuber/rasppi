import datetime
from datetime import date, time
import holidays
import birthday_list


def check_national_holidays(us_holidays, year,month,day):
    curr_date=date(year,month,day)
    #checks if today is a US holiday
    if date(year,month,day) in us_holidays:
        #rename some of the holidays to shortened versions

        if us_holidays.get(curr_date) == "Martin Luther King Jr. Day":
            return "MLK Jr. Day"
        elif us_holidays.get(curr_date) == "Juneteenth National Independence Day":
            return "Juneteenth"
        elif us_holidays.get(curr_date) == "Washington's Birthday":
            return "President's Day"
        elif us_holidays.get(curr_date) == "Independence Day (observed)":
            return False
        
        return us_holidays.get(curr_date)
    
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
    elif (month,day) == (3,14):
        return "Pi Day"
    elif (month,day) == (1,2):
        return "Sci-Fi Day"
    elif (month,day) == (4,1):
        return "April Fool's Day"
    elif (month,day) == (11,23):
        return "Fibonacci Day"

    #holidays that change year to year (easter, mother's day, father's day)
    elif year == 2027:
        if (month,day) == (3,28):
            "Easter"
        elif (month,day) == (6,20):
            "Father's Day"
        elif (month,day) == (5,9):
            "Mother's Day"
        elif (month,day) == (8,4):
            "Engineer's Day"

    elif year == 2028:
        if (month,day) == (4,16):
            "Easter"
        elif (month,day) == (6,18):
            "Father's Day"
        elif (month,day) == (5,14):
            "Mother's Day"
        elif (month,day) == (8,2):
            "Engineer's Day"

    elif year == 2029:
        if (month,day) == (4,1):
            "Easter"
        elif (month,day) == (6,17):
            "Father's Day"
        elif (month,day) == (5,13):
            "Mother's Day"
        elif (month,day) == (8,1):
            "Engineer's Day"

    elif year == 2030:
        if (month,day) == (4,21):
            "Easter"
        elif (month,day) == (6,16):
            "Father's Day"
        elif (month,day) == (5,12):
            "Mother's Day"
        elif (month,day) == (8,7):
            "Engineer's Day"

    else:
        return False
    

def holidays_return_str(us_holidays,year,month,day):
    if check_national_holidays(us_holidays, year,month,day):
        if check_national_holidays(us_holidays, year,month,day) != "Christmas":
            print_str = "Happy " + check_national_holidays(us_holidays, year,month,day) + ", Dad!"
        else:
            print_str = "Merry Christmas, Dad!"

        return print_str
    return False


def check_birthdays(birthdays,year,month,day) -> str:
    #checks if today is anyone's birthday
    for name, bday in birthdays.items():
        if (bday.month, bday.day) == (month, day):
            age = year - bday.year
            return name, age
    return False

def birthday_return_str(birthdays,year,month,day):
    #get the final return string for birthdays
    #get name and age
    if check_birthdays(birthdays,year,month,day):
        name, age = check_birthdays(birthdays,year,month,day)

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
    return False

def check_time(now) -> str:
    if now.time() >= time(5,0,0) and now.time() < time(12,0,0):
        #between 5am and noon
        return "Morning"

    elif now.time() >= time(12,0,0) and now.time() < time(17,0,0):
        #between noon and 5pm
        return "Afternoon"

    elif now.time() >= time(17,0,0) and now.time() < time(21,0,0):
        #between 5pm and 9pm
        return "Evening"
    
    else:
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


def return_text(year=None,month=None,day=None):

    now = datetime.datetime.now()

    formatted_date = now.strftime("%Y, %m, %d")
    # year = int(now.strftime("%Y"))
    # month = int(now.strftime("%m"))
    # day = int(now.strftime("%d"))
    if not year:
        year=int(now.strftime("%Y"))
    if not month:
        month=int(now.strftime("%m"))
    if not day:
        day=int(now.strftime("%d"))
    formatted_time = now.strftime("%H:%M:%S")

    birthdays = birthday_list.get_birthdays()
    us_holidays = holidays.US(years=year)

    if check_birthdays(birthdays,year,month,day) and check_national_holidays(us_holidays,year,month,day):
        combo_print_str = ""
        #check birthdays first
        print_str1 = birthday_return_str(birthdays,year,month,day)
        
        print_str2 = holidays_return_str(us_holidays,year,month,day)
        
        combo_print_str = print_str1 + " " + print_str2
        return combo_print_str


    elif check_birthdays(birthdays, year,month,day):
        print_str = birthday_return_str(birthdays,year,month,day)
        
        return print_str

    elif check_national_holidays(us_holidays, year,month,day):
        #check national holidays second
        print_str = holidays_return_str(us_holidays,year,month,day)

        return print_str
    
    else:
        time_of_day = check_time(now)
        print_str = "Good " + time_of_day + ", Dad"
        return print_str
    


if __name__ == "__main__":
    #us_holidays = holidays.US()
    #print(us_holidays.get(2026,1,25))
    #print(check_national_holidays2(us_holidays,2027,11,25))
    print(return_text())
    
    #first: install holidays
    ##pip install holidays

    #to schedule:
    #bash: crontab -e (if prompted, choose 1 to open with nano text editor)
    #scroll to very bottom of file and add this line:
    #0 * * * * /usr/bin/python3 {absolute path to script}
    #Save and exit (Press Ctrl+O, Enter, then Ctrl+X to quit nano)