'''
Exercise 8.10
'''

def is_palindrome(s):
    return s == s[::-1]

def main():
    s = 'racecar'
    s = 'hello'
    s = 'noon'
    print is_palindrome(s)

main()
