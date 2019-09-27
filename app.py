# -*- coding: utf-8 -*-

import logging
import os
from flask import Flask, request
from flask_cors import CORS

from api import *
from database import *

from logging.handlers import RotatingFileHandler

from extensions import (db, cache)

__all__ = ('create_app', )

BLUEPRINTS = (
    api,
)

def create_app(config=None, app_name='Yu-Gi-Oh! API', blueprints=None):

    app = Flask(app_name)

    app.config.from_pyfile('project.config', silent=True)

    if blueprints is None:
        blueprints = BLUEPRINTS

    initialize_api()
    blueprints_fabrics(app, blueprints)
    extensions_fabrics(app)
    configure_logging(app)
    CORS(app)

    return app


def blueprints_fabrics(app, blueprints):
    """Configure blueprints in views."""
    for blueprint in blueprints:
        app.register_blueprint(
            blueprint, url_prefix="/{0}".format(blueprint.name))


def extensions_fabrics(app):
    db.init_app(app)
    cache.init_app(app)
    admin = ModelViewAdministrator(app)


def initialize_api():
    pass


def configure_logging(app):
    """Configure file(info) logging."""

    if not app.config['LOG_ENABLED']:
        return

    # Set info level on logger, which might be overwritten by handers.
    # Suppress DEBUG messages.
    app.logger.setLevel(logging.DEBUG)

    info_log = os.path.join(app.config['LOG_FOLDER'], 'info.log')
    info_file_handler = RotatingFileHandler(
        info_log, maxBytes=1000000, backupCount=10)
    info_file_handler.setLevel(logging.INFO)
    info_file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]')
    )
    app.logger.addHandler(info_file_handler)

    # Testing
    # app.logger.info("Testing info.")
    # app.logger.warn("Testing warnings.")
    # app.logger.error("Testing errors.")