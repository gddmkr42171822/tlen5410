'''
Exercise 17.5
'''

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '%d:%d' % (self.x, self.y)

    def __add__(self, other):
        point = Point(0, 0)
        if isinstance(other, Point):
            point.x = other.x + self.x
            point.y = other.y + self.y
            return point
        elif isinstance(other, tuple):
            point.x += other[0]
            point.y += other[1]
            return point

def main():
    point_a = Point(4, 5)
    point_b = Point(4, 5)
    t = 1, 2
    print point_a + point_b
    print point_a + t

if __name__ == '__main__':
    main()
