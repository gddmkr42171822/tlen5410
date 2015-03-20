'''

Lab 1: Obtain and Parse Configuration via tftp


'''

import tftpy
import os
import filecmp

'''
Description: Grabs config file from router
Input: list of ip address
Output: new files with router configs
'''
def getConfig(ip):
    connection = tftpy.TftpClient(ip, 69)
    connection.download('/startup-config','/tmp/' + ip + '_tmp')

'''
Description: Creates router directory if it doesn't exist
Input: dictionary
Output: Saves config file or there are no changes
'''
def saveConfig(ip):
    path = '/tmp/{0}/'.format(ip)
    if os.path.exists(path):
        compareConfigs(path, ip)
    else:
        os.mkdir('/tmp/' + ip)
        os.rename('/tmp/' + ip + '_tmp', '/tmp/{0}/{0}_v1'.format(ip))

'''
Description: Checks the differenc ein a file
Input: ip address, path to old configs, dictionary
Output: saves new config or finds no changes
'''
def compareConfigs(path, ip):
    l = []
    for filename in os.listdir(path):
        l.append(filename[-1])
    if filecmp.cmp('/tmp/' + ip + '_tmp', path + ip + \
    '_v' + max(l)):
        os.remove('/tmp/' + ip + '_tmp')
    else:
        v = str(int(max(l))+1)
        os.rename('/tmp/' + ip + '_tmp', '/tmp/{0}/{0}_v{1}'.format(ip, v))




