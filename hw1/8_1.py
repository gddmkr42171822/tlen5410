'''
Exercise 8.1

https://stackoverflow.com/questions/766141/reverse-a-string-in-python
- How to reverse a string
'''

def backwardsString(s):
    for char in reversed(s):
        print char

def main():
    s = 'banana'
    backwardsString(s)

main()

