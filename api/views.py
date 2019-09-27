# -*- coding: utf-8 -*-

from flask import abort, Blueprint, request, make_response, json, jsonify, Response

from extensions import db

from database import *

from .utils import model_by_tablename, columns_from_model, column_from_model, dict, get_paginated_list

api = Blueprint('api', __name__)

# FUNCTIONS

@api.route('/values', methods=['GET'])
def values():
	table = request.args.get('table')
	field = request.args.get('field')

	model = model_by_tablename(db, table)
	column = column_from_model(model, field)

	result = sorted([row[0] for row in db.session.query(column).distinct().all()], key=lambda x: (x is None, x))
	
	return Response(json.dumps(result), mimetype='application/json')

@api.route('/card', methods=['GET'])
def card():
	codepass = request.args.get('codepass')
	result = db.session.query(card_plus).filter_by(codepass=codepass).first_or_404()
	return Response(json.dumps(dict(result)), mimetype='application/json')

@api.route('/cards', methods=['POST'])
def cards():
	postdata = request.get_json()
	attributes = postdata.get('attributes')
	species = postdata.get('species')
	stars = postdata.get('stars')
	monster_types = postdata.get('monster_types')
	spell_families = postdata.get('spell_families')
	trap_families = postdata.get('trap_families')
	archetypes = postdata.get('archetypes')
	search = postdata.get('search')

	order = postdata.get('order') or 'name'
	if order not in columns_from_model(model_by_tablename(db, 'cards')):
		abort(404)
	
	if order == 'attack':
		order = db.cast(MonsterCard.attack, db.Integer)
	if order == 'defense':
		order = db.cast(MonsterCard.defense, db.Integer)

	inverse = postdata.get('inverse') if postdata.get('inverse')!=None else False

	
	filters = []
	if attributes:
		filters.append(MonsterCard.attribute.in_(attributes))
	if species:
		filters.append(MonsterCard.species.in_(species))
	if stars:
		filters.append(MonsterCard.stars.in_(stars))
	if monster_types:
		filters.append(MonsterCard.types.any(MonsterType.value.in_(monster_types)))
	if spell_families:
		filters.append(SpellCard.spell_family.in_(spell_families))
	if trap_families:
		filters.append(TrapCard.trap_family.in_(trap_families))
	if archetypes:
		filters.append(Card.archetypes.any(Archetype.value.in_(archetypes)))
	if search:
		filters.append(Card.name.like('%' + search + '%'))
	if inverse:
		order = db.desc(order)

	if len(filters):

		result = db.session.query(card_plus).filter(
				db.and_(
					*filters
				)
			).order_by(
				order
			).all()

	else:
		result = db.session.query(card_plus).all()

	response = get_paginated_list(
					result,
					'/api/cards',
					start=request.args.get('start', 1),
					limit=request.args.get('limit', 20)
				)

	return Response(json.dumps(response), mimetype='application/json')


	