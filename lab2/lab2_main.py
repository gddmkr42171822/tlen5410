'''
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

def connectSwitches(switches):
    for i in range(len(switches) - 1):
        switches[i].connect(switches[i+1])
        switches[i+1].connect(switches[i])

def connectHosts(hosts, switches):
    i = 0
    for switch in switches:
        switch.connect(hosts[i])
        switch.connect(hosts[i+1])
        hosts[i].connect(switch)
        hosts[i+1].connect(switch)
        i += 2


def main():

    switches = []
    hosts = []

    generateSwitches(switches, 4)
    generateHosts(hosts, len(switches)*2)

    connectSwitches(switches)
    connectHosts(hosts, switches)

    '''
    s0 = Switch("s0", generate_mac())
    s1 = Switch("s1", generate_mac())
    s2 = Switch("s2", generate_mac())

    h0 = Host("h0", generate_mac())
    h1 = Host("h1", generate_mac())
    h2 = Host("h2", generate_mac())
    h3 = Host("h3", generate_mac())
    h4 = Host("h4", generate_mac())
    h5 = Host("h5", generate_mac())

    s0.connect(h0)
    h0.connect(s0)
    s0.connect(h1)
    h1.connect(s0)

    s1.connect(h2)
    h2.connect(s1)
    s1.connect(h3)
    h3.connect(s1)
    s1.connect(s0)
    s0.connect(s1)

    s2.connect(s1)
    s1.connect(s2)
    h4.connect(s2)
    s2.connect(h4)
    h5.connect(s2)
    s2.connect(h5)

    # Send data between devices
    h0.send(h1)
    h1.send(h0)
    h0.send(h5)
    h5.send(h0)
    h4.send(h5)
    h4.send(h2)
    '''
    # Print out the values of ports & forward table from the switch
    '''
    s0.printPorts()
    s0.printForwardtable()
    s1.printPorts()
    s1.printForwardtable()
    s2.printPorts()
    s2.printForwardtable()
    '''


if __name__ == "__main__":
    main()
