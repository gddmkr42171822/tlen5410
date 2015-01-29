'''
Exercise 8_12

https://stackoverflow.com/questions/4435169/good-way-to-append-to-a-string
- How to append to string
'''

def rotate_word(s, d):
    new_s = ''
    new_x = 0
    for x in s:
        if (ord(x) + d) > 122:
            new_x = (ord(x) + d) - 122 + 96
        elif (ord(x) + d) < 97:
            new_x = (ord(x) + d) - 97 + 123
        else:
            new_x = ord(x) + d
        new_s += chr(new_x)
    return new_s


def main():
    s = 'cubed'
    d = 10
    print rotate_word(s, d)

main()
