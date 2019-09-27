from flask import abort, jsonify, json

def model_by_tablename(db, tablename):
    str_to_model = {}
    for model in db.Model._decl_class_registry.values():
        if hasattr(model, '__tablename__'):
            str_to_model[model.__tablename__] = model

    return str_to_model[tablename]


def columns_from_model(model):
    return [column.key for column in model.__table__.columns]


def column_from_model(model, fieldname):
    result = None
    for column in model.__table__.columns:
        if column.key == fieldname:
            result = column
    return result


def dict(row):
    from sqlalchemy.orm.attributes import instance_dict
    result = instance_dict(row)
    if '_sa_instance_state' in result:
        del result['_sa_instance_state']
    return result


def get_paginated_list(query_result, url, start, limit):
    # check if page exists
    count = len(query_result)
    if (count < start):
        abort(404)
    # make response
    obj = {}
    obj['start'] = start
    obj['limit'] = limit
    obj['count'] = count
    # make URLs
    # make previous url
    if start == 1:
        obj['previous'] = ''
    else:
        start_copy = max(1, start - limit)
        limit_copy = start - 1
        obj['previous'] = url + '?start=%d&limit=%d' % (start_copy, limit_copy)
    # make next url
    if start + limit > count:
        obj['next'] = ''
    else:
        start_copy = start + limit
        obj['next'] = url + '?start=%d&limit=%d' % (start_copy, limit)
	
    obj['data'] = query_result[(start - 1):(start - 1 + limit)]
    obj['data'] = [dict(r) for r in obj['data']]
    return obj
