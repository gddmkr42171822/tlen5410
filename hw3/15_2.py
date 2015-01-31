'''
Exercise 15.2
'''
import math

class Rectangle(object):
    '''Represents a rectangle.
    attributes:width, height, corner.
    '''

class Point(object):
    '''Represents a point in 2-D space
    attributes: x coordinate, y coordinate
    '''

def move_rectangle(rect, dx, dy):
    rect.corner.x += dx
    rect.corner.y += dy

def main():
    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 0.0
    box.corner.y = 0.0
    move_rectangle(box, 1, 2)
    print box.corner.x, box.corner.y

main()
