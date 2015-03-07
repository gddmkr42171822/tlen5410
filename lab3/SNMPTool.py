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

    def retrieveRouteTable(self):
        ifnumber = netsnmp.Varbind('.1.3.6.1.2.1.2.1.0')
        vl = netsnmp.VarList(ifnumber)
        self.session.get(vl)
        iproutedest = netsnmp.Varbind('.1.3.6.1.2.1.4.24.4.1.1')
        iproutemask = netsnmp.Varbind('.1.3.6.1.2.1.4.24.4.1.2')
        iproutenexthop = netsnmp.Varbind('.1.3.6.1.2.1.4.24.4.1.4')
        varlist = netsnmp.VarList()
        varlist.append(iproutedest)
        varlist.append(iproutemask)
        varlist.append(iproutenexthop)
        destlist = []
        masklist = []
        hoplist = []
        finallist = []
        for i in range(0, int(ifnumber.val)-1):
            self.session.getnext(varlist)
            destlist.append(iproutedest.val)
            masklist.append(iproutemask.val)
            hoplist.append(iproutenexthop.val)
        finallist.append(destlist)
        finallist.append(masklist)
        finallist.append(hoplist)
        print len(finallist[0])
        return finallist


def main():
    r = Router('198.51.100.3', 'password')
    print r.retrieveHostname()
    print r.retrieveContact()
    print r.retrieveLocation()
    print r.retrieveRouteTable()


if __name__ == '__main__':
    main()
