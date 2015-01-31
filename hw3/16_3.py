'''
Exercise 16.3
'''

class Time(object):
    '''Represents the time of day.

    attributes: hour, minute, second
    '''
def print_time(time):
    print '%2d:%2d:%2d' % (time.hour, time.minute, time.second)

def increment(time, seconds):
    time.second += seconds % 60
    if time.second >= 60:
        time.seconds -= 60
        time.minute += 1
    time.minute += seconds/60
    if time.minute >= 60:
        time.minute -= 60
        time.hour += 1

def main():
    time = Time()
    time.hour = 1
    time.minute = 20
    time.second = 15
    increment(time, 200)
    print_time(time)

main()
