from flask import jsonify, request, Blueprint

from model import *
from routes import commons

criteria_api = Blueprint('criteria_api', __name__)

@criteria_api.route('/criteria')
def get_criteria():
    return commons.get_all_records_paginated__sort(request.args, Criterion)

@criteria_api.route('/criteria/<id>')
def get_criteria_by_id(id):
    crit = Criterion.query.get(id)
    return jsonify(artifact=crit.to_dict())

@criteria_api.route('/criteria/title/<title>')
def get_criteria_by_title(title):

    crits = Criterion.query.filter(Criterion.title.ilike("%" + title + "%"))

    try:
        crits = commons.paginate_and_sort_records(request.args, crits, Criterion)
    except Exception as error:
        return jsonify(error=error.message)

    return jsonify(page=crits.page, totalpages=crits.pages, records=[item.to_dict() for item in crits.items])

@criteria_api.route('/criteria/description/<desc>')
def get_criteria_by_desc(desc):
    crits = Criterion.query.filter(Criterion.description.ilike("%" + desc + "%"))

    try:
        crits = commons.paginate_and_sort_records(request.args, crits, Criterion)
    except Exception as error:
        return jsonify(error=error.message)

    return jsonify(page=crits.page, totalpages=crits.pages, records=[item.to_dict() for item in crits.items])

@criteria_api.route('/criteria/type/<type>')
def get_criteria_by_type(type):

    crits = Criterion.query.filter(Criterion.type.ilike("%" + type + "%"))

    try:
        crits = commons.paginate_and_sort_records(request.args, crits, Criterion)
    except Exception as error:
        return jsonify(error=error.message)

    return jsonify(page=crits.page, totalpages=crits.pages, records=[item.to_dict() for item in crits.items])

@criteria_api.route('/criteria/minscore/<minscore>/maxscore/<maxscore>')
def get_criteria_by_score(minscore, maxscore):

    crits = Criterion.query.filter_by(min_score = minscore, max_score = maxscore)

    try:
        crits = commons.paginate_and_sort_records(request.args, crits, Criterion)
    except Exception as error:
        return jsonify(error=error.message)

    return jsonify(page=crits.page, totalpages=crits.pages, records=[item.to_dict() for item in crits.items])

@criteria_api.route('/criteria/weight/<weight>')
def get_criteria_by_weight(weight):

    crits = Criterion.query.filter_by(weight = weight)

    try:
        crits = commons.paginate_and_sort_records(request.args, crits, Criterion)
    except Exception as error:
        return jsonify(error=error.message)

    return jsonify(page=crits.page, totalpages=crits.pages, records=[item.to_dict() for item in crits.items])

