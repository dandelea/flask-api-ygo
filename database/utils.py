# -*- coding: utf-8 -*-

from flask_sqlalchemy import inspect

def object_as_dict(obj):
	return {c.key: getattr(obj, c.key) for c in inspect(obj).mapper.column_attrs}