from flask import Flask
import os
import flask
from flask import request, jsonify, make_response
import variables.saagie as saagie


@app.route('/projectinfo',  methods=['GET'])
def get_info_projet():
    proj_id="db844ca5-4041-4661-917d-0ba8ea6dd086"
    projetinfo = saagie.API.projects.get_info(proj_id)
    return projetinfo
    
@app.route('/pipeinfo',  methods=['GET'])
def get_info_pipe():
    proj_id="db844ca5-4041-4661-917d-0ba8ea6dd086"
    pipesinfo = saagie.API.pipelines.list_for_project(proj_id)
    return pipesinfo
    
@app.route('/jobinfo',  methods=['GET'])   
def get_info_job():
    proj_id="db844ca5-4041-4661-917d-0ba8ea6dd086"
    jobsinfo = saagie.API.jobs.list_for_project(proj_id)
    return jobsinfo


@app.route('/appinfo',  methods=['GET'])   
def get_info_app():
    proj_id="db844ca5-4041-4661-917d-0ba8ea6dd086"
    appsinfo = saagie.API.apps.list_for_project(proj_id)
    return appsinfo


def count_keys(dict):
    count = 0
    
    for i in enumerate(dict):
        count += 1
    return count

@app.route('/audit')
def get_audit_project():
    dict1 = saagie.API.apps.list_for_project("db844ca5-4041-4661-917d-0ba8ea6dd086")
    return print(count_keys(dict1))
