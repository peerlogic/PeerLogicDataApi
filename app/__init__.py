import json

from flask import Flask, jsonify, request
from flask.ext.sqlalchemy import SQLAlchemy
from model import *

app = Flask(__name__)

#Include config from config.py
app.config.from_object('config')


#Create an instance of SQLAclhemy
db = SQLAlchemy(app)

DEFAULT_PAGE_LENGTH = 50
DEFAULT_START_PAGE = 1

def get_entities(classname):
    page = DEFAULT_START_PAGE
    pagelength = DEFAULT_PAGE_LENGTH

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

    if 'orderby' in locals() and orderby in classname.__dict__:
        if 'order' in locals() and order in ['desc', 'asc']:
            orderby = orderby + " " + order
        crits = classname.query.order_by(db.text(orderby)).paginate(page, pagelength, False)
    elif 'orderby' in locals() and orderby not in classname.__dict__:
        return jsonify(error="can't find the property to order the records by")
    else:
        crits = classname.query.paginate(page, pagelength, False)

    return jsonify(page=crits.page, totalpages=crits.pages, records=[item.to_dict() for item in crits.items])

############################### critiques ####################################
@app.route('/critiques')
def get_critiques():
    return get_entities(Answer)

@app.route('/critiques/score')
def get_critique_by_score():
    page = DEFAULT_START_PAGE
    pagelength = DEFAULT_PAGE_LENGTH

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
        crits = crits.order_by(db.text(orderby))
    elif 'orderby' in locals() and orderby not in Answer.__dict__:
        return jsonify(error="can't find the property to order the records")

    crits = crits.paginate(page, pagelength, False)

    return jsonify(page=crits.page, totalpages=crits.pages, critiques=[item.to_dict() for item in crits.items])

@app.route('/critiques/<crit_id>')
def get_critique_by_id(crit_id):
    crit = Answer.query.get(crit_id)
    return jsonify(critique=crit.to_dict())

@app.route('/critiques/evaluation_mode_id/<eval_mode>')
def get_critique_by_eval_mode(eval_mode):
    page = DEFAULT_START_PAGE
    pagelength = DEFAULT_PAGE_LENGTH

    try:
        if 'page' in request.args:
            page = int(request.args.get('page'))
        if 'pagelength' in request.args:
            pagelength = int(request.args.get('pagelength'))
    except:
        return jsonify(error="page and pagelength must be numbers")

    crits = Answer.query.filter_by(evaluation_mode_id=eval_mode).paginate(page, pagelength, False)

    return jsonify(page=crits.page, totalpages=crits.pages, critiques=[item.to_dict() for item in crits.items])

@app.route('/critiques/artifact_id/<artifact_id>')
def get_critique_by_artifact_id(artifact_id):
    crits = Answer.query.filter_by(assessee_artifact_id=artifact_id).all()
    return jsonify(critiques=[item.to_dict() for item in crits])


@app.route('/critiques/create_in_task_id')
def get_critique_by_create_in_task_id_range():

    page = DEFAULT_START_PAGE
    pagelength = DEFAULT_PAGE_LENGTH

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
        crits = crits.order_by(db.text(orderby))
    elif 'orderby' in locals() and orderby not in Answer.__dict__:
        return jsonify(error="can't find the property to order the records")

    crits = crits.paginate(page, pagelength, False)

    return jsonify(page=crits.page, totalpages=crits.pages, critiques=[item.to_dict() for item in crits.items])

@app.route('/critiques/create_in_task_id/<task_id>')
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
        crits = crits.order_by(db.text(orderby))
    elif 'orderby' in locals() and orderby not in Answer.__dict__:
        return jsonify(error="can't find the property to order the records")

    crits = crits.paginate(page, pagelength, False)

    return jsonify(page=crits.page, totalpages=crits.pages, critiques=[item.to_dict() for item in crits.items])

