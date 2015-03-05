import flask

app = flask.Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    return flask.render_template('home.html', pagename='SNMP: Lab 3 Homepage')

@app.route("/monitor", methods=['GET', 'POST'])
def monitor():
    router = flask.request.form['ip1']
    return flask.render_template('monitor.html', router=router)

if __name__ == '__main__':
    app.run(debug=True)
