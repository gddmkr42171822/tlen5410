'''
SNMPTool.py
This file defines methods that use netsnmp to interact 
with a router.
'''
import netsnmp

class Router(object):

    def __init__(self, desthost, community):
        '''
        Creates and snmp session and creates the varbinds for
        hostname, contact, and location
        '''
        self.session = netsnmp.Session(DestHost=desthost, Community=community,
                                Version = 1)
        self.sysname = netsnmp.Varbind('.1.3.6.1.2.1.1.5.0')
        self.syscontact = netsnmp.Varbind('.1.3.6.1.2.1.1.4.0')
        self.syslocation = netsnmp.Varbind('.1.3.6.1.2.1.1.6.0')

    def retrieveHostname(self):
        '''
        Returns the hostname of a router.
        '''
        varlist = netsnmp.VarList(self.sysname)
        self.session.get(varlist)
        return self.sysname.val

    def setHostname(self, hostname):
        '''
        Changes the hostname of a router.
        '''
        self.retrieveHostname()
        self.sysname.val = hostname
        varlist = netsnmp.VarList(self.sysname)
        self.session.set(varlist)

    def retrieveContact(self):
        '''
        Returns the contact of a router.
        '''
        varlist = netsnmp.VarList(self.syscontact)
        self.session.get(varlist)
        return self.syscontact.val

    def setContact(self, contact):
        '''
        Changes the contact of a router.
        '''
        self.retrieveContact()
        self.syscontact.val = contact
        varlist = netsnmp.VarList(self.syscontact)
        self.session.set(varlist)


    def retrieveUptime(self):
        '''
        Returns the uptime of a router.
        '''
        sysuptime = netsnmp.Varbind('.1.3.6.1.2.1.1.3.0')
        varlist = netsnmp.VarList(sysuptime)
        self.session.get(varlist)
        return sysuptime.val


    def retrieveLocation(self):
        '''
        Returns the location of a router.
        '''
        varlist = netsnmp.VarList(self.syslocation)
        self.session.get(varlist)
        return self.syslocation.val

    def setLocation(self, location):
        '''
        Changes the location of a router.
        '''
        self.retrieveLocation()
        self.syslocation.val = location
        varlist = netsnmp.VarList(self.syslocation)
        self.session.set(varlist)

    def retrieveCDPneighbors(self):
        '''
        Returns two lists about a router's cdp neighbors.
        '''
        cdpdeviceport = netsnmp.Varbind('.1.3.6.1.4.1.9.9.23.1.2.1.1.7')
        cdpdeviceid = netsnmp.Varbind('.1.3.6.1.4.1.9.9.23.1.2.1.1.6')
        idvarlist = netsnmp.VarList(cdpdeviceid)
        portvarlist = netsnmp.VarList(cdpdeviceport)
        self.session.walk(idvarlist)
        self.session.walk(portvarlist)
        portlist = []
        idlist = []
        for x in idvarlist:
            idlist.append(x.val)
        for x in portvarlist:
            portlist.append(x.val)
        return idlist, portlist



    def retrieveRouteTable(self):
        '''
        Returns four lists about a router's routing table.
        '''
        ifnumber = netsnmp.Varbind('.1.3.6.1.2.1.4.24.3.0')
        vl = netsnmp.VarList(ifnumber)
        self.session.get(vl)
        iproutedest = netsnmp.Varbind('.1.3.6.1.2.1.4.24.4.1.1')
        iproutemask = netsnmp.Varbind('.1.3.6.1.2.1.4.24.4.1.2')
        iproutenexthop = netsnmp.Varbind('.1.3.6.1.2.1.4.24.4.1.4')
        iproutemetric = netsnmp.Varbind('.1.3.6.1.2.1.4.24.4.1.11')
        varlist = netsnmp.VarList()
        varlist.append(iproutedest)
        varlist.append(iproutemask)
        varlist.append(iproutenexthop)
        varlist.append(iproutemetric)
        destlist = []
        masklist = []
        hoplist = []
        metriclist = []
        for i in range(0, int(ifnumber.val)):
            self.session.getnext(varlist)
            destlist.append(iproutedest.val)
            masklist.append(iproutemask.val)
            hoplist.append(iproutenexthop.val)
            metriclist.append(iproutemetric.val)
        return destlist, masklist, hoplist, metriclist



def main():
    r = Router('172.20.74.101', 'public')
    print r.retrieveHostname()
    print r.retrieveContact()
    print r.retrieveLocation()
    print r.retrieveRouteTable()
    print r.retrieveCDPneighbors()


if __name__ == '__main__':
    main()
