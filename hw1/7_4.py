'''
Exercise 7_4
'''

def eval_loop():
    l = []
    while True:
        input = raw_input('Enter string to eval (or done): ')
        if input == 'done':
            print l[-1]
            break
        else:
            l.append(eval(input))
            print eval(input)

def main():
    eval_loop()

main()

