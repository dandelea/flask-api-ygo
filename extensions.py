# -*- coding: utf-8 -*-

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from flask_caching import Cache
cache = Cache()

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView