import flowd
from pylab import *

def TopPorts(log):
    counter = {}
    portsL = []
    octetsL = []
    for flow in log:
        if '192.168.1.' not in flow.dst_addr:
            try:
                counter[flow.dst_port] += flow.octets
            except KeyError:
                counter[flow.dst_port] = flow.octets
    sortedValues = sorted(counter.values(), reverse=True)
    sortedValues = sortedValues[:10]
    for port, octets in counter.iteritems():
        if octets in sortedValues:
            portsL.append(port)
            octetsL.append(octets)
    figure(figsize=(7,7))
    colors = ['red', 'green', 'blue', 'pink',\
    'cyan', 'yellow', 'orange', 'silver', 'brown', 'grey']
    labels = portsL
    values = octetsL
    pie(values, labels=labels, colors=colors, shadow=True, autopct='%1.1f%%')
    title('10 Ports With Most Traffic')
    savefig('top_ports.png')

def TopRemoteHosts(log):
    pass

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
