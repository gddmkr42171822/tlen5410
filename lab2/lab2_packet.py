'''
This file defines the Packet class and its methods
'''
class Packet(object):
    def __init__(self, src, dst, payload):
        '''
        Attributes:
            src -> source address
            dst -> destination address
            payload -> packet data
        '''
        self.src = src
        self.dst = dst
        self.payload = payload

    def __str__(self):
        '''
        Prints the source address, destination address, and payload
        of a packet
        '''
        return '\nsrc: {0} dst: {1} payload: {2}'.format(self.src, self.dst,\
        self.payload)
