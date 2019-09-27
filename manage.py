# -*- coding: utf-8 -*-

import flask
from flask_script import Server, Manager

from app import create_app
from extensions import db

manager = Manager(create_app)
manager.add_command("runserver", Server(host='0.0.0.0', port=5000))

if __name__ == "__main__":
	manager.run()