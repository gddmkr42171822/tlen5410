'''
Exercise 16.1
'''
class Time(object):
    '''Represents the time of day.

    attributes: hour, minute, second
    '''
def print_time(time):
    print '%2d:%2d:%2d' % (time.hour, time.minute, time.second)

def main():
    time = Time()
    time.hour = 11
    time.minute = 59
    time.second = 30
    print_time(time)

main()
