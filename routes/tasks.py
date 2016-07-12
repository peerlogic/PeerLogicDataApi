from flask import jsonify, request, Blueprint
from model import *
from routes import constants
from routes import commons
import routes

task_api = Blueprint('task_api', __name__)

@task_api.route('/critiques')
def get_critiques():
    return commons.get_entities(Task)

@task_api.route('/tasks/<id>')
def get_artifacts_by_id(id):
    task = Task.query.get(id)
    return jsonify(task=task.to_dict())
