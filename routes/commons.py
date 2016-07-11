from flask import jsonify, request
from routes import constants
import routes


def get_entities(classname):
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

    if 'orderby' in locals() and orderby in classname.__dict__:
        if 'order' in locals() and order in ['desc', 'asc']:
            orderby = orderby + " " + order
        crits = classname.query.order_by(routes.db.text(orderby)).paginate(page, pagelength, False)
    elif 'orderby' in locals() and orderby not in classname.__dict__:
        return jsonify(error="can't find the property to order the records by")
    else:
        crits = classname.query.paginate(page, pagelength, False)

    return jsonify(page=crits.page, totalpages=crits.pages, records=[item.to_dict() for item in crits.items])