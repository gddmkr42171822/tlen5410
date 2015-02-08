'''
Name: Robert Werthman
Lab 2




Sources:
https://docs.python.org/2/tutorial/datastructures.html
-How to iterate and print keys and values in a dictionary
'''


from lab2_host import Host
from lab2_packet import Packet
from lab2_switch import Switch
import random

def generate_mac():
    mac = ""
    for i in range(0, 6):
        mac += "%02x:" % random.randint(0x00, 0xff)
    return mac.strip(":")

def main():
    s0 = Switch("s0", generate_mac())
    h0 = Host("h0", generate_mac())
    h1 = Host("h1", generate_mac())

    print s0
    print h0
    print h1

    # Connect Host 0 to Switch 0
    s0.connect(h0)
    h0.connect(s0)

    # Connect Host 1 to Switch 1
    s0.connect(h1)
    h1.connect(s0)

    # Print what switches the hosts are connected to
    h1.printConnected_switch()
    h0.printConnected_switch()

    # Send data from Host 0 to Host 1
    #h0.send(h1.address)

    # Print out the values of ports & forward table from the switch
    s0.printPorts()
    s0.printForwardtable()

if __name__ == "__main__":
    main()
