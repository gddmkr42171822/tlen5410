'''
Exercise 16.7 (1 & 2 only)

Sources:

pymotw.com/2/datetime/
-How to use the datetime module and format the day from a number to a
string

www.greenteapress.com/thinkpython/code/Time1_soln.py
-How to get the proper number of days until next birthday

'''

import datetime

class Time(object):
    '''Represents the time of day.

    attributes: hour, minute, second
    '''

def weekDay():
    today = datetime.date.today()
    print 'Current day is: ' + today.strftime('%A')

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def currentAge(birthday):
    today = datetime.date.today()
    age = today.year - birthday.year
    if birthday.month == today.month:
        if birthday.day > today.day:
            return (age - 1)
        else:
            return age
    elif birthday.month > today.month:
        return (age - 1)
    else:
        return age

def nextBirthday(birthday):
    today = datetime.datetime.now()
    next_birthday = datetime.datetime(today.year, birthday.month, \
    birthday.day)
    if today > next_birthday:
        next_birthday = datetime.datetime(today.year+1, birthday.month,\
        birthday.day)
    delta = next_birthday - today
    time = int_to_time(delta.seconds)
    print 'There are {0} days, {1} hours, {2} minutes, and {3} seconds'\
    ' until you next birthday!'\
    .format(delta.days, time.hour, time.minute, time.second)

def main():
    my_birthday = datetime.date(1989, 07, 11)
    weekDay()
    print 'Your age is: ' + str(currentAge(my_birthday))
    nextBirthday(my_birthday)


main()
