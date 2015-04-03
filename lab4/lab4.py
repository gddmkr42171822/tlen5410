'''
Lab 4
Names: Robert Werthman, Dallas Hays

Sources:
1. http://www.mkyong.com/python/how-do-send-email-in-python-via-smtplib/
- How to send an email with python and smtp.

2. Cisco SNMP Object Navigator
- Look up oid of managed objects

'''

import re
import smtplib
import lab1

'''
Emails an email address if a specified trap occurs.
'''
def emailAdmin(error):
    fromaddr = "bobdallas.tlen5540@gmail.com"
    password = "netman2015"
    toaddrs = "robert.werthman@colorado.edu"
    msg = 'To:' + toaddrs + '\n' + 'From: ' + fromaddr + '\n' + 'Subject:lab4 \n'
    msg = msg + '\n' + error + '\n\n'
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.ehlo
    server.login(fromaddr, password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()

'''
If a config trap is generated this method gets a copy of the router config
and saves it if there are changes.  It then emails the admin about the trap.
'''
def handleConfigTrap(ip, trap):
    ip = ip.strip('[]')
    lab1.getConfig(ip)
    lab1.saveConfig(ip)
    error = '\n'.join(trap)
    emailAdmin(error)

'''
Emails the admin if there is a link state change.
'''
def handleLinkTrap(trap):
    error = '\n'.join(trap)
    emailAdmin(error)

'''
Emails the admin if a rsing threshold is met for incoming bytes on an
interface
'''
def handlePingTrap(trap):
    error = '\n'.join(trap)
    emailAdmin(error)

'''
This method determines which trap was received and calls the appropriate
trap handler.
'''
def handleTrap(trap):
    prog = re.compile('(\[[0-9]+\.[0-9]+\.[0-9]+\.[0-9]\])')
    ip = ''
    for line in trap:
        matchIP = prog.search(line)
        if matchIP:
            ip =  matchIP.group(0)
        if "SNMPv2-SMI::enterprises.9.9.43.2.0.1" in line:
            handleConfigTrap(ip, trap)
            break
        elif any(substring in line for substring in ["linkUp", "linkDown"]):
            handleLinkTrap(trap)
            break
        elif "SNMPv2-SMI::mib-2.16.0.1" in line:
            handlePingTrap(trap)

'''
Waits on the command line for all the lines of a snmp trap and then handles
the trap.
'''
def main():
    trap = []
    while True:
        try:
            line = raw_input()
            trap.append(line)
        except EOFError:
            break
    handleTrap(trap)

if __name__=='__main__':
    main()
