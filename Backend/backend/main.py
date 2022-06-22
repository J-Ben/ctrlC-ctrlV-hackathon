from pydoc import resolve
from flask import Flask
import os
import flask
from flask import request, jsonify, make_response
import variables.saagie as saagie
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "Hello world Lyse !!!!!"

@app.route('/test')
def a():
    projects = saagie.API.projects.list()
    return projects



def length_list(list):
    count = 0
    for item in list:
        count += 1
    return count
    
def list_dict(dict_list):
    k = 0
    for v in dict_list.values():
        length_list(v)
        k = length_list(v)
    return k
 

@app.route('/audit_count/<string:proj_id>')
def count_all(proj_id):
    jobsinfo = saagie.API.jobs.list_for_project(proj_id)
    pipelineinfo = saagie.API.pipelines.list_for_project(proj_id)
    appsinfo = saagie.API.apps.list_for_project(proj_id)
    dic_lisjb = jobsinfo
    dic_lisap = appsinfo
    dic_lispp = pipelineinfo
    return {'countjob': list_dict(dic_lisjb),'countpipeline': list_dict(dic_lispp), 'countapp': list_dict(dic_lisap)} 




if __name__ == "__main__":
    app.run()
