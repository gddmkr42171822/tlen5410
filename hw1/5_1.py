'''
Name: Robert Werthman
HW2
Exercises 5.1, 6.2, 6.4, 7.4, 8.1, 8.3, 8.10, 8.12
'''

def print_n(s, n):
    if n <= 0:
        return
    print s
    print_n(s, n - 1)

Stack Diagram
------------------
<module> s = 'Hello'
         n = 2
print_n  s = 'Hello'
         n = 1
print_n  s = 'Hello'
         n = 0
