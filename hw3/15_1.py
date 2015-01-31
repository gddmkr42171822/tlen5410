'''
Exerciese 15.1
'''
import math

class Point(object):
    '''Represents a point in 2-D space
    attributes: x coordinate, y coordinate
    '''

def distance_between_points(p1, p2):
    '''Compute distance between two Point objects'''
    x = p1.x - p2.x
    y = p1.y - p2.y
    distance = math.sqrt(x**2 + y**2)
    return distance

def main():
    p1 = Point()
    p2 = Point()
    p1.x = 4
    p2.x = 4
    p1.y = 6
    p2.y = 6
    print distance_between_points(p1, p2)

main()
