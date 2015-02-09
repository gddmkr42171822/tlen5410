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

def sendPackets(hosts):
    for i, host in enumerate(hosts):
        for j in range(len(hosts)):
            if hosts[i].address != hosts[j].address:
                hosts[i].send(hosts[j])

def printSwitches(switches):
    for switch in switches:
        switch.printPorts()
        switch.printForwardtable()

def main():

    switches = []
    hosts = []

    generateSwitches(switches, 3)
    generateHosts(hosts, len(switches)*2)

    connectSwitches(switches)
    connectHosts(hosts, switches)

    sendPackets(hosts)
    printSwitches(switches)



if __name__ == "__main__":
    main()
