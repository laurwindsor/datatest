from flask import Flask
app = Flask(__name__)

@app.route('/')
def v1():
    return 'App version 1'

@app.route('/v2')
def v2():
    return 'App version 2'