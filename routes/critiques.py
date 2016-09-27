
from flask import jsonify, request, Blueprint
from model import *
from routes import constants
from routes import commons
import routes

crit_api = Blueprint('crit_api', __name__)

############################### critiques ####################################
@crit_api.route('/critiques')
def get_critiques():
    try:
        return commons.get_all_records_paginated__sort(request.args, Answer)
    except Exception as error:
        return jsonify(error=error.message)

@crit_api.route('/critiques/score')
def get_critique_by_score():

    try:
        crits = commons.get_records_int_greater_or_less_than(request.args, Answer, Answer.score)
        crits = commons.paginate_and_sort_records(request.args, crits, Answer)
    except Exception as error:
        return jsonify(error=error.message)

    return jsonify(page=crits.page, totalpages=crits.pages, records=[item.to_dict() for item in crits.items])

@crit_api.route('/critiques/rank')
def get_critique_by_rank():

    try:
        crits = commons.get_records_int_greater_or_less_than(request.args, Answer, Answer.rank)
        crits = commons.paginate_and_sort_records(request.args, crits, Answer)
    except Exception as error:
        return jsonify(error=error.message)

    return jsonify(page=crits.page, totalpages=crits.pages, records=[item.to_dict() for item in crits.items])

@crit_api.route('/critiques/<crit_id>')
def get_critique_by_id(crit_id):
    crit = Answer.query.get(crit_id)
    return jsonify(critique=crit.to_dict())

@crit_api.route('/critiques/evaluation_mode_id/<eval_mode>')
def get_critique_by_eval_mode(eval_mode):

    crits = Answer.query.filter_by(evaluation_mode_id=eval_mode)

    try:
        crits = commons.paginate_and_sort_records(request.args, crits, Answer)
    except Exception as error:
        return jsonify(error=error.message)

    return jsonify(page=crits.page, totalpages=crits.pages, records=[item.to_dict() for item in crits.items])

@crit_api.route('/critiques/artifact_id/<artifact_id>')
def get_critique_by_artifact_id(artifact_id):
    crits = Answer.query.filter_by(assessee_artifact_id=artifact_id).all()
    return jsonify(records=[item.to_dict() for item in crits])


@crit_api.route('/critiques/create_in_task_id')
def get_critique_by_create_in_task_id_range():

    try:
        crits = commons.get_records_str_greater_or_less_than(request.args, Answer, Answer.create_in_task_id)
        crits = commons.paginate_and_sort_records(request.args, crits, Answer)
    except Exception as error:
        return jsonify(error=error.message)

    return jsonify(page=crits.page, totalpages=crits.pages, records=[item.to_dict() for item in crits.items])

@crit_api.route('/critiques/create_in_task_id/<task_id>')
def get_critique_by_create_in_task_id(task_id):

    crits = Answer.query.filter_by(create_in_task_id=task_id)

    try:
        crits = commons.paginate_and_sort_records(request.args, crits, Answer)
    except Exception as error:
        return jsonify(error=error.message)

    return jsonify(page=crits.page, totalpages=crits.pages, records=[item.to_dict() for item in crits.items])

@crit_api.route('/critiques/create_in_task_id/<task_id>/assessor_id/<assessor_id>')
def get_critique_by_create_in_task_id_and_assessor_id(task_id, assessor_id):

    crits = Answer.query.filter_by(create_in_task_id=task_id, assessor_actor_id=assessor_id)

    try:
        crits = commons.paginate_and_sort_records(request.args, crits, Answer)
    except Exception as error:
        return jsonify(error=error.message)

    return jsonify(page=crits.page, totalpages=crits.pages, records=[item.to_dict() for item in crits.items])

@crit_api.route('/critiques/create_in_task_id/<task_id>/assessee_id/<assessee_id>')
def get_critique_by_create_in_task_id_and_assessee_id(task_id, assessee_id):

    crits = Answer.query.filter_by(create_in_task_id=task_id, assessee_actor_id=assessee_id)

    try:
        crits = commons.paginate_and_sort_records(request.args, crits, Answer)
    except Exception as error:
        return jsonify(error=error.message)

    return jsonify(page=crits.page, totalpages=crits.pages, records=[item.to_dict() for item in crits.items])

@crit_api.route('/critiques/assessor_id/<assessor_id>/assessee_id/<assessee_id>')
def get_critiques_by_assessor_id_and_assessee_id(assessor_id, assessee_id):

    crits = Answer.query.filter_by(assessor_actor_id=assessor_id, assessee_actor_id=assessee_id)

    try:
        crits = commons.paginate_and_sort_records(request.args, crits, Answer)
    except Exception as error:
        return jsonify(error=error.message)

    return jsonify(page=crits.page, totalpages=crits.pages, records=[item.to_dict() for item in crits.items])

