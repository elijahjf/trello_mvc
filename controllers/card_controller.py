from flask import Blueprint

from init import db
from models.card import Card, cards_schema

cards_bp =  Blueprint('cards', __name__, url_prefix='/cards')

# create route that will aloow us to fetch all cards in database
@cards_bp.route('/') # by just writing slash that means /cards bc of prefix
def get_all_cards():
    stmt = db.select(Card).order_by(Card.date.desc()) # desc is descending order
    cards = db.session.scalars(stmt)
    return cards_schema.dump(cards)