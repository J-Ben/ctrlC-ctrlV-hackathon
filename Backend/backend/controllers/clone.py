import variables.saagie as saagie
import variables.request as configAPI
import requests
from flask import Flask
import json


def handler(name, projectId):
    currentProject = saagie.API.projects.get_info(projectId)
    newProject = saagie.API.projects.create(name='"'+name+'"',
                                            group="estiam_g14_hackaton",
                                            role='Manager',
                                            description=currentProject['project']['description'])

    return projectId