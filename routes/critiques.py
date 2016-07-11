
from flask import jsonify, request, Blueprint
from model import *
from routes import constants
from routes import commons
import routes

crit_api = Blueprint('crit_api', __name__)

############################### critiques ####################################
@crit_api.route('/critiques')
def get_critiques():
    return commons.get_entities(Answer)

@crit_api.route('/critiques/score')
def get_critique_by_score():
    page = constants.DEFAULT_START_PAGE
    pagelength = constants.DEFAULT_PAGE_LENGTH

    try:
        if 'gte' in request.args:
            gte = int(request.args.get('gte'))
        if 'lte' in request.args:
            lte = int(request.args.get('lte'))
        if 'gt' in request.args:
            gt = int(request.args.get('gt'))
        if 'lt' in request.args:
            lt = int(request.args.get('lt'))
        if 'orderby' in request.args:
            orderby = request.args.get('orderby')
        if 'order' in request.args:
            order = request.args.get('order')
        if 'page' in request.args:
            page = int(request.args.get('page'))
        if 'pagelength' in request.args:
            pagelength = int(request.args.get('pagelength'))
    except:
        return jsonify(error="page and pagelength must be numbers")

    if 'gte' in locals() and 'lte' in locals():
        crits = Answer.query.filter(Answer.score >= gte, Answer.score <= lte)
    elif 'gt' in locals() and 'lte' in locals():
        crits = Answer.query.filter(Answer.score > gt, Answer.score <= lte)
    elif 'gte' in locals() and 'lt' in locals():
        crits = Answer.query.filter(Answer.score >= gte, Answer.score < lt)
    elif 'gt' in locals() and 'lt' in locals():
        crits = Answer.query.filter(Answer.score > gt, Answer.score < lt)


    if 'orderby' in locals() and orderby in Answer.__dict__:
        if 'order' in locals() and order in ['desc', 'asc']:
            orderby = orderby + " " + order
        crits = crits.order_by(routes.db.text(orderby))
    elif 'orderby' in locals() and orderby not in Answer.__dict__:
        return jsonify(error="can't find the property to order the records")

    crits = crits.paginate(page, pagelength, False)

    return jsonify(page=crits.page, totalpages=crits.pages, records=[item.to_dict() for item in crits.items])

@crit_api.route('/critiques/<crit_id>')
def get_critique_by_id(crit_id):
    crit = Answer.query.get(crit_id)
    return jsonify(critique=crit.to_dict())

@crit_api.route('/critiques/evaluation_mode_id/<eval_mode>')
def get_critique_by_eval_mode(eval_mode):
    page = constants.DEFAULT_START_PAGE
    pagelength = constants.DEFAULT_PAGE_LENGTH

    try:
        if 'page' in request.args:
            page = int(request.args.get('page'))
        if 'pagelength' in request.args:
            pagelength = int(request.args.get('pagelength'))
    except:
        return jsonify(error="page and pagelength must be numbers")

    crits = Answer.query.filter_by(evaluation_mode_id=eval_mode).paginate(page, pagelength, False)

    return jsonify(page=crits.page, totalpages=crits.pages, records=[item.to_dict() for item in crits.items])

@crit_api.route('/critiques/artifact_id/<artifact_id>')
def get_critique_by_artifact_id(artifact_id):
    crits = Answer.query.filter_by(assessee_artifact_id=artifact_id).all()
    return jsonify(records=[item.to_dict() for item in crits])


