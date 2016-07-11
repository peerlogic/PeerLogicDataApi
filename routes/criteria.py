

from flask import jsonify, request, Blueprint
from model import *
from routes import constants
from routes import commons
import routes

criteria_api = Blueprint('criteria_api', __name__)

@criteria_api.route('/criterion')
def get_criteria():
    return commons.get_entities(Criterion)

@criteria_api.route('/criterion/<id>')
def get_criteria_by_id(id):
    crit = Criterion.query.get(id)
    return jsonify(artifact=crit.to_dict())

@criteria_api.route('/criterion/title/<title>')
def get_criteria_by_title(title):
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

    crits = Criterion.query.filter(Criterion.title.ilike("%" + title + "%"))

    if 'orderby' in locals() and orderby in Criterion.__dict__:
        if 'order' in locals() and order in ['desc', 'asc']:
            orderby = orderby + " " + order
        crits = crits.order_by(routes.db.text(orderby))
    elif 'orderby' in locals() and orderby not in Criterion.__dict__:
        return jsonify(error="can't find the property to order the records")

    crits = crits.paginate(page, pagelength, False)

    return jsonify(page=crits.page, totalpages=crits.pages, records=[item.to_dict() for item in crits.items])

@criteria_api.route('/criterion/description/<desc>')
def get_criteria_by_desc(desc):
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

    crits = Criterion.query.filter(Criterion.description.ilike("%" + desc + "%"))

    if 'orderby' in locals() and orderby in Criterion.__dict__:
        if 'order' in locals() and order in ['desc', 'asc']:
            orderby = orderby + " " + order
        crits = crits.order_by(routes.db.text(orderby))
    elif 'orderby' in locals() and orderby not in Criterion.__dict__:
        return jsonify(error="can't find the property to order the records")

    crits = crits.paginate(page, pagelength, False)

    return jsonify(page=crits.page, totalpages=crits.pages, records=[item.to_dict() for item in crits.items])

@criteria_api.route('/criterion/type/<type>')
def get_criteria_by_type(type):
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

    crits = Criterion.query.filter(Criterion.type.ilike("%" + type + "%"))

    if 'orderby' in locals() and orderby in Criterion.__dict__:
        if 'order' in locals() and order in ['desc', 'asc']:
            orderby = orderby + " " + order
        crits = crits.order_by(routes.db.text(orderby))
    elif 'orderby' in locals() and orderby not in Criterion.__dict__:
        return jsonify(error="can't find the property to order the records")

    crits = crits.paginate(page, pagelength, False)

    return jsonify(page=crits.page, totalpages=crits.pages, records=[item.to_dict() for item in crits.items])

@criteria_api.route('/criterion/minscore/<minscore>/maxscore/<maxscore>')
def get_criteria_by_score(minscore, maxscore):
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

    crits = Criterion.query.filter_by(min_score = minscore, max_score = maxscore)

    if 'orderby' in locals() and orderby in Criterion.__dict__:
        if 'order' in locals() and order in ['desc', 'asc']:
            orderby = orderby + " " + order
        crits = crits.order_by(routes.db.text(orderby))
    elif 'orderby' in locals() and orderby not in Criterion.__dict__:
        return jsonify(error="can't find the property to order the records")

    crits = crits.paginate(page, pagelength, False)

    return jsonify(page=crits.page, totalpages=crits.pages, records=[item.to_dict() for item in crits.items])

@criteria_api.route('/criterion/weight/<weight>')
def get_criteria_by_weight(weight):
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

    crits = Criterion.query.filter_by(weight = weight)

    if 'orderby' in locals() and orderby in Criterion.__dict__:
        if 'order' in locals() and order in ['desc', 'asc']:
            orderby = orderby + " " + order
        crits = crits.order_by(routes.db.text(orderby))
    elif 'orderby' in locals() and orderby not in Criterion.__dict__:
        return jsonify(error="can't find the property to order the records")

    crits = crits.paginate(page, pagelength, False)

    return jsonify(page=crits.page, totalpages=crits.pages, records=[item.to_dict() for item in crits.items])

