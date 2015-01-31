'''
Exercise 16.5
'''
import copy

class Time(object):
    '''Represents the time of day.

    attributes: hour, minute, second
    '''
def print_time(time):
    print '%2d:%2d:%2d' % (time.hour, time.minute, time.second)

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def increment(time, seconds):
    new_time = time_to_int(time)
    new_time += seconds
    return int_to_time(new_time)

def main():
    time = Time()
    time.hour = 1
    time.minute = 20
    time.second = 15
    print_time(increment(time, 200))

main()
