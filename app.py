from flask import Flask 

app = Flask(__name__)

#create root for routes to branch off from 

@app.route('/')

def hello_world():
    return 'Hello World'
