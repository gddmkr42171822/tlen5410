'''
Exercise 6.2
'''
'''
Step 1
-------
Outline function

def hypotenuse(l1, l2):
    print 0
'''

'''
Step 2
-------
Define equation to find hypotenuse
c = math.sqrt(a**2 + b**2)
find library to do math functions

import math

def hypotenuse(l1, l2):
    c = math.sqrt(l1**2 + l2**2)
    print c
'''

'''
Step 3
-------
After verifying the function does what it is supposed
return the result
'''
import math

def hypotenuse(l1, l2):
    c = math.sqrt(l1**2 + l2**2)
    return c



def main():
    print hypotenuse(3, 4)

main()
