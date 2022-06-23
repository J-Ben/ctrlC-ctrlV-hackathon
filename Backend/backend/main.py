from flask import Flask
import variables.saagie as saagie
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "Hello world !!!!!"


@app.route('/test')
def a():
    projects = saagie.API.projects.list(id)
    return projects
    
@app.route('/test/<string:idproject>')
def pinfo(idproject):
    
    info = saagie.API.jobs.get_info(idproject)
    return info

@app.route('/testjob/<string:idjob>')
def jinfo(idjob):
    
    infojob = saagie.API.jobs.get_info(idjob)
    return infojob


if __name__ == "__main__":
    app.run()
