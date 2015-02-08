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
        print 'Connecting {0} to {1}'.format(self.hostname, \
        device.hostname)
        self.ports.append(device)

    def receive(self, pkt, sender):
        '''
        1. Receive a packet.
        2. Add packet source address and received-on port to
        forwardtable of switch if it's not there.
        3. If packet destination address is in the forwardtable then
        call forward method.
        4. If packet destination address is not in the forwardtable
        call broadcast method
        '''
        if pkt.src not in self.forwardtable:
            self.forwardtable[pkt.src] = self.ports.index(sender)
        if pkt.dst in self.forwardtable:
            self.forward(pkt)
        else:
            self.broadcast(pkt, sender)


    def forward(self, pkt):
        '''
        1. Get the hostname from the port in the forwardtable
         and send the packet to the next device
        '''
        print 'Forward'
        (self.ports[self.forwardtable[pkt.dst]]).receive(pkt, self)

    def broadcast(self, pkt, sender):
        '''
        Broadcast packet out all of the switchports except the one
        it received the packet from
        '''
        print 'Broadcast'
        for device in self.ports:
            if device.address != sender.address:
                device.receive(pkt, self)
        pass

