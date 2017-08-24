#!flask/bin/python
from flask import render_template
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/submit/')
def submit():
    return "valami"



if __name__ == '__main__':
    app.run(host='0.0.0.0')
