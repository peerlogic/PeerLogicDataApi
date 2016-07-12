
from flask import jsonify, request, Blueprint
from model import *
from routes import constants
from routes import commons
import routes

artifact_api = Blueprint('artifact_api', __name__)

@artifact_api.route('/artifact')
def get_artifacts():
    return commons.get_entities(Artifact)

@artifact_api.route('/artifact/<id>')
def get_artifacts_by_id(id):
    crit = Artifact.query.get(id)
    return jsonify(artifact=crit.to_dict())

@artifact_api.route('/artifact/submitted_in_task_id/<task_id>')
def get_artifacts_by_submitted_in_task(task_id):
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

    crits = Artifact.query.filter_by(submitted_in_task_id=task_id)

    if 'orderby' in locals() and orderby in Artifact.__dict__:
        if 'order' in locals() and order in ['desc', 'asc']:
            orderby = orderby + " " + order
        crits = crits.order_by(routes.db.text(orderby))
    elif 'orderby' in locals() and orderby not in Artifact.__dict__:
        return jsonify(error="can't find the property to order the records")

    crits = crits.paginate(page, pagelength, False)

    return jsonify(page=crits.page, totalpages=crits.pages, records=[item.to_dict() for item in crits.items])


@artifact_api.route('/artifact/context_case/<context_case>')
def get_artifacts_by_context_case(context_case):
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

    crits = Artifact.query.filter(Artifact.context_case.ilike("%" + context_case + "%"))

    if 'orderby' in locals() and orderby in Artifact.__dict__:
        if 'order' in locals() and order in ['desc', 'asc']:
            orderby = orderby + " " + order
        crits = crits.order_by(routes.db.text(orderby))
    elif 'orderby' in locals() and orderby not in Artifact.__dict__:
        return jsonify(error="can't find the property to order the records")

    crits = crits.paginate(page, pagelength, False)

    return jsonify(page=crits.page, totalpages=crits.pages, records=[item.to_dict() for item in crits.items])

@artifact_api.route('/artifact/content/<content>')
def get_artifacts_by_content(content):
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

    crits = Artifact.query.filter(Artifact.content.ilike("%" + content + "%"))

    if 'orderby' in locals() and orderby in Artifact.__dict__:
        if 'order' in locals() and order in ['desc', 'asc']:
            orderby = orderby + " " + order
        crits = crits.order_by(routes.db.text(orderby))
    elif 'orderby' in locals() and orderby not in Artifact.__dict__:
        return jsonify(error="can't find the property to order the records")

    crits = crits.paginate(page, pagelength, False)

    return jsonify(page=crits.page, totalpages=crits.pages, records=[item.to_dict() for item in crits.items])

