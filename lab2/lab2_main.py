'''
Lab 2

Task: Simulate a layer 2 network with switches and hosts


Sources:
https://docs.python.org/2/tutorial/datastructures.html
-How to iterate and print keys and values in a dictionary

https://stackoverflow.com/questions/2847386/python-string-and-integer-concatenation
-How to concatenate an int to a string

'''


from lab2_host import Host
from lab2_packet import Packet
from lab2_switch import Switch
import random

def generate_mac():
    '''
    Job: Generates a random mac address
    '''
    mac = ""
    for i in range(0, 6):
        mac += "%02x:" % random.randint(0x00, 0xff)
    return mac.strip(":")

def generateSwitches(switches, num):
    '''
    Job: Creates switch objects and adds them to a list
    Input: an empty list of switches, number of switches to be made
    '''
    for x in range(0, num):
        switches.append(Switch("s" + str(x), generate_mac()))

def generateHosts(hosts, num):
    '''
    Job: Creates host objects and adds them to a list
    Inpute: an empty list of hosts, number of hosts to be
    '''
    for x in range(0, num):
        hosts.append(Host("h" + str(x), generate_mac()))

def connectSwitches(switches):
    '''
    Job: Connects switch objects linearly with each other
    Input: a list of switches
    '''
    for i in range(len(switches) - 1):
        switches[i].connect(switches[i+1])
        switches[i+1].connect(switches[i])

def connectHosts(hosts, switches):
    '''
    Job: Connects 2 hosts with one switch
    Input: a list of hosts, a list of switches
    '''
    i = 0
    for switch in switches:
        switch.connect(hosts[i])
        switch.connect(hosts[i+1])
        hosts[i].connect(switch)
        hosts[i+1].connect(switch)
        i += 2

def sendPackets(hosts):
    '''
    Job: send packets between all hosts in a list of hosts
    Input: a list of hosts
    '''
    for i, host in enumerate(hosts):
        for j in range(len(hosts)):
            if hosts[i].address != hosts[j].address:
                hosts[i].send(hosts[j])

def printSwitches(switches):
    '''
    Job: print the ports list and forwardtable of each switch
    Input: a list of switches
    '''
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
