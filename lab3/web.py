import flask
import SNMPTool

app = flask.Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    return flask.render_template('home.html', pagename='SNMP: Lab 3 Homepage')

@app.route("/monitor", methods=['GET', 'POST'])
def monitor():
    if flask.request.method == 'POST':
        ip = flask.request.form['routerip']
        router = SNMPTool.Router(ip, 'password')
        sysname = router.retrieveHostname()
        syscontact = router.retrieveContact()
        sysuptime = router.retrieveUptime()
        syslocation = router.retrieveLocation()
        routetable = router.retrieveRouteTable()
        lsize=len(routetable[0])
        return flask.render_template('monitor.html', router=ip,
                    sysname=sysname, syscontact=syscontact,
                    sysuptime = sysuptime, syslocation = syslocation,
                    routetable=routetable, destlist=routetable[0],
                    masklist=routetable[1], hoplist=routetable[2],
                    lsize=lsize)

@app.route("/change", methods=['GET', 'POST'])
def change():
    if flask.request.method == 'POST':
        ip = flask.request.form['routerip']
        router = SNMPTool.Router(ip, 'password')
        if flask.request.form['attribute'] == 'hostname':
            sysname = router.setHostname(flask.request.form['newvalue'])
        elif flask.request.form['attribute'] == 'contact':
            syscontact = router.setContact(flask.request.form['newvalue'])
        elif flask.request.form['attribute'] == 'location':
            syslocation = router.setLocation(flask.request.form['newvalue'])
        sysname = router.retrieveHostname()
        syscontact = router.retrieveContact()
        sysuptime = router.retrieveUptime()
        syslocation = router.retrieveLocation()
        routetable = router.retrieveRouteTable()
        lsize=len(routetable[0])
        return flask.render_template('monitor.html', router=ip,
                    sysname=sysname, syscontact=syscontact,
                    sysuptime = sysuptime, syslocation = syslocation,
                    routetable=routetable, destlist=routetable[0],
                    masklist=routetable[1], hoplist=routetable[2],
                    lsize=lsize)



if __name__ == '__main__':
    app.run(debug=True)
