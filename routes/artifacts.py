from flask import jsonify, request, Blueprint

from model import *
from routes import commons

artifact_api = Blueprint('artifact_api', __name__)


@artifact_api.route('/artifacts')
def get_artifacts():
    return commons.get_all_records_paginated__sort(request.args, Artifact)

@artifact_api.route('/artifacts/<id>')
def get_artifacts_by_id(id):
    artifacts = Artifact.query.get(id)
    return jsonify(artifact=artifacts.to_dict())

@artifact_api.route('/artifacts/submitted_in_task_id/<task_id>')
def get_artifacts_by_submitted_in_task(task_id):

    artifacts = Artifact.query.filter_by(submitted_in_task_id=task_id)
    try:
        artifacts = commons.paginate_and_sort_records(request.args, artifacts, Artifact)
    except Exception as error:
        return jsonify(error=error.message)

    return jsonify(page=artifacts.page, totalpages=artifacts.pages, records=[item.to_dict() for item in artifacts.items])


@artifact_api.route('/artifacts/context_case/<context_case>')
def get_artifacts_by_context_case(context_case):

    artifacts = Artifact.query.filter(Artifact.context_case.ilike("%" + context_case + "%"))
    try:
        artifacts = commons.paginate_and_sort_records(request.args, artifacts, Artifact)
    except Exception as error:
        return jsonify(error=error.message)

    return jsonify(page=artifacts.page, totalpages=artifacts.pages, records=[item.to_dict() for item in artifacts.items])

@artifact_api.route('/artifacts/content/<content>')
def get_artifacts_by_content(content):

    artifacts = Artifact.query.filter(Artifact.content.ilike("%" + content + "%"))
    try:
        artifacts = commons.paginate_and_sort_records(request.args, artifacts, Artifact)
    except Exception as error:
        return jsonify(error=error.message)

    return jsonify(page=artifacts.page, totalpages=artifacts.pages, records=[item.to_dict() for item in artifacts.items])

