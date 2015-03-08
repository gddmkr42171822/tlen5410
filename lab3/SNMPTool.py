import netsnmp

class Router(object):

    def __init__(self, desthost, community):
        self.session = netsnmp.Session(DestHost=desthost, Community=community,
                                Version = 1)
        self.sysname = netsnmp.Varbind('.1.3.6.1.2.1.1.5.0')
        self.syscontact = netsnmp.Varbind('.1.3.6.1.2.1.1.4.0')
        self.syslocation = netsnmp.Varbind('.1.3.6.1.2.1.1.6.0')

    def retrieveHostname(self):
        varlist = netsnmp.VarList(self.sysname)
        self.session.get(varlist)
        return self.sysname.val

    def setHostname(self, hostname):
        self.retrieveHostname()
        self.sysname.val = hostname
        varlist = netsnmp.VarList(self.sysname)
        self.session.set(varlist)

    def retrieveContact(self):
        varlist = netsnmp.VarList(self.syscontact)
        self.session.get(varlist)
        return self.syscontact.val

    def setContact(self, contact):
        self.retrieveContact()
        self.syscontact.val = contact
        varlist = netsnmp.VarList(self.syscontact)
        self.session.set(varlist)


    def retrieveUptime(self):
        sysuptime = netsnmp.Varbind('.1.3.6.1.2.1.1.3.0')
        varlist = netsnmp.VarList(sysuptime)
        self.session.get(varlist)
        return sysuptime.val


    def retrieveLocation(self):
        varlist = netsnmp.VarList(self.syslocation)
        self.session.get(varlist)
        return self.syslocation.val

    def setLocation(self, location):
        self.retrieveLocation()
        self.syslocation.val = location
        varlist = netsnmp.VarList(self.syslocation)
        self.session.set(varlist)

    def retrieveCDPneighbors(self):
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
