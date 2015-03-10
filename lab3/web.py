'''
web.py

This file defines this particular 
snmp web application using the Python Flask microframework.

'''

import flask
import SNMPTool

app = flask.Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
'''
Handles the main web page.
Asks for an ip to monitor.
'''
def home():
    return flask.render_template('home.html', pagename='SNMP: Main Page')

@app.route("/monitor", methods=['GET', 'POST'])
'''
Handles the monitor page.
Displays router attributes:
    hostname, location, contact, uptime, routing table, cdp neighbors
Asks for changes to the page refresh rate and hostname, location, contact
'''
def monitor():
    if flask.request.method == 'POST':
            if flask.request.form.get('routerip') is not None:
                flask.session['ip'] = flask.request.form['routerip']
            if flask.request.form.get('rate') is None:
                flask.session['rrate'] = "60"
            else:
                flask.session['rrate'] = flask.request.form['rate']
    router = SNMPTool.Router(flask.session['ip'], 'public')
    sysname = router.retrieveHostname()
    syscontact = router.retrieveContact()
    sysuptime = router.retrieveUptime()
    syslocation = router.retrieveLocation()
    routetable = router.retrieveRouteTable()
    cdptable = router.retrieveCDPneighbors()
    cdpsize = len(cdptable[0])
    routesize=len(routetable[0])
    return flask.render_template('monitor.html', router=flask.session['ip'],
                    sysname=sysname, syscontact=syscontact,
                    sysuptime = sysuptime, syslocation = syslocation,
                    routetable=routetable, destlist=routetable[0],
                    masklist=routetable[1], hoplist=routetable[2],
                    metriclist=routetable[3], routesize=routesize, cdpsize = cdpsize,
                    idlist = cdptable[0], portlist = cdptable[1], rrate=flask.session['rrate'])

@app.route("/change", methods=['POST'])
'''
Called in the monitor page.
Handles the changing the hostname, contact, and location
'''
def change():
    router = SNMPTool.Router(flask.session['ip'], 'public')
    if flask.request.form['attribute'] == 'hostname':
        sysname = router.setHostname(flask.request.form['newvalue'])
    elif flask.request.form['attribute'] == 'contact':
        syscontact = router.setContact(flask.request.form['newvalue'])
    elif flask.request.form['attribute'] == 'location':
        syslocation = router.setLocation(flask.request.form['newvalue'])
    return flask.redirect(flask.url_for('monitor'))

app.secret_key = 'bob'

if __name__ == '__main__':
    app.run(debug=True)
