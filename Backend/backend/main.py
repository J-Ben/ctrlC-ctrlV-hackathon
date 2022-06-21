from flask import Flask
import variables.saagie as saagie

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world !!!!!"


@app.route('/test')
def a():
    projects = saagie.API.projects.list()
    return projects
    


if __name__ == "__main__":
    app.run()
