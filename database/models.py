# -*- coding: utf-8 -*-
from extensions import db

from sqlalchemy.ext.hybrid import hybrid_property

cardsarchetypes = db.Table('cardsarchetypes',
	db.Column('card_id', db.Integer, db.ForeignKey('cards.id')),
	db.Column('archetype_id', db.Integer, db.ForeignKey('archetypes.id'))
)

class Card(db.Model):
	__tablename__ = 'cards'

	id = db.Column(db.Integer, primary_key=True)
	codepass = db.Column(db.String, nullable=False)
	name = db.Column(db.String, nullable=False)
	text = db.Column(db.String, nullable=False)
	illegal = db.Column(db.Boolean, nullable=False)
	has_name_condition = db.Column(db.Boolean, nullable=False)
	type = db.Column(db.Enum('monster', 'spell', 'trap'), nullable=False)
	
	rarities = db.relationship('Rarity', backref='cards', lazy=True)
	archetypes = db.relationship("Archetype", secondary=cardsarchetypes, back_populates="cards")

	__mapper_args__ = {'polymorphic_on': type}


class Archetype(db.Model):
	__tablename__ = 'archetypes'

	id = db.Column(db.Integer, primary_key=True)
	value = db.Column(db.String, unique=True, nullable=False)

	cards = db.relationship("Card", secondary=cardsarchetypes, back_populates="archetypes")

	def __init__ (self, value):
		self.value = value

	def __repr__(self):
		return self.value

monsterstypes = db.Table('monsterstypes',
	db.Column('monster_id', db.Integer, db.ForeignKey('cards.id')),
	db.Column('type_id', db.Integer, db.ForeignKey('monster_types.id'))
)

class MonsterCard(Card):
	__tablename__ = 'monsters'

	attack = db.Column(db.String(4))
	defense = db.Column(db.String(4))
	stars = db.Column(db.Integer)
	attribute = db.Column(db.Enum('dark', 'divine', 'earth', 'fire', 'light', 'water', 'wind', name='attribute'))
	species = db.Column(db.Enum('aqua', 'beast', 'beast-warrior', 'creator god', 'cyberse', 'dinosaur', 'divine-beast', 'dragon', 'fairy', 'fiend', 'fish', 'insect', 'machine', 'plant', 'psychic', 'pyro', 'reptile', 'rock', 'sea serpent', 'spellcaster', 'thunder', 'warrior', 'winged beast', 'wyrm', 'zombie'))

	types = db.relationship('MonsterType', secondary=monsterstypes, backref=db.backref('monsters', lazy='dynamic'))

	__mapper_args__ = {'polymorphic_identity': 'monster'}

	def __init__ (self, codepass, name, text, image, thumbnail, illegal, has_name_condition, attack, defense, stars, attribute, species):
		self.codepass = codepass
		self.name = name
		self.text = text
		self.image = image
		self.thumbnail = thumbnail
		self.illegal = illegal
		self.has_name_condition = has_name_condition
		self.attack = attack
		self.defense = defense
		self.stars = stars
		self.attribute = attribute
		self.species = species

class MonsterType(db.Model):
	__tablename__ = 'monster_types'

	id = db.Column(db.Integer, primary_key=True)
	value = db.Column(db.Enum('effect', 'flip', 'fusion', 'gemini', 'link', 'normal', 'pendulum', 'ritual', 'spirit', 'synchro', 'token', 'toon', 'tuner', 'union', 'xyz', name='monster_type'), unique=True, nullable=False)

	def __init__(self, value):
		self.value = value

	def __repr__(self):
		return self.value
	
class SpellCard(Card):
	__tablename__ = 'spells'

	spell_family = db.Column(db.Enum('continuous', 'quick-play', 'normal', 'equip', 'field', 'ritual', name='family'))

	__mapper_args__ = {'polymorphic_identity': 'spell'}

	def __init__ (self, codepass, name, text, image, thumbnail, illegal, has_name_condition, spell_family):
		self.codepass = codepass
		self.name = name
		self.text = text
		self.image = image
		self.thumbnail = thumbnail
		self.illegal = illegal
		self.has_name_condition = has_name_condition
		self.spell_family = spell_family
	
