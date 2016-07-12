from flask import jsonify, request, Blueprint
from datetime import datetime
from model import *
from routes import constants
from routes import commons
import routes

task_api = Blueprint('task_api', __name__)

@task_api.route('/tasks')
def get_tasks():
    return commons.get_entities(Task)

@task_api.route('/tasks/<id>')
def get_task_by_id(id):
    task = Task.query.get(id)
    return jsonify(task=task.to_dict())


@task_api.route('/tasks/task_type/<task_type>')
def get_tasks_by_task_type(task_type):
    page = constants.DEFAULT_START_PAGE
    pagelength = constants.DEFAULT_PAGE_LENGTH

    try:
        if 'page' in request.args:
            page = int(request.args.get('page'))
        if 'pagelength' in request.args:
            pagelength = int(request.args.get('pagelength'))
        if 'orderby' in request.args:
            orderby = request.args.get('orderby')
        if 'order' in request.args:
            order = request.args.get('order')
    except:
        return jsonify(error="page and pagelength must be numbers")

    tasks = Task.query.filter_by(task_type=task_type)

    if 'orderby' in locals() and orderby in Task.__dict__:
        if 'order' in locals() and order in ['desc', 'asc']:
            orderby = orderby + " " + order
        tasks = tasks.order_by(routes.db.text(orderby))
    elif 'orderby' in locals() and orderby not in Task.__dict__:
        return jsonify(error="can't find the property to order the records")

    tasks = tasks.paginate(page, pagelength, False)

    return jsonify(page=tasks.page, totalpages=tasks.pages, records=[item.to_dict() for item in tasks.items])


@task_api.route('/tasks/assignment_title/<assignment_title>')
def get_tasks_by_assignment_title(assignment_title):
    page = constants.DEFAULT_START_PAGE
    pagelength = constants.DEFAULT_PAGE_LENGTH

    try:
        if 'page' in request.args:
            page = int(request.args.get('page'))
        if 'pagelength' in request.args:
            pagelength = int(request.args.get('pagelength'))
        if 'orderby' in request.args:
            orderby = request.args.get('orderby')
        if 'order' in request.args:
            order = request.args.get('order')
    except:
        return jsonify(error="page and pagelength must be numbers")

    tasks = Task.query.filter(Task.assignment_title.ilike("%" + assignment_title + "%"))

    if 'orderby' in locals() and orderby in Task.__dict__:
        if 'order' in locals() and order in ['desc', 'asc']:
            orderby = orderby + " " + order
        tasks = tasks.order_by(routes.db.text(orderby))
    elif 'orderby' in locals() and orderby not in Task.__dict__:
        return jsonify(error="can't find the property to order the records")

    tasks = tasks.paginate(page, pagelength, False)

    return jsonify(page=tasks.page, totalpages=tasks.pages, records=[item.to_dict() for item in tasks.items])

@task_api.route('/tasks/task_description/<task_description>')
def get_tasks_by_task_description(task_description):
    page = constants.DEFAULT_START_PAGE
    pagelength = constants.DEFAULT_PAGE_LENGTH

    try:
        if 'page' in request.args:
            page = int(request.args.get('page'))
        if 'pagelength' in request.args:
            pagelength = int(request.args.get('pagelength'))
        if 'orderby' in request.args:
            orderby = request.args.get('orderby')
        if 'order' in request.args:
            order = request.args.get('order')
    except:
        return jsonify(error="page and pagelength must be numbers")

    tasks = Task.query.filter(Criterion.task_description.ilike("%" + task_description + "%"))

    if 'orderby' in locals() and orderby in Task.__dict__:
        if 'order' in locals() and order in ['desc', 'asc']:
            orderby = orderby + " " + order
        tasks = tasks.order_by(routes.db.text(orderby))
    elif 'orderby' in locals() and orderby not in Task.__dict__:
        return jsonify(error="can't find the property to order the records")

    tasks = tasks.paginate(page, pagelength, False)

    return jsonify(page=tasks.page, totalpages=tasks.pages, records=[item.to_dict() for item in tasks.items])



@task_api.route('/tasks/start_end_between/<start>/<end>')
def get_tasks_by_start_end_between(start, end):
    page = constants.DEFAULT_START_PAGE
    pagelength = constants.DEFAULT_PAGE_LENGTH

    try:
        if 'page' in request.args:
            page = int(request.args.get('page'))
        if 'pagelength' in request.args:
            pagelength = int(request.args.get('pagelength'))
        if 'orderby' in request.args:
            orderby = request.args.get('orderby')
        if 'order' in request.args:
            order = request.args.get('order')
    except:
        return jsonify(error="page and pagelength must be numbers")
    start_date_object = datetime.strptime(start, '%Y-%m-%d %H:%M')
    end_date_object = datetime.strptime(end, '%Y-%m-%d %H:%M')

    tasks = Task.query.filter(Task.starts_at >= start_date_object, Task.ends_at <= end_date_object)

    if 'orderby' in locals() and orderby in Task.__dict__:
        if 'order' in locals() and order in ['desc', 'asc']:
            orderby = orderby + " " + order
        tasks = tasks.order_by(routes.db.text(orderby))
    elif 'orderby' in locals() and orderby not in Task.__dict__:
        return jsonify(error="can't find the property to order the records")

    tasks = tasks.paginate(page, pagelength, False)

    return jsonify(page=tasks.page, totalpages=tasks.pages, records=[item.to_dict() for item in tasks.items])