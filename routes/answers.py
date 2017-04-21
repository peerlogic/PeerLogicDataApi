from flask import jsonify, request, Blueprint

from model import *
from routes import commons
from datetime import datetime
crit_api = Blueprint('crit_api', __name__)

############################### critiques ####################################
@crit_api.route('/answers')
def get_answers():
    try:
        return commons.get_all_records_paginated__sort(request.args, Answer)
    except Exception as error:
        return jsonify(error=error.message)

@crit_api.route('/answers/score')
def get_answers_by_score():

    try:
        crits = commons.get_records_int_greater_or_less_than(request.args, Answer, Answer.score)
        crits = commons.paginate_and_sort_records(request.args, crits, Answer)
    except Exception as error:
        return jsonify(error=error.message)

    return jsonify(page=crits.page, totalpages=crits.pages, records=[item.to_dict() for item in crits.items])

@crit_api.route('/answers/rank')
def get_answers_by_rank():

    try:
        crits = commons.get_records_int_greater_or_less_than(request.args, Answer, Answer.rank)
        crits = commons.paginate_and_sort_records(request.args, crits, Answer)
    except Exception as error:
        return jsonify(error=error.message)

    return jsonify(page=crits.page, totalpages=crits.pages, records=[item.to_dict() for item in crits.items])

@crit_api.route('/answers/<crit_id>')
def get_answers_by_id(crit_id):
    crit = Answer.query.get(crit_id)
    return jsonify(critique=crit.to_dict())

@crit_api.route('/answers/evaluation_mode_id/<eval_mode>')
def get_answers_by_eval_mode(eval_mode):

    crits = Answer.query.filter_by(evaluation_mode_id=eval_mode)

    try:
        crits = commons.paginate_and_sort_records(request.args, crits, Answer)
    except Exception as error:
        return jsonify(error=error.message)

    return jsonify(page=crits.page, totalpages=crits.pages, records=[item.to_dict() for item in crits.items])

@crit_api.route('/answers/artifact_id/<artifact_id>')
def get_answers_by_artifact_id(artifact_id):
    crits = Answer.query.filter_by(assessee_artifact_id=artifact_id).all()
    return jsonify(records=[item.to_dict() for item in crits])


@crit_api.route('/answers/create_in_task_id')
def get_answers_by_create_in_task_id_range():

    try:
        crits = commons.get_records_str_greater_or_less_than(request.args, Answer, Answer.create_in_task_id)
        crits = commons.paginate_and_sort_records(request.args, crits, Answer)
    except Exception as error:
        return jsonify(error=error.message)

    return jsonify(page=crits.page, totalpages=crits.pages, records=[item.to_dict() for item in crits.items])

@crit_api.route('/answers/create_in_task_id/<task_id>')
def get_answers_by_create_in_task_id(task_id):

    crits = Answer.query.filter_by(create_in_task_id=task_id)

    try:
        crits = commons.paginate_and_sort_records(request.args, crits, Answer)
    except Exception as error:
        return jsonify(error=error.message)

    return jsonify(page=crits.page, totalpages=crits.pages, records=[item.to_dict() for item in crits.items])

@crit_api.route('/answers/create_in_task_id/<task_id>/assessor_id/<assessor_id>')
def get_answers_by_create_in_task_id_and_assessor_id(task_id, assessor_id):

    crits = Answer.query.filter_by(create_in_task_id=task_id, assessor_actor_id=assessor_id)

    try:
        crits = commons.paginate_and_sort_records(request.args, crits, Answer)
    except Exception as error:
        return jsonify(error=error.message)

    return jsonify(page=crits.page, totalpages=crits.pages, records=[item.to_dict() for item in crits.items])

@crit_api.route('/answers/create_in_task_id/<task_id>/assessee_id/<assessee_id>')
def get_answers_by_create_in_task_id_and_assessee_id(task_id, assessee_id):

    crits = Answer.query.filter_by(create_in_task_id=task_id, assessee_actor_id=assessee_id)

    try:
        crits = commons.paginate_and_sort_records(request.args, crits, Answer)
    except Exception as error:
        return jsonify(error=error.message)

    return jsonify(page=crits.page, totalpages=crits.pages, records=[item.to_dict() for item in crits.items])

@crit_api.route('/answers/assessor_id/<assessor_id>/assessee_id/<assessee_id>')
def get_answers_by_assessor_id_and_assessee_id(assessor_id, assessee_id):

    crits = Answer.query.filter_by(assessor_actor_id=assessor_id, assessee_actor_id=assessee_id)

    try:
        crits = commons.paginate_and_sort_records(request.args, crits, Answer)
    except Exception as error:
        return jsonify(error=error.message)

    return jsonify(page=crits.page, totalpages=crits.pages, records=[item.to_dict() for item in crits.items])



@crit_api.route('/answers/submitted_at')
def get_get_answers_submitted_at():

    #follow ISO 8601 date notation
    try:
        crits = commons.get_records_datetime_greater_or_less_than(request.args, Answer, Answer.submitted_at)
        crits = commons.paginate_and_sort_records(request.args, crits, Answer)
    except Exception as error:
        return jsonify(error=error.message)

    return jsonify(page=crits.page, totalpages=crits.pages, records=[item.to_dict() for item in crits.items])

# @crit_api.route('/answers/submitted_before')
# def get_answers_submitted_before():
#
#     #follow ISO 8601 date notation
#     try:
#         crits = commons.get_records_datetime_greater_or_less_than(request.args, Answer, Answer.submitted_at)
#         crits = commons.paginate_and_sort_records(request.args, crits, Answer)
#     except Exception as error:
#         return jsonify(error=error.message)
#
#     return jsonify(page=crits.page, totalpages=crits.pages, records=[item.to_dict() for item in crits.items])


@crit_api.route('/answers/submitted_between/<start>/<end>')
def get_tasks_by_start_end_between(start, end):

    #follow ISO 8601 date notation
    start_date_object = datetime.strptime(start, '%Y-%m-%d %H:%M')
    end_date_object = datetime.strptime(end, '%Y-%m-%d %H:%M')

    crits = Answer.query.filter(Answer.submitted_at >= start_date_object, Answer.submitted_at <= end_date_object)

    try:
        crits = commons.paginate_and_sort_records(request.args, crits, Answer)
    except Exception as error:
        return jsonify(error=error.message)

    return jsonify(page=crits.page, totalpages=crits.pages, records=[item.to_dict() for item in crits.items])