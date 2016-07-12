from flask import jsonify, request, Blueprint
from datetime import datetime
from model import *
from routes import commons

task_api = Blueprint('task_api', __name__)

@task_api.route('/tasks')
def get_tasks():
    return commons.get_all_records_paginated__sort(request.args, Task)

@task_api.route('/tasks/<id>')
def get_task_by_id(id):
    task = Task.query.get(id)
    return jsonify(task=task.to_dict())


@task_api.route('/tasks/task_type/<task_type>')
def get_tasks_by_task_type(task_type):

    tasks = Task.query.filter_by(task_type=task_type)

    try:
        tasks = commons.paginate_and_sort_records(request.args, tasks, Task)
    except Exception as error:
        return jsonify(error=error.message)

    return jsonify(page=tasks.page, totalpages=tasks.pages, records=[item.to_dict() for item in tasks.items])


@task_api.route('/tasks/assignment_title/<assignment_title>')
def get_tasks_by_assignment_title(assignment_title):

    tasks = Task.query.filter(Task.assignment_title.ilike("%" + assignment_title + "%"))

    try:
        tasks = commons.paginate_and_sort_records(request.args, tasks, Task)
    except Exception as error:
        return jsonify(error=error.message)

    return jsonify(page=tasks.page, totalpages=tasks.pages, records=[item.to_dict() for item in tasks.items])

@task_api.route('/tasks/task_description/<task_description>')
def get_tasks_by_task_description(task_description):

    tasks = Task.query.filter(Task.task_description.ilike("%" + task_description + "%"))
    try:
        tasks = commons.paginate_and_sort_records(request.args, tasks, Task)
    except Exception as error:
        return jsonify(error=error.message)
    return jsonify(page=tasks.page, totalpages=tasks.pages, records=[item.to_dict() for item in tasks.items])

@task_api.route('/tasks/start')
def get_tasks_by_starts_at():

    #follow ISO 8601 date notation
    try:
        tasks = commons.get_records_datetime_greater_or_less_than(request.args, Task, Task.starts_at)
        tasks = commons.paginate_and_sort_records(request.args, tasks, Task)
    except Exception as error:
        return jsonify(error=error.message)

    return jsonify(page=tasks.page, totalpages=tasks.pages, records=[item.to_dict() for item in tasks.items])
@task_api.route('/tasks/end')
def get_tasks_by_ends_at():

    #follow ISO 8601 date notation
    try:
        tasks = commons.get_records_datetime_greater_or_less_than(request.args, Task, Task.ends_at)
        tasks = commons.paginate_and_sort_records(request.args, tasks, Task)
    except Exception as error:
        return jsonify(error=error.message)

    return jsonify(page=tasks.page, totalpages=tasks.pages, records=[item.to_dict() for item in tasks.items])


@task_api.route('/tasks/start_end_between/<start>/<end>')
def get_tasks_by_start_end_between(start, end):

    #follow ISO 8601 date notation
    start_date_object = datetime.strptime(start, '%Y-%m-%d %H:%M')
    end_date_object = datetime.strptime(end, '%Y-%m-%d %H:%M')

    tasks = Task.query.filter(Task.starts_at >= start_date_object, Task.ends_at <= end_date_object)

    try:
        tasks = commons.paginate_and_sort_records(request.args, tasks, Task)
    except Exception as error:
        return jsonify(error=error.message)

    return jsonify(page=tasks.page, totalpages=tasks.pages, records=[item.to_dict() for item in tasks.items])

@task_api.route('/tasks/organization_title/<organization_title>')
def get_tasks_by_organization_title(organization_title):

    tasks = Task.query.filter(Task.organization_title.ilike("%" + organization_title + "%"))

    try:
        tasks = commons.paginate_and_sort_records(request.args, tasks, Task)
    except Exception as error:
        return jsonify(error=error.message)

    return jsonify(page=tasks.page, totalpages=tasks.pages, records=[item.to_dict() for item in tasks.items])

@task_api.route('/tasks/owner_name/<owner_name>')
def get_tasks_by_owner_name(owner_name):

    tasks = Task.query.filter(Task.owner_name.ilike("%" + owner_name + "%"))

    try:
        tasks = commons.paginate_and_sort_records(request.args, tasks, Task)
    except Exception as error:
        return jsonify(error=error.message)

    return jsonify(page=tasks.page, totalpages=tasks.pages, records=[item.to_dict() for item in tasks.items])

@task_api.route('/tasks/course_title/<course_title>')
def get_tasks_by_course_title(course_title):

    tasks = Task.query.filter(Task.course_title.ilike("%" + course_title + "%"))

    try:
        tasks = commons.paginate_and_sort_records(request.args, tasks, Task)
    except Exception as error:
        return jsonify(error=error.message)

    return jsonify(page=tasks.page, totalpages=tasks.pages, records=[item.to_dict() for item in tasks.items])

@task_api.route('/tasks/cip_level1_code/<cip_level1_code>')
def get_tasks_by_cip_level1_code(cip_level1_code):

    tasks = Task.query.filter_by(cip_level1_code=cip_level1_code)

    try:
        tasks = commons.paginate_and_sort_records(request.args, tasks, Task)
    except Exception as error:
        return jsonify(error=error.message)

    return jsonify(page=tasks.page, totalpages=tasks.pages, records=[item.to_dict() for item in tasks.items])

@task_api.route('/tasks/cip_level2_code/<cip_level2_code>')
def get_tasks_by_cip_level2_code(cip_level2_code):

    tasks = Task.query.filter_by(cip_level2_code=cip_level2_code)

    try:
        tasks = commons.paginate_and_sort_records(request.args, tasks, Task)
    except Exception as error:
        return jsonify(error=error.message)

    return jsonify(page=tasks.page, totalpages=tasks.pages, records=[item.to_dict() for item in tasks.items])

@task_api.route('/tasks/cip_level3_code/<cip_level3_code>')
def get_tasks_by_cip_level3_code(cip_level3_code):

    tasks = Task.query.filter_by(cip_level3_code=cip_level3_code)

    try:
        tasks = commons.paginate_and_sort_records(request.args, tasks, Task)
    except Exception as error:
        return jsonify(error=error.message)

    return jsonify(page=tasks.page, totalpages=tasks.pages, records=[item.to_dict() for item in tasks.items])