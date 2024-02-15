from init import db, ma
from marshmallow import fields

class Card(db.Model):
    __tablename__ = "cards" #this gives name to the table cards

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    date = db.Column(db.Date) # Date the card was created (not yet on our erd)
    status = db.Column(db.String)
    priority = db.Column(db.String)
    # fk 
    user_id =db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False) # id column of the users table in the erd and it is one and only one - or rather the id's class model name for __tablename__
    # fk is from postgress above

    # this below is a feature not of postgres but of sqlalchemy, which is why it is not used above
    # feature of orm sqlalchemy which deals with model name to exact info of user directly
    user = db.relationship('User', back_populates='cards')
    # {id: 1, title: Card 1, user_id: 2}
    # {
    #   id: 1,
    #   title: Card 1,
    #   user: {
    #       name: User 1,
    #       email: user1@email.com
    #   }
    # }

class CardSchema(ma.Schema):
    # this is from ma so we refer to schema
    user = fields.Nested('UserSchema', only = ['name', 'email'])

    class Meta:
        fields = ('id', 'title', 'description', 'date', 'status', 'priority', 'user')
        order = True

# we make this so later we can dump which is a part of ma to make into python obj so it can be read by flask and put data in proper way for application
card_schema = CardSchema()
cards_schema = CardSchema(many=True)