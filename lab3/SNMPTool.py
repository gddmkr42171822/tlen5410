import netsnmp

class Router(object):

    def __init__(self, desthost, community):
        self.session = netsnmp.Session(DestHost=desthost, Community=community,
                                Version = 1)

    def retrieveHostname(self):
        sysname = netsnmp.Varbind('.1.3.6.1.2.1.1.5.0')
        varlist = netsnmp.VarList(sysname)
        self.session.get(varlist)
        return sysname.val

    def retrieveContact(self):
        syscontact = netsnmp.Varbind('.1.3.6.1.2.1.1.4.0')
        varlist = netsnmp.VarList(syscontact)
        self.session.get(varlist)
        return syscontact.val

def main():
    r = Router('198.51.100.3', 'password')
    print r.retrieveHostname()
    print r.retrieveContact()

if __name__ == '__main__':
    main()
