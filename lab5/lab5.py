'''
Lab 5

Names: Robert Werthman (rowe7280), Derrick D'Souza (deds7325)

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
    percent_ycord = [(i/sum(ycord))*100 for i in ycord]
    if not isinstance(xcord[0], tuple):
        labels = ['{0} - {1:0.2f}% ({2:0.2f} KiloBytes)'.format(x, percent, y) for x, percent, y in zip(xcord, percent_ycord, ycord)]
    else:
        if not isinstance(xcord[0][1], long):
            labels = ['Src Address: {0} Dst Address: {1} - {2:0.2f}% ({3:0.2f} KiloBytes)'.format(x[1], x[0], percent, y) for x, percent, y in zip(xcord, percent_ycord, ycord)]
        else:
            labels = ['Local Host: {0} Port: {1} - {2:0.2f}% ({3:0.2f} KiloBytes)'.format(x[0], x[1], percent, y) for x, percent, y in zip(xcord, percent_ycord, ycord)]
    values = ycord
    patches, texts = pie(values, colors=colors, shadow=True)
    legend(patches, labels, loc='upper left')
    title(graphTitle)
    savefig(fileName)

def TopRemotePorts(log, file):
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
            octetsL.append(float(octets)/1024)
            protocolL.append(protocolCounter[port])
    # Find the service related to the highest used ports
    for port, protocol in zip(portsL, protocolL):
        if protocol == 6:
            serviceL.append(PortLookup(port, 'tcp'))
        elif protocol == 17:
            serviceL.append(PortLookup(port, 'udp'))
    # Create a graph of port/service vs traffic
    graphTitle = 'Top 10 Remote Ports By Amount Of Traffic'
    fileName = 'top_ports_{0}.png'.format(file)
    Graph(serviceL, octetsL, graphTitle, fileName)

def TopRemoteHosts(log, file):
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
            octetsL.append(float(octets)/1024)
    # Lookup hostname of ip address
    for ip in remoteIPL:
        remoteHostName.append(DNSLookup(ip))
    # Create a graph of IP address vs traffic
    graphTitle = 'Top 10 Remote Sites Accessed By Traffic Generated'
    fileName = 'top_remote_{0}.png'.format(file)
    Graph(remoteHostName, octetsL, graphTitle, fileName)

def TopLocalToRemote(log, file):
    counter = {}
    ipports = {}
    octetsL = []
    remoteIPL = []
    localIPL = []
    remoteHostName = []
    for flow in log:
        if '192.168.1.' in flow.src_addr and '192.168.1.' not in flow.dst_addr:
            try:
                counter[(flow.dst_addr, flow.src_addr)] += flow.octets
            except KeyError:
                counter[(flow.dst_addr, flow.src_addr)] = flow.octets
    sortedValues = sorted(counter.values(), reverse=True)
    sortedValues = sortedValues[:10]
    for tuple, octets in counter.iteritems():
        if octets in sortedValues:
            remoteIPL.append(tuple[0])
            localIPL.append(tuple[1])
            octetsL.append(float(octets)/1024)
    for remoteip, localip in zip(remoteIPL, localIPL):
        remoteHostName.append((DNSLookup(remoteip), localip))
    graphTitle = 'Top 10 Remote Sites Accessed By Local IPs'
    fileName = 'remote_local_{0}.png'.format(file)
    Graph(remoteHostName, octetsL, graphTitle, fileName)

def TopLocalHostLocalPort(log, file):
    counter = {}
    ipports = []
    octetsL = []
    for flow in log:
        if '192.168.1.' in flow.src_addr and '192.168.1.' not in flow.dst_addr:
            try:
                counter[(flow.src_addr, flow.src_port)] += flow.octets
            except KeyError:
                counter[(flow.src_addr, flow.src_port)] = flow.octets
    sortedValues = sorted(counter.values(), reverse=True)
    sortedValues = sortedValues[:10]
    for tuple, octets in counter.iteritems():
        if octets in sortedValues:
            ipports.append((tuple[0], tuple[1]))
            octetsL.append(float(octets)/1024)
    graphTitle = 'Top Local Hosts And Ports'
    fileName = 'local_port_{0}.png'.format(file)
    Graph(ipports, octetsL, graphTitle, fileName)

def UserInput():
    print('Choose the Netflow file to anaylyze:')
    print('1. flowd_capture_1')
    print ('2. flowd_capture_2')
    flowFile = raw_input('Enter your choice [1-2]: ')
    if flowFile == '1':
        try:
            log = flowd.FlowLog('flowd_capture_1')
            TopRemotePorts(log, 'flowd_capture_1')
            log = flowd.FlowLog('flowd_capture_1')
            TopRemoteHosts(log, 'flowd_capture_1')
            log = flowd.FlowLog('flowd_capture_1')
            TopLocalToRemote(log, 'flowd_capture_1')
            log = flowd.FlowLog('flowd_capture_1')
            TopLocalHostLocalPort(log, 'flowd_capture_1')
        except IOError:
            print 'flowd_capture_1 not found.'
            return UserInput()
    elif flowFile == '2':
        try:
            log = flowd.FlowLog('flowd_capture_2')
            TopRemotePorts(log, 'flowd_capture_2')
            log = flowd.FlowLog('flowd_capture_2')
            TopRemoteHosts(log, 'flowd_capture_2')
            log = flowd.FlowLog('flowd_capture_2')
            TopLocalToRemote(log, 'flowd_capture_2')
            log = flowd.FlowLog('flowd_capture_2')
            TopLocalHostLocalPort(log, 'flowd_capture_2')
        except IOError:
            print 'flowd_capture_2 not found.'
            return UserInput()


def main():
    UserInput()


if __name__ == '__main__':
    main()