class TrapCard(Card):
	__tablename__ = 'traps'

	trap_family = db.Column(db.Enum('continuous', 'counter', 'normal', name='family'))

	__mapper_args__ = {'polymorphic_identity': 'trap'}

	def __init__(self, codepass, name, text, image, thumbnail, illegal, has_name_condition, trap_family):
		self.codepass = codepass
		self.name = name
		self.text = text
		self.image = image
		self.thumbnail = thumbnail
		self.illegal = illegal
		self.has_name_condition = has_name_condition
		self.trap_family = trap_family

setsregions = db.Table('setsregions',
	db.Column('set_id', db.Integer, db.ForeignKey('sets.id')),
	db.Column('region_id', db.Integer, db.ForeignKey('regions.id'))
)

class Set(db.Model):
	__tablename__ = 'sets'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, unique=True, nullable=False)
	type = db.Column(db.String, nullable=False)

	regions = db.relationship('Region', secondary=setsregions, backref=db.backref('sets'))
	countries = db.relationship('Country', backref='sets', lazy=True)

	def __init__(self, name, type):
		self.name = name
		self.type = type

	def __repr__(self):
		return self.name

class Region(db.Model):
	__tablename__ = 'regions'

	id = db.Column(db.Integer, primary_key=True)
	value = db.Column(db.String, unique=True, nullable=False)

	def __init__(self, value):
		self.value = value

	def __repr__(self):
		return self.value

countriesrarities = db.Table('countriesrarities',
	db.Column('country_id', db.Integer, db.ForeignKey('countries.id')),
	db.Column('rarity_id', db.Integer, db.ForeignKey('rarities.id'))
)

class Country(db.Model):
	__tablename__ = 'countries'

	id = db.Column(db.Integer, primary_key=True)
	language = db.Column(db.String, nullable=False)
	date = db.Column(db.Date, nullable=False)

	set_id = db.Column(db.Integer, db.ForeignKey('sets.id'), nullable=False)
	rarities = db.relationship('Rarity', secondary=countriesrarities, backref=db.backref('countriess'))

	def __init__(self, language, date):
		self.language = language
		self.date = date

	def __repr__(self):
		return self.language

class Rarity(db.Model):
	__tablename__ = 'rarities'

	id = db.Column(db.Integer, primary_key=True)
	rarity = db.Column(db.String, nullable=False)
	code = db.Column(db.String, nullable=False)
	
	card_id = db.Column(db.Integer, db.ForeignKey('cards.id'), nullable=False)
	countries = db.relationship('Country', secondary=countriesrarities, backref=db.backref('raritiess'))

	__table_args__ = (db.UniqueConstraint('rarity', 'code'),)

	def __init__(self, rarity, code, card_id):
		self.rarity = rarity
		self.code = code
		self.card_id = card_id

	def __repr__(self):
		return self.code

class Banlist(db.Model):
	__tablename__ = 'banlists'

	id = db.Column(db.Integer, primary_key=True)
	start_date = db.Column(db.Date, nullable=False)
	end_date = db.Column(db.Date)
	game_type = db.Column(db.Enum('Advanced', 'Traditional', name='game_type'))
	region = db.Column(db.Enum('TCG', 'OCG', name='region'), nullable=False)

	bans = db.relationship('Ban', backref='banlist')

	__table_args__ = (db.UniqueConstraint('start_date', 'game_type', 'region'),)

	def __init__ (self, start_date, end_date, game_type, region):
		self.start_date = start_date
		self.end_date = end_date
		self.game_type = game_type
		self.region = region

	def __repr__(self):
		return "<Banlist {0} / {1} - {2} - {3}>".format(self.start_date, self.end_date, self.game_type, self.region) 

class Ban(db.Model):
	__tablename__ = 'bans'

	id = db.Column(db.Integer, primary_key=True)
	status = db.Column(db.String, nullable=False)

	card_id = db.Column(db.Integer, db.ForeignKey('cards.id'), nullable=False)
	banlist_id = db.Column(db.Integer, db.ForeignKey('banlists.id'), nullable=False)

	def __init__ (self, status, card_id):
		self.status = status
		self.card_id = card_id

card_plus = db.with_polymorphic(Card, [MonsterCard, SpellCard, TrapCard])
