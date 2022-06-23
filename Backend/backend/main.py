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


#fonction permett
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

@app.route('/appinfo/<string:proj_id>',  methods=['GET'])   
def get_info_app(proj_id):
    appsinfo = saagie.API.apps.list_for_project(proj_id)
    return appsinfo


@app.route('/jobinfo/<string:proj_id>',  methods=['GET'])   
def get_info_job(proj_id):
    jobsinfo = saagie.API.jobs.list_for_project(proj_id)
    return jobsinfo

@app.route('/pipeinfo/<string:proj_id>',  methods=['GET'])   
def get_info_pipe(proj_id):
    pipesinfo = saagie.API.pipelines.list_for_project(proj_id)
    return pipesinfo
    

@app.route('/projinfo/<string:proj_id>',  methods=['GET'])   
def get_info_proj(proj_id):
    projtsinfo = saagie.API.projects.get_info(proj_id)
    return projtsinfo

@app.route('/vareninfo/<string:proj_id>',  methods=['GET'])   
def get_info_varenv(proj_id):
    envvarinfo = saagie.API.env_vars.list_for_project(proj_id)
    return envvarinfo


if __name__ == "__main__":
    app.run()
