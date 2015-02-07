'''
Exercise 17.7

Sources:
http://www.greenteapress.com/thinkpython/code/GoodKangaroo.py
- How to do the __str__ method
'''

class Kangaroo(object):
    def __init__(self):
        '''
        Kangaroo init function that initializes the attribute
        pouch_contents to an empty list.
        '''
        self.pouch_contents = []

    def put_in_pouch(self, any_type):
        '''
        Takes in an object of any type and adds it to the current
        objects pouch_contents.
        '''
        self.pouch_contents.append(any_type)

    def __str__(self):
        '''
        Returns a representation of the kangaroo object and
        its contents
        '''
        t = [ object.__str__(self) + ' with pouch contents:' ]
        for obj in self.pouch_contents:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

def main():
    kanga = Kangaroo()
    roo = Kangaroo()
    kanga.put_in_pouch(roo)
    print kanga


if __name__ == '__main__':
    main()
