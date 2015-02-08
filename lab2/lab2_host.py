'''
This file defines the class Host and its methods
'''
from lab2_packet import Packet

class Host(object):
    def __init__(self, hostname, address):
        self.hostname = hostname
        self.address = address

    def __str__(self):
        '''
        Print the hostname and address of the host
        '''
        return 'hostname: {0} address: {1}'.format( \
        self.hostname, self.address)

    def printConnected_switch(self):
        '''
        Print the hostname of the switch the host is connected to
        '''
        print '\nhost |{0}| connected to switch |{1}|'.format(\
        self.hostname, self.connected_switch.hostname)

    def connect(self, switch):
        '''
        Connect the host to a switch
        '''
        print 'Connecting {0} to {1}'.format(self.hostname, \
        switch.hostname)
        self.connected_switch = switch

    def send(self, dst, payload = 'Hello World!'):
        '''
        Send a packet to a destination through the connected_switch
        '''
        print 'Sending data from {0} ({1}) to {2} ({3})'.format(\
        self.hostname, self.address, dst.hostname, dst.address)
        pkt = Packet(self.address, dst.address, payload)
        self.connected_switch.receive(pkt, self)

    def receive(self, pkt, device):
        '''
        Print the packet payload if it has the same destination address
        as the current host
        '''
        if pkt.dst == self.address:
            print 'Host {0} ({1}) : Received "{2}" from {3}'.format(\
            self.hostname, self.address, pkt.payload, pkt.src)
