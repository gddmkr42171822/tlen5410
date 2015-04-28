'''
Name:

Lab 6

Sources:
1. https://stackoverflow.com/questions/19419754/how-to-remove-a-node-inside-an-iterator-in-python-xml-etree-elementree
- How remove a child node with an iterator to the parent
2. http://lxml.de/1.3/tutorial.html
- How to insert an element in the tree
3. https://groups.google.com/forum/#!topic/comp.lang.python/Rq40dmwLfMQ
- How to remove the first and last line of a string
'''

import paramiko
import xml.etree.ElementTree as etree
import xml.parsers.expat


username = 'netman'
password = 'netman'
hosts = ['172.20.74.238', '172.20.74.239', '172.20.74.240',
            '172.20.74.241', '172.20.74.242']

hello = '''
<?xml version="1.0" encoding="UTF-8"?>
<hello>
    <capabilities>
        <capability>
            urn:ietf:params:xml:ns:netconf:base:1.0
    </capability>
</capabilities>
</hello>
]]>]]>
'''

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

oureditconfig_template = '''
<rpc>
    <edit-config>
        <target>
            <running/>
        </target>
        <config>
'''

class Router(object):
    def __init__(self):
        self.compliant = True
        self.violations = []

    def establish_connection(self, hostname, username, password):
        '''
        Establish a connection to a router.
        '''
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, 22, username, password, allow_agent=False, look_for_keys=False)
        self.client = client

    def establish_channel(self):
        '''
        Establish a netconf channel to a router.
        '''
        transport = self.client.get_transport()
        self.channel = transport.open_channel('session')
        self.channel.invoke_subsystem('netconf')

    def receive_data(self):
        '''
        Read data from a channel.
        '''
        data = ""
        while True:
            if data.find(']]>]]>') != -1:
                data = data.replace(']]>]]>', '')
                break
            data += self.channel.recv(1024)
        self.data = data

    def remove_reply(self):
        '''
        Remove rpc-reply and configuration from the request.
        '''
        self.data = self.data.replace('<rpc-reply>', '')
        self.data = self.data.replace('</rpc-reply>', '')
        self.data = self.data.strip('\n')

    def remove_http(self):
        '''
        Remove http if is enabled.
        '''
        try:
            tree = etree.fromstring(self.data)
            for web_management in tree.iter('web-management'):
                for http in web_management.iter('http'):
                    self.violations.append('Disabled the HTTP Service')
                    self.compliant = False
                    web_management.remove(http)
        except xml.parsers.expat.ExpatError, ex:
            print ex
        self.data = etree.tostring(tree)

    def remove_user(self):
        '''
        Remove a user from the xml element tree.
        '''
        try:
            tree = etree.fromstring(self.data)
            for login in tree.iter('login'):
                for user in login.iter('user'):
                    if user.find('name').text == 'bkool':
                        self.compliant = False
                        self.violations.append('Removed User Bob Kool')
                        login.remove(user)
        except xml.parsers.expat.ExpatError, ex:
            print ex
        self.data = etree.tostring(tree)

    def change_mtu(self):
        '''
        Set the MTU to 1500.
        '''
        try:
            tree = etree.fromstring(self.data)
            for interfaces in tree.iter('interfaces'):
                for interface in interfaces.iter('interface'):
                    if 'ge' in interface.find('name').text:
                        for unit in interface.iter('unit'):
                            if unit.find('mtu') is not None:
                                if unit.find('mtu').text != '1500':
                                    self.violations.append('Set the MTU for ' + interface.find('name').text + ' to 1500')
                                    self.compliant = False
                                    unit.find('mtu').text = '1500'
                            else:
                                unit.insert(1, etree.Element('mtu'))
                                self.violations.append('Set the MTU for ' + interface.find('name').text + ' to 1500')
                                self.compliant = False
                                unit.find('mtu').text = '1500'
        except xml.parsers.expat.ExpatError, ex:
            print ex
        self.data = etree.tostring(tree)

    def change_snmp(self):
        '''
        Change the SNMP community string to read-only.
        '''
        try:
            tree = etree.fromstring(self.data)
            for community in tree.iter('community'):
                if community.find('authorization').text != 'read-only':
                    community.find('authorization').text = 'read-only'
                    self.violations.append('Set the SNMP community string ' + community.find('name').text + ' to be read-only')
                    self.compliant = False
        except xml.parsers.expat.ExpatError, ex:
            print ex
        self.data = etree.tostring(tree)

    def fix_xml(self):
        '''
        Change the received router configuration.
        '''
        self.remove_http()
        self.remove_user()
        self.change_mtu()
        self.change_snmp()
        self.remove_reply()

    def edit_config(self):
        '''
        Send the edited configuration back to the router.
        '''
        self.data = oureditconfig_template + self.data + '\n</config>\n</edit-config>\n</rpc>\n]]>]]>\n'
        self.channel.send(self.data)
        self.receive_data()

def main():
    for host in hosts:
        router = Router()
        router.establish_connection(host, username, password)
        router.establish_channel()
        router.channel.send(hello)
        router.receive_data()
        router.channel.send(get_config_request)
        router.receive_data()
        router.fix_xml()
        router.edit_config()
        if router.compliant:
            print '\nScanning the configuration for ' + host + '... OKAY'
        else:
            print '\nScanning the configuration for ' + host + '... NON-COMPLIANT'
            for violation in router.violations:
                print violation
        router.client.close()

if __name__ == '__main__':
    main()
