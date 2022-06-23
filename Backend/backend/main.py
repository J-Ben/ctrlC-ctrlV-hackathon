from flask import Flask
import json
import variables.saagie as saagie
from flask import request
import controllers.clone as cloneHandler
import variables.request as configAPI


app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world !!!!!"


@app.route('/clone', methods = ['POST'])
def clone():
    
    name = request.form['name']
    projectId = request.form['id']
    respo = cloneHandler.handler(name, projectId)
    return respo
    


if __name__ == "__main__":
    app.run()
