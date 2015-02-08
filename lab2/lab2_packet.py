'''
This file defines the Packet class and its methods
'''
class Packet(object):
    def __init__(self, src, dst, payload):
        self.src = src
        self.dst = dst
        self.payload = payload

    def __str__(self):
        return '\nsrc: {0} dst: {1} payload: {2}'.format(self.src, self.dst,\
        self.payload)
