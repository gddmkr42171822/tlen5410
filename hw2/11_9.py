#http://www.greenteapress.com/thinkpython/code/has_duplicates.py

def has_duplicates(t):
    d = {}
    for x in t:
        if x in d:
            return True
        d[x] = x
    return False

def main():
    print has_duplicates([1, 2, 3, 4])
    print has_duplicates([1, 3, 4, 5, 3])

main()
