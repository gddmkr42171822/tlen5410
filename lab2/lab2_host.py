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
        return '\nhostname: {0} address: {1}'.format( \
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
        self.connected_switch = switch

    def send(self, dst, payload = 'Hello World!'):
        '''
        Send a packet to a destination through the connected_switch
        '''
        pkt = Packet(self.address, dst, payload)
        self.connected_switch.receive(pkt, self)

    def receive(self, pkt):
        print pkt.payload
