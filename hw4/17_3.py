'''
Exercies 17.3
'''

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '%d:%d' % (self.x, self.y)

def main():
    point = Point(4, 5)
    print point

if __name__ == '__main__':
    main()