@crit_api.route('/critiques/create_in_task_id')
def get_critique_by_create_in_task_id_range():

    page = constants.DEFAULT_START_PAGE
    pagelength = constants.DEFAULT_PAGE_LENGTH

    try:
        if 'gte' in request.args:
            gte = request.args.get('gte')
        if 'lte' in request.args:
            lte = request.args.get('lte')
        if 'gt' in request.args:
            gt = request.args.get('gt')
        if 'lt' in request.args:
            lt = request.args.get('lt')
        if 'orderby' in request.args:
            orderby = request.args.get('orderby')
        if 'order' in request.args:
            order = request.args.get('order')
        if 'page' in request.args:
            page = int(request.args.get('page'))
        if 'pagelength' in request.args:
            pagelength = int(request.args.get('pagelength'))
    except:
        return jsonify(error="page and pagelength must be numbers")

    if 'gte' in locals() and 'lte' in locals():
        crits = Answer.query.filter(Answer.create_in_task_id >= gte, Answer.create_in_task_id <= lte)
    elif 'gt' in locals() and 'lte' in locals():
        crits = Answer.query.filter(Answer.create_in_task_id > gt, Answer.create_in_task_id <= lte)
    elif 'gte' in locals() and 'lt' in locals():
        crits = Answer.query.filter(Answer.create_in_task_id >= gte, Answer.create_in_task_id < lt)
    elif 'gt' in locals() and 'lt' in locals():
        crits = Answer.query.filter(Answer.create_in_task_id > gt, Answer.create_in_task_id < lt)


    if 'orderby' in locals() and orderby in Answer.__dict__:
        if 'order' in locals() and order in ['desc', 'asc']:
            orderby = orderby + " " + order
        crits = crits.order_by(routes.db.text(orderby))
    elif 'orderby' in locals() and orderby not in Answer.__dict__:
        return jsonify(error="can't find the property to order the records")

    crits = crits.paginate(page, pagelength, False)

    return jsonify(page=crits.page, totalpages=crits.pages, records=[item.to_dict() for item in crits.items])

@crit_api.route('/critiques/create_in_task_id/<task_id>')
def get_critique_by_create_in_task_id(task_id):

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

    crits = Answer.query.filter_by(create_in_task_id=task_id)\

    if 'orderby' in locals() and orderby in Answer.__dict__:
        if 'order' in locals() and order in ['desc', 'asc']:
            orderby = orderby + " " + order
        crits = crits.order_by(routes.db.text(orderby))
    elif 'orderby' in locals() and orderby not in Answer.__dict__:
        return jsonify(error="can't find the property to order the records")

    crits = crits.paginate(page, pagelength, False)

    return jsonify(page=crits.page, totalpages=crits.pages, records=[item.to_dict() for item in crits.items])

@crit_api.route('/critiques/create_in_task_id/<task_id>/assessor_id/<assessor_id>')
def get_critique_by_create_in_task_id_and_assessor_id(task_id, assessor_id):

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

    crits = Answer.query.filter_by(create_in_task_id=task_id, assessor_actor_id=assessor_id)

    if 'orderby' in locals() and orderby in Answer.__dict__:
        if 'order' in locals() and order in ['desc', 'asc']:
            orderby = orderby + " " + order
        crits = crits.order_by(routes.db.text(orderby))
    elif 'orderby' in locals() and orderby not in Answer.__dict__:
        return jsonify(error="can't find the property to order the records")

    crits = crits.paginate(page, pagelength, False)

    return jsonify(page=crits.page, totalpages=crits.pages, records=[item.to_dict() for item in crits.items])

@crit_api.route('/critiques/create_in_task_id/<task_id>/assessee_id/<assessee_id>')
def get_critique_by_create_in_task_id_and_assessee_id(task_id, assessee_id):

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

    crits = Answer.query.filter_by(create_in_task_id=task_id, assessee_actor_id=assessee_id)

    if 'orderby' in locals() and orderby in Answer.__dict__:
        if 'order' in locals() and order in ['desc', 'asc']:
            orderby = orderby + " " + order
        crits = crits.order_by(routes.db.text(orderby))
    elif 'orderby' in locals() and orderby not in Answer.__dict__:
        return jsonify(error="can't find the property to order the records")

    crits = crits.paginate(page, pagelength, False)

    return jsonify(page=crits.page, totalpages=crits.pages, records=[item.to_dict() for item in crits.items])

@crit_api.route('/critiques/assessor_id/<assessor_id>/assessee_id/<assessee_id>')
def get_critiques_by_assessor_id_and_assessee_id(assessor_id, assessee_id):

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

    crits = Answer.query.filter_by(create_in_task_id=assessor_id, assessee_actor_id=assessee_id)

    if 'orderby' in locals() and orderby in Answer.__dict__:
        if 'order' in locals() and order in ['desc', 'asc']:
            orderby = orderby + " " + order
        crits = crits.order_by(routes.db.text(orderby))
    elif 'orderby' in locals() and orderby not in Answer.__dict__:
        return jsonify(error="can't find the property to order the records")

    crits = crits.paginate(page, pagelength, False)

    return jsonify(page=crits.page, totalpages=crits.pages, records=[item.to_dict() for item in crits.items])

