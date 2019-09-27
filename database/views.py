# -*- coding: utf-8 -*-

from extensions import db, ModelView, Admin
from .models import Card, Archetype, MonsterCard, SpellCard, TrapCard, MonsterType, Set, Region, Country, Rarity, Ban, Banlist

class ModelViewAdministrator:

	def __init__(self, app):
		self.admin = Admin(app)
		self.init_app()

	def init_app(self):
		self.admin.add_view(ModelView(Card, db.session))
		self.admin.add_view(ModelView(Archetype, db.session))
		self.admin.add_view(ModelView(MonsterCard, db.session))
		self.admin.add_view(ModelView(SpellCard, db.session))
		self.admin.add_view(ModelView(TrapCard, db.session))
		self.admin.add_view(ModelView(MonsterType, db.session))
		self.admin.add_view(ModelView(Set, db.session))
		self.admin.add_view(ModelView(Region, db.session))
		self.admin.add_view(ModelView(Country, db.session))
		self.admin.add_view(ModelView(Rarity, db.session))
		self.admin.add_view(ModelView(Banlist, db.session))
		self.admin.add_view(ModelView(Ban, db.session))
