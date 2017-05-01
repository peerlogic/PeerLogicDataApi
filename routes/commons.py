from flask import jsonify, request
from routes import constants
import routes
from datetime import datetime
from sqlalchemy.sql.expression import func
import json

def query_by_attrs(model, attrs):
    filter_args = []

    records = model.query

    for attr in attrs:
        str_len = False

        op = json.loads(attrs[attr])

        if attr.endswith('_len'):
            str_len = True
            attr = attr[:-4]
        #try:

        if 'gte' in  op.keys():
            if str_len:
                records = records.filter(func.length(getattr(model, attr)) >=op['gte'])
            else:
                records = records.filter(getattr(model, attr) >= op['gte'])
        if 'lte' in op.keys():
            if str_len:
                records = records.filter(func.length(getattr(model, attr)) <= op['lte'])
            else:
                records = records.filter(getattr(model, attr) <= op['lte'])
        if 'gt' in op.keys():
            if str_len:
                records = records.filter(func.length(getattr(model, attr)) > op['gt'])
            else:
               records = records.filter(getattr(model, attr) > op['gt'])
        if 'lt' in op.keys():
            if str_len:
               records = records.filter(func.length(getattr(model, attr)) < op['lt'])
            else:
               records = records.filter(getattr(model, attr) < op['lt'])
        if 'eq' in op.keys():
            if str_len:
                records = records.filter(func.length(getattr(model, attr)) == op['eq'])
            else:
                records = records.filter(getattr(model, attr) == op['eq'])
        if 'ne' in op.keys():
            if str_len:
                records = records.filter(func.length(getattr(model, attr)) <> op['ne'])
            else:
                records = records.filter(getattr(model, attr) <> op['ne'])
        #except:
        #    raise ValueError("gt, lt, gte, lte values must be in a json format e.g., {'lt':'5', 'gt':'3'}")

    return records



def get_all_records_paginated__sort(args, model):
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
        raise ValueError("page and pagelength must be numbers")

    if 'orderby' in locals() and orderby in model.__dict__:
        if 'order' in locals() and order in ['desc', 'asc']:
            orderby = orderby + " " + order
        records = model.query.order_by(routes.db.text(orderby)).paginate(page, pagelength, False)
    elif 'orderby' in locals() and orderby not in model.__dict__:
        attributes = [ v for v in model.__dict__.values() ]
        raise ValueError("can't find property '" + orderby + "' in " + attributes + " to order the records")
    else:
        records = model.query.paginate(page, pagelength, False)

    return jsonify(page=records.page, totalpages=records.pages, records=[item.to_dict() for item in records.items])

def paginate_and_sort_records(args, records, model):
    page = constants.DEFAULT_START_PAGE
    pagelength = constants.DEFAULT_PAGE_LENGTH

    try:
        if 'page' in args:
            page = int(args.get('page'))
        if 'pagelength' in args:
            pagelength = int(args.get('pagelength'))
        if 'orderby' in args:
            orderby = args.get('orderby')
        if 'order' in args:
            order = args.get('order')
    except:
        raise ValueError("page and pagelength must be integers")

    if 'orderby' in locals() and orderby in model.__dict__:
        if 'order' in locals() and order in ['desc', 'asc']:
            orderby = orderby + " " + order
        records = records.order_by(routes.db.text(orderby))
    elif 'orderby' in locals() and orderby not in model.__dict__:
        attributes = [ attr for attr in dir(model) if not attr.startswith('_')]
        raise ValueError("can't find property '" + orderby + "' in [" + ", ".join(attributes) + "] to order the records")

    records = records.paginate(page, pagelength, False)

    return records

def get_records_int_greater_or_less_than(args, model, attribute):
    try:
        if 'gte' in request.args:
            gte = int(request.args.get('gte'))
        if 'lte' in request.args:
            lte = int(request.args.get('lte'))
        if 'gt' in request.args:
            gt = int(request.args.get('gt'))
        if 'lt' in request.args:
            lt = int(request.args.get('lt'))
    except:
        raise ValueError("gt, lt, gte, lte values must be integers")

    if 'gte' in locals() and 'lte' in locals():
        records = model.query.filter(attribute >= gte, attribute <= lte)
    elif 'gt' in locals() and 'lte' in locals():
        records = model.query.filter(attribute > gt, attribute <= lte)
    elif 'gte' in locals() and 'lt' in locals():
        records = model.query.filter(attribute >= gte, attribute < lt)
    elif 'gt' in locals() and 'lt' in locals():
        records = model.query.filter(attribute > gt, attribute < lt)
    elif 'gte' in locals():
        records = model.query.filter(attribute >= gte)
    elif 'lte' in locals():
        records = model.query.filter(attribute <= lte)
    elif 'gt' in locals():
        records = model.query.filter(attribute > gt)
    elif 'lt' in locals():
        records = model.query.filter(attribute < lt)

    return records

