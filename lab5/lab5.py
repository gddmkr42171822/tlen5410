'''

Sources:
1. http://stackoverflow.com/questions/6170246/how-do-i-use-matplotlib-autopct
- my_autopct function
2. http://stackoverflow.com/questions/23577505/how-to-avoid-overlapping-of-labels-autopct-in-piechart-generated-using-matplot
- pie legend
3. http://stackoverflow.com/questions/1614236/in-python-how-to-i-convert-all-items-in-a-list-to-floats
- cast list to float
'''

import flowd
import socket
from pylab import *

def DNSLookup(ip):
    try:
        name = socket.gethostbyaddr(ip)
        return name[0]
    except socket.herror, ex:
        return ip

def PortLookup(portNumber, flowProtocol):
    try:
        service = socket.getservbyport(portNumber, flowProtocol)
        return service
    except:
        return portNumber


def Graph(xcord, ycord, graphTitle, fileName):
    figure(figsize=(13,13))
    colors = ['orangered', 'green', 'skyblue', 'pink',\
    'steelblue', 'yellow', 'orange', 'silver', 'blueviolet', 'grey']
    ycord = [int(i) for i in ycord]
    percent_ycord = [(float(i)/sum(ycord))*100 for i in ycord]
    labels = ['{0} - {1:0.2f}% ({2} Bytes)'.format(x, percent, y) for x, percent, y in zip(xcord, percent_ycord, ycord)]
    values = ycord
    patches, texts = pie(values, colors=colors, shadow=True)
    legend(patches, labels, loc='upper left')
    title(graphTitle)
    savefig(fileName)

def TopPorts(log):
    counter = {}
    protocolCounter = {}
    portsL = []
    octetsL = []
    protocolL = []
    serviceL = []
    # Capture the ports with the highest traffic
    for flow in log:
        if '192.168.1.' not in flow.dst_addr:
            try:
                counter[flow.dst_port] += flow.octets
            except KeyError:
                counter[flow.dst_port] = flow.octets
                protocolCounter[flow.dst_port] = flow.protocol
    sortedValues = sorted(counter.values(), reverse=True)
    sortedValues = sortedValues[:10]
    for port, octets in counter.iteritems():
        if octets in sortedValues:
            portsL.append(port)
            octetsL.append(octets)
            protocolL.append(protocolCounter[port])
    # Find the service related to the highest used ports
    for port, protocol in zip(portsL, protocolL):
        if protocol == 6:
            serviceL.append(PortLookup(port, 'tcp'))
        elif protocol == 17:
            serviceL.append(PortLookup(port, 'udp'))
    # Create a graph of port/service vs traffic
    graphTitle = 'Top 10 Remote Ports By Amount Of Traffic'
    fileName = 'top_ports.png'
    Graph(serviceL, octetsL, graphTitle, fileName)

def TopRemoteHosts(log):
    counter = {}
    octetsL = []
    remoteIPL = []
    remoteHostName = []
    # Capture the remote IP addresses with the most traffic
    for flow in log:
        if '192.168.1.' not in flow.dst_addr:
            try:
                counter[flow.dst_addr] += flow.octets
            except KeyError:
                counter[flow.dst_addr] = flow.octets
    sortedValues = sorted(counter.values(), reverse=True)
    sortedValues = sortedValues[:10]
    for ip, octets in counter.iteritems():
        if octets in sortedValues:
            remoteIPL.append(ip)
            octetsL.append(octets)
    # Lookup hostname of ip address
    for ip in remoteIPL:
        remoteHostName.append(DNSLookup(ip))
    # Create a graph of IP address vs traffic
    graphTitle = 'Top 10 Remote Sites Accessed By Traffic Generated'
    fileName = 'top_remote.png'
    Graph(remoteHostName, octetsL, graphTitle, fileName)

def TotalBandwidth(log):
    pass




def UserInput():
    print('Choose the Netflow file to anaylyze:')
    print('1. flowd_capture_1')
    print ('2. flowd_capture_2')
    flowFile = raw_input('Enter your choice [1-2]: ')
    if flowFile == '1':
        try:
            log = flowd.FlowLog('flowd_capture_1')
            TopPorts(log)
            log = flowd.FlowLog('flowd_capture_1')
            TopRemoteHosts(log)
        except IOError:
            print 'flowd_capture_1 not found.'
            return UserInput()
    elif flowFile == '2':
        try:
            log = flowd.FlowLog('flowd_capture_2')
        except IOError:
            print 'flowd_capture_2 not found.'
            return UserInput()


def main():
    UserInput()


if __name__ == '__main__':
    main()
