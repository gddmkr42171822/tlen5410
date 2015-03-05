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
        return flask.render_template('monitor.html', router=ip, sysname=sysname,
                                syscontact=syscontact)

if __name__ == '__main__':
    app.run(debug=True)
