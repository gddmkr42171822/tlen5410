'''
Exercise 17.4
'''

class Point(object):
    def __init__(self, x, y):
        '''
        Attributes: x coordinate, y coordinate
        '''
        self.x = x
        self.y = y

    def __str__(self):
        '''
        Prints the attriubtes of a Point object
        '''
        return '%d:%d' % (self.x, self.y)

    def __add__(self, other):
        '''
        Adds one point to another
        '''
        self.x += other.x
        self.y += other.y
        return self

def main():
    point_a = Point(4, 5)
    point_b = Point(4, 5)
    print point_a + point_b

if __name__ == '__main__':
    main()

