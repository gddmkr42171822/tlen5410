def has_duplicates(t):
    u = t
    u.sort()
    for x in range(0, len(u)-1):
        if u[x] == u[x+1]:
            return True
    return False

def main():
    print has_duplicates([1, 2, 3, 4])
    print has_duplicates([1, 3, 4, 5, 3])

main()
