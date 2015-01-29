'''
Name: Robert Werthman

Lab 1: Obtain and Parse Configuration via tftp

Sources:
    https://stackoverflow.com/questions/21864192/most-elegant-way-to-format-multi-line-strings-in-python
    -How to do multiline string format print statement for printOut

    https://www.kumari.net/index.php/programming/programmingcat/22-python-making-a-dictionary-of-lists-a-hash-of-arrays
    -How to create a dictionary of lists

    https://stackoverflow.com/questions/5082452/python-string-formatting-vs-move f
    -How to do format strings in python

    https://stackoverflow.com/questions/8858008/moving-a-file-in-python
    -How to rename a file

    https://stackoverflow.com/questions/8858008/moving-a-file-in-python
    -How to create sequential file names

    https://stackoverflow.com/questions/509211/explain-pythons-slice-notation
    -Get last char in python string

    http://www.sontek.net/blog/2010/10/28/convert_a_string_to_an_integer_in_python.html
    -Convert char to int

    https://stackoverflow.com/questions/3421523/what-exactly-does-a-non-shallow-filecmp-cmp-do
    -How to compare two files

'''

import tftpy
import os
import filecmp

'''
Descriptoin: prints out ip, hostname, and version to command line
Input: dictionary with ip, hostname, and version
Output:
'''

def printOut(x, d):
    print 'Saving new config for ' + x + ' (' + d[x][1] + ') '\
    'running IOS version ' + d[x][0]

'''
Description: Parses config; puts hostname and version in dictionary
Input: list of ip address, empty dictionary
Output: dictionary with values: hostname, version; key: ip address
'''
def readFile(l, d):
    for x in l:
        f = open(x)
        for line in f:
            line = line.strip()
            if 'version' in line:
                d[x] = []
                d[x].append(line[8:])
                #print d[x][0]
            elif 'hostname' in line:
                d[x].append(line[9:])
                #print d[x][1]
        f.close()

'''
Description: Grabs config file from router
Input: list of ip address
Output: new files with router configs
'''
def getConfig(l):
    for x in l:
        connection = tftpy.TftpClient(x, 69)
        connection.download('/startup-config','/home/netman/Desktop/' + x)

'''
Description: Gets user input and appends it to a list
Input: a list
Output: list with user supplied ip addresses
'''
def getInput(l):
    while True:
        input = raw_input('Enter management IP (or done): ')
        if input == 'done':
            return
        else:
            l.append(input)

'''
Description: Creates router directory if it doesn't exist
Input: dictionary
Output: Saves config file or there are no changes
'''
def saveConfig(d):
    for x in d:
        path = '/home/netman/Desktop/{0}/'.format(d[x][1])
        if os.path.exists(path):
            print "Configs exist for {0}!".format(d[x][1])
            compareConfigs(x, path, d)
        else:
            print "Creating new directory for {0}!".format(d[x][1])
            printOut(x, d)
            os.mkdir('/home/netman/Desktop/' + d[x][1])
            os.rename('/home/netman/Desktop/' + x, '/home/netman/'\
            'Desktop/{0}/{0}_v1'.format(d[x][1]))

'''
Description: Checks the differenc ein a file
Input: ip address, path to old configs, dictionary
Output: saves new config or finds no changes
'''
def compareConfigs(x, path, d):
    l = []
    for filename in os.listdir(path):
        l.append(filename[-1])
    if filecmp.cmp('/home/netman/Desktop/' + x, path + d[x][1] + \
    '_v' + max(l)):
        print "No changes!"
        os.remove('/home/netman/Desktop/' + x)
    else:
        printOut(x, d)
        v = str(int(max(l))+1)
        os.rename('/home/netman/Desktop/' + x, '/home/netman/'\
        'Desktop/{0}/{0}_v{1}'.format(d[x][1], v))

def main():
    l = []
    d = {}
    getInput(l)
    getConfig(l)
    readFile(l, d)
    saveConfig(d)

main()



