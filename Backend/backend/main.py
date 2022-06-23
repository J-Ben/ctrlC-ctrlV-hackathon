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
    projects = saagie.API.projects.list()
    for  project in projects['projects']:
        projectId = project['id']
        # respo = cloneHandler.handler(name, projectId)
        response = "{\n"
 
        info = saagie.API.projects.get_info(projectId)
 
        response = response +  str(info['project'])
        info = saagie.API.projects.get_rights(projectId)
        response = response + str(info['rights']) + "{\n"
 
        respo = saagie.API.jobs.list_for_project(project_id=projectId, instances_limit=2)
        for job in respo['jobs']:
            response = response +"{\n"
            result= saagie.API.jobs.get_info(job_id=job['id'], instances_limit=2)
            response = response + str(result)+ "\n}"
 
        response = response +"\n}\n{"
 
        respo = saagie.API.apps.list_for_project(project_id = projectId)
        for app in respo['labWebApps']:
 
            response = response +"{\n"+ str(app)+ "\n}"
 
 
        response = response +"\n}\n{"
 
        respo = saagie.API.pipelines.list_for_project(project_id= projectId)
        for app in respo['project']['pipelines']:
 
            response = response +"{\n"+ str(app)+ "\n}"
 
        response = response +"\n}\n{"
 
        respo = saagie.API.docker_credentials.list_for_project(project_id= projectId)
        for app in respo['allDockerCredentials']:
 
            response = response +"{\n"+ str(app)+ "\n}"
 
    return response + "\n}"



if __name__ == "__main__":
    app.run()