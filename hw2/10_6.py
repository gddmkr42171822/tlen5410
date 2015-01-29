#https://stackoverflow.com/questions/3755136/pythonic-way-to-check-if-a-list-is-sorted-or-not

def is_sorted(t):
    for x in range(0, len(t)-1):
        if t[x] > t[x+1]:
            return False
    return True;

def main():
    print is_sorted([1, 2, 3])
    print is_sorted([3, 4, 2, 6])

main()