@app.route('/critiques/create_in_task_id/<task_id>/assessor_id/<assessor_id>')
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
        crits = crits.order_by(db.text(orderby))
    elif 'orderby' in locals() and orderby not in Answer.__dict__:
        return jsonify(error="can't find the property to order the records")

    crits = crits.paginate(page, pagelength, False)

    return jsonify(page=crits.page, totalpages=crits.pages, critiques=[item.to_dict() for item in crits.items])

@app.route('/critiques/create_in_task_id/<task_id>/assessee_id/<assessee_id>')
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
        crits = crits.order_by(db.text(orderby))
    elif 'orderby' in locals() and orderby not in Answer.__dict__:
        return jsonify(error="can't find the property to order the records")

    crits = crits.paginate(page, pagelength, False)

    return jsonify(page=crits.page, totalpages=crits.pages, critiques=[item.to_dict() for item in crits.items])

@app.route('/critiques/assessor_id/<assessor_id>/assessee_id/<assessee_id>')
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
        crits = crits.order_by(db.text(orderby))
    elif 'orderby' in locals() and orderby not in Answer.__dict__:
        return jsonify(error="can't find the property to order the records")

    crits = crits.paginate(page, pagelength, False)

    return jsonify(page=crits.page, totalpages=crits.pages, critiques=[item.to_dict() for item in crits.items])

############################### ARTIFACT ####################################
@app.route('/artifact')
def get_artifacts():
    return get_entities(Artifact)

@app.route('/artifact/<id>')
def get_artifacts_by_id(id):
    crit = Artifact.query.get(id)
    return jsonify(artifact=crit.to_dict())

@app.route('/artifact/submitted_in_task_id/<task_id>')
def get_artifacts_by_submitted_in_task(task_id):
    page = DEFAULT_START_PAGE
    pagelength = DEFAULT_PAGE_LENGTH

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

    crits = Artifact.query.filter_by(submitted_in_task_id=task_id)

    if 'orderby' in locals() and orderby in Answer.__dict__:
        if 'order' in locals() and order in ['desc', 'asc']:
            orderby = orderby + " " + order
        crits = crits.order_by(db.text(orderby))
    elif 'orderby' in locals() and orderby not in Answer.__dict__:
        return jsonify(error="can't find the property to order the records")

    crits = crits.paginate(page, pagelength, False)

    return jsonify(page=crits.page, totalpages=crits.pages, records=[item.to_dict() for item in crits.items])


@app.route('/artifact/context_case/<context_case>')
def get_artifacts_by_context_case(context_case):
    page = DEFAULT_START_PAGE
    pagelength = DEFAULT_PAGE_LENGTH

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

    crits = Artifact.query.filter(Artifact.context_case.ilike("%" + context_case + "%"))

    if 'orderby' in locals() and orderby in Answer.__dict__:
        if 'order' in locals() and order in ['desc', 'asc']:
            orderby = orderby + " " + order
        crits = crits.order_by(db.text(orderby))
    elif 'orderby' in locals() and orderby not in Answer.__dict__:
        return jsonify(error="can't find the property to order the records")

    crits = crits.paginate(page, pagelength, False)

    return jsonify(page=crits.page, totalpages=crits.pages, records=[item.to_dict() for item in crits.items])

@app.route('/artifact/content/<content>')
def get_artifacts_by_content(content):
    page = DEFAULT_START_PAGE
    pagelength = DEFAULT_PAGE_LENGTH

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

    crits = Artifact.query.filter(Artifact.content.ilike("%" + content + "%"))

    if 'orderby' in locals() and orderby in Answer.__dict__:
        if 'order' in locals() and order in ['desc', 'asc']:
            orderby = orderby + " " + order
        crits = crits.order_by(db.text(orderby))
    elif 'orderby' in locals() and orderby not in Answer.__dict__:
        return jsonify(error="can't find the property to order the records")

    crits = crits.paginate(page, pagelength, False)

    return jsonify(page=crits.page, totalpages=crits.pages, records=[item.to_dict() for item in crits.items])


############################### critiques ####################################



if __name__ == '__main__':
    app.run()




