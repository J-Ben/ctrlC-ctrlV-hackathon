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


#fonction permettant de recuperer la taille d'une liste
def length_liste(liste):
    count = 0
    if isinstance(liste, list):
        if len(liste) == 0:
           count = 0
        else:
           for item in liste:
              count += 1
    else:
        count = 0
    
    return count
#Fonction permettant de parcourir un dictionnaire    
def list_dict(dict_list):
    k = 0
    for v in dict_list.values():
        length_list(v)
        k = length_list(v)
    return k
    
#Fonction permettant de parcourir 2 dictionnaire    
def list_dictpipe(dict_list):
    k = 0
    for v in dict_list.values():
        if isinstance(v, dict):
            for u in v.values():
              length_list(u)
              k = length_list(u)
    return {"": k}
    
    
@app.route('/countpipe/<string:proj_id>',  methods=['GET'])   
def get_lis_pipe(proj_id):
    appsinfo = saagie.API.pipelines.list_for_project(proj_id)
    listp = list_dictpipe(appsinfo)
    return listp


@app.route('/audit_count/<string:proj_id>')
def count_all(proj_id):
    jobsinfo = saagie.API.jobs.list_for_project(proj_id)
    pipelineinfo = saagie.API.pipelines.list_for_project(proj_id)
    appsinfo = saagie.API.apps.list_for_project(proj_id)
    dic_lisjb = jobsinfo
    dic_lisap = appsinfo
    dic_lispp = pipelineinfo
    return {'countjob': list_dict(dic_lisjb),'countpipeline': list_dictpipe(dic_lispp), 'countapp': list_dict(dic_lisap)} 

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
