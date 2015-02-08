'''
This file defines the class Switch and its methods
'''

class Switch(object):
    def __init__(self, hostname, address):
        self.hostname = hostname
        self.address = address
        self.ports = []
        self.forwardtable = {}

    def __str__(self):
        '''
        Prints the hostname and address of the switch
        '''
        return 'hostname: {0} address: {1}'.format(self.hostname, \
        self.address)

    def printPorts(self):
        '''
        Prints the ports and associated hosts of the switch
        '''
        print '\n' + self.hostname + ' port list:'
        for port, host in enumerate(self.ports):
            print 'port: {0} hostname: {1}'.format(port, host.hostname)

    def printForwardtable(self):
        '''
        Prints the mac address table (address and associated port)
        of the switch
        '''
        print '\n' + self.hostname + ' forwardtable:'
        for address, port in self.forwardtable.iteritems():
            print 'address: {0} port: {1}'.format(address, port)

    def connect(self, device):
        '''
        Connects a switch to a device
        '''
        self.ports.append(device)

    def receive(self, pkt, sender):
        '''
        1. Receive a packet.
        2. Add packet source address and received-on port to
        forwardtable of switch if it's not there.
        '''
        if pkt.src not in self.forwardtable:
            self.forwardtable[pkt.src] = self.ports.index(sender)

    def forward(self, pkt, sender):
        '''
        1. Add packet source address to forwardtable of switch if it's
        not there.
        2. If packet destination address is in the forwardtable then
        send it to next host.
        3. If packet destination address is not in the forwardtable
        call broadcast method
        '''
        pass

    def broadcast(self, pkt):
        '''
        Broadcast packet out all of the switchports except the one
        it received the packet from
        '''
        pass

