'''

Lab 1: Obtain and Parse Configuration via tftp

'''

import tftpy
import os
import filecmp

'''
Gets a router configuration from a router and saves it in the tmp folder.
'''
def getConfig(ip):
    connection = tftpy.TftpClient(ip, 69)
    connection.download('/startup-config','/tmp/' + ip + '_tmp')

'''
Saves the downloaded config if there aren't any for the router otherwise
it compares it to the other router configs to see if there are changes.
'''
def saveConfig(ip):
    path = '/tmp/{0}/'.format(ip)
    if os.path.exists(path):
        compareConfigs(path, ip)
    else:
        os.mkdir('/tmp/' + ip)
        os.rename('/tmp/' + ip + '_tmp', '/tmp/{0}/{0}_v1'.format(ip))

'''
Checks for changes between router configs.  If there is it creates a new
router config version and saves the newest one as it.
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




