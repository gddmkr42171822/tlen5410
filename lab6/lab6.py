'''

Sources:
1. https://stackoverflow.com/questions/19419754/how-to-remove-a-node-inside-an-iterator-in-python-xml-etree-elementree
- How remove a child node with an iterator to the parent
'''

import paramiko
import xml.etree.ElementTree as etree
import xml.parsers.expat

hello = '''<?xml version="1.0" encoding="UTF-8"?>
<hello>
    <capabilities>
        <capability>
            urn:ietf:params:xml:ns:netconf:base:1.0
    </capability>
</capabilities>
</hello>
]]>]]>'''

get_config_request = '''
<?xml version="1.0" encoding="UTF-8"?>
<rpc message-id="105" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
<get-config>
    <source>
        <running/>
    </source>
</get-config>
</rpc>
]]>]]>
'''

hostname = '172.20.74.239'
username = 'netman'
password = 'netman'

# Get more information
#paramiko.common.logging.basicConfig(level=paramiko.common.DEBUG)

# Establish the connection
def establish_connection(hostname, username, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, 22, username, password, allow_agent=False, look_for_keys=False)
    return client

client = establish_connection(hostname, username, password)
transport = client.get_transport()
channel = transport.open_channel('session')
channel.invoke_subsystem('netconf')

data = ""
while True:
    if data.find(']]>]]>') != -1:
        data = data.replace(']]>]]>', '')
        break

    data = channel.recv(1024)
#print data.strip()

channel.send(hello)
channel.send(get_config_request)

data = ""
while True:
    if data.find(']]>]]>') != -1:
        data = data.replace(']]>]]>', '')
        break

    data += channel.recv(1024)

#print data.strip()

try:
    tree = etree.fromstring(data)
    print tree.findall('.//user')
    for login in tree.iter('login'):
        for user in login.iter('user'):
            if user.find('name').text == 'admin':
                login.remove(user)
    print tree.findall('.//user')
    '''
    for user in tree.findall('.//user'):
        if user.find('name').text == 'admin':
            tree.findall('.//user').remove(user)
            print tree.findall('.//user')
    '''
    #tree = etree.tostring(tree)
    #print tree

except xml.parsers.expat.ExpatError, ex:
    print ex

# Create the shell channel, execute command & wait for response
#(stdin, stdout, stderr) = client.exec_command('show ip int br')
#for line in stdout.readlines():
#    print line
client.close()
