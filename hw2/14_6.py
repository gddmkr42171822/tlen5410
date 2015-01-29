'''
https://stackoverflow.com/questions/4071396/split-by-comma-and-strip-whitespace-in-python
-How to split on commas

http://tartley.com/?p=1349
-How to do regexes

https://docs.python.org/2/library/string.html
-How to use find on a string
'''

import urllib
import re

def get_userinput():
    user_zip = raw_input('Enter a zipcode to look up: ')
    return user_zip

def get_zipinfo(zip):
    url = 'http://www.uszip.com/zip/' + zip
    print url
    conn = urllib.urlopen(url)
    for line in conn:
        line = line.strip()
        if 'Total population' in line:
            i = line.find('Total population')
            line = line[i:]
            line = re.sub(r'[^,\d]+', " ", line)
            line = line.split()
            print 'Population: ' + line[0]
        if '<title>' in line:
            line = re.sub(r'[<>/]+(title)+[>]', '', line)
            line = line.replace('zip', '')
            line = line.replace('code', '')
            line = line.split(',')
            print 'Town Name: ' + line[0]

def main():
    zip = get_userinput()
    get_zipinfo(zip)

main()
