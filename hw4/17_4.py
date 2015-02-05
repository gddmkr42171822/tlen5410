'''
Exercise 17.4
'''

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '%d:%d' % (self.x, self.y)

    def __add__(self, other):
        self.x += other.x
        self.y += other.y
        return self

def main():
    point_a = Point(4, 5)
    point_b = Point(4, 5)
    print point_a + point_b

if __name__ == '__main__':
    main()

