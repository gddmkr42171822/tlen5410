'''
Exercise 16.4
'''
import copy

class Time(object):
    '''Represents the time of day.

    attributes: hour, minute, second
    '''
def print_time(time):
    print '%2d:%2d:%2d' % (time.hour, time.minute, time.second)

def increment(time, seconds):
    new_time = copy.copy(time)

    new_time.second += seconds % 60
    if new_time.second >= 60:
        new_time.seconds -= 60
        new_time.minute += 1
    new_time.minute += seconds/60
    if new_time.minute >= 60:
        new_time.minute -= 60
        new_time.hour += 1
    return new_time

def main():
    time = Time()
    time.hour = 1
    time.minute = 20
    time.second = 15
    print_time(increment(time, 200))

main()