def get_records_str_greater_or_less_than(args, model, attribute):
    try:
        if 'gte' in request.args:
            gte = request.args.get('gte')
        if 'lte' in request.args:
            lte = request.args.get('lte')
        if 'gt' in request.args:
            gt = request.args.get('gt')
        if 'lt' in request.args:
            lt = request.args.get('lt')
    except:
        raise ValueError("gt, lt, gte, lte values must be string")

    if 'gte' in locals() and 'lte' in locals():
        records = model.query.filter(attribute >= gte, attribute <= lte)
    elif 'gt' in locals() and 'lte' in locals():
        records = model.query.filter(attribute > gt, attribute <= lte)
    elif 'gte' in locals() and 'lt' in locals():
        records = model.query.filter(attribute >= gte, attribute < lt)
    elif 'gt' in locals() and 'lt' in locals():
        records = model.query.filter(attribute > gt, attribute < lt)
    elif 'gte' in locals():
        records = model.query.filter(attribute >= gte)
    elif 'lte' in locals():
        records = model.query.filter(attribute <= lte)
    elif 'gt' in locals():
        records = model.query.filter(attribute > gt)
    elif 'lt' in locals():
        records = model.query.filter(attribute < lt)

    return records

def get_records_len_str_greater_or_less_than(args, model, attribute):

    attr_pos = request.args.getlist('field_len').index(attribute)
    attr_op = request.args
    try:
        if 'gte' in request.args:
            gte = int(request.args.get('gte'))
        if 'lte' in request.args:
            lte = int(request.args.get('lte'))
        if 'gt' in request.args:
            gt = int(request.args.get('gt'))
        if 'lt' in request.args:
            lt = int(request.args.get('lt'))
    except:
        raise ValueError("gt, lt, gte, lte values must be integer")

    if 'gte' in locals() and 'lte' in locals():
        records = model.query.filter(func.length(attribute) >= gte, func.length(attribute) <= lte)
    elif 'gt' in locals() and 'lte' in locals():
        records = model.query.filter(func.length(attribute) > gt, func.length(attribute) <= lte)
    elif 'gte' in locals() and 'lt' in locals():
        records = model.query.filter(func.length(attribute) >= gte, func.length(attribute) < lt)
    elif 'gt' in locals() and 'lt' in locals():
        records = model.query.filter(func.length(attribute) > gt, func.length(attribute) < lt)
    elif 'gte' in locals():
        records = model.query.filter(func.length(attribute) >= gte)
    elif 'lte' in locals():
        records = model.query.filter(func.length(attribute) <= lte)
    elif 'gt' in locals():
        records = model.query.filter(func.length(attribute) > gt)
    elif 'lt' in locals():
        records = model.query.filter(func.length(attribute) < lt)

    return records

def get_records_datetime_greater_or_less_than(args, model, attribute):

    #follow ISO 8601 date notation
    try:
        if 'gte' in request.args:
            gte = datetime.strptime(request.args.get('gte'), '%Y-%m-%d %H:%M')
        if 'lte' in request.args:
            lte = datetime.strptime(request.args.get('lte'), '%Y-%m-%d %H:%M')
        if 'gt' in request.args:
            gt = datetime.strptime(request.args.get('gt'), '%Y-%m-%d %H:%M')
        if 'lt' in request.args:
            lt = datetime.strptime(request.args.get('lt'), '%Y-%m-%d %H:%M')
    except:
        raise ValueError("gt, lt, gte, lte values must be datetime with ISO 8601 format (YYYY-mm-dd HH:MM) ")

    if 'gte' in locals() and 'lte' in locals():
        records = model.query.filter(attribute >= gte, attribute <= lte)
    elif 'gt' in locals() and 'lte' in locals():
        records = model.query.filter(attribute > gt, attribute <= lte)
    elif 'gte' in locals() and 'lt' in locals():
        records = model.query.filter(attribute >= gte, attribute < lt)
    elif 'gt' in locals() and 'lt' in locals():
        records = model.query.filter(attribute > gt, attribute < lt)
    elif 'gte' in locals():
        records = model.query.filter(attribute >= gte)
    elif 'lte' in locals():
        records = model.query.filter(attribute <= lte)
    elif 'gt' in locals():
        records = model.query.filter(attribute > gt)
    elif 'lt' in locals():
        records = model.query.filter(attribute < lt)


    return records