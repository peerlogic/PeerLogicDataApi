from flask import jsonify, request, Blueprint

from model import *
from routes import commons

eval_mode_api = Blueprint('eval_mode_api', __name__)


@eval_mode_api.route('/eval_mode')
def get_eval_mode():
    return commons.get_all_records_paginated__sort(request.args, EvalMode)

@eval_mode_api.route('/eval_mode/<id>')
def get_eval_mode_by_id(id):
    evalmodes = EvalMode.query.get(int(id))
    return jsonify(evalmodes=evalmodes.to_dict())