'''
Exercise 16.2
'''

class Time(object):
    '''Represents the time of day.

    attributes: hour, minute, second
    '''
def print_time(time):
    return '%2d:%2d:%2d' % (time.hour, time.minute, time.second)

def is_after(t1, t2):
    s1 = print_time(t1)
    s2 = print_time(t2)
    return s1 > s2

def main():
    t1 = Time()
    t2 = Time()
    t1.hour = 03
    t2.hour = 03
    t1.minute = 43
    t2.minute = 55
    t1.second = 05
    t2.second = 45
    print is_after(t1, t2)

main()
