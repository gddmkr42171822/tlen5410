'''
Name: Robert Werthman
Lab 2




Sources:
https://docs.python.org/2/tutorial/datastructures.html
-How to iterate and print keys and values in a dictionary

https://stackoverflow.com/questions/2847386/python-string-and-integer-concatenation
-How to concatenate and int and a string
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

def generateSwitches(switches, num):
    for x in range(0, num):
        switches.append(Switch("s" + str(x), generate_mac()))

def generateHosts(hosts, num):
    for x in range(0, num):
        hosts.append(Host("h" + str(x), generate_mac()))

def main():
    switches = []
    hosts = []
    generateSwitches(switches, 5)
    generateHosts(hosts, 5)
    for x in switches:
        print x.hostname, x.address
    for x in hosts:
        print x.hostname, x.address

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
    #h1.printConnected_switch()
    #h0.printConnected_switch()

    # Send data between devices
    h0.send(h1)
    h1.send(h0)
    h0.send(h1)
    h1.send(h0)

    # Print out the values of ports & forward table from the switch
    s0.printPorts()
    s0.printForwardtable()



if __name__ == "__main__":
    main()
