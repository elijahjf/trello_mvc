from init import db, ma
from marshmallow import fields

# extending model class to create our own models here
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    # fk
    cards = db.relationship('Card', back_populates='user', cascade='all delete') # i think this means if user is del then del all their cards?

   # {id: 1, name: User 1, email: user1@email.com}
    # {
    #   id: 1,
    #   name: User 1,
    #   email: user1@email.com,
    #   cards: [
    #       {id: 1, title: Card 1},
    #       {id: 3, title: Card 3},
    #       {id: 7, title: Card 7}
    #   ]
    # }

class UserSchema(ma.Schema):

    cards = fields.List(fields.Nested('CardSchema', exclude['user'])
                       )
    class Meta:
        fields = ('id', 'name', 'email', 'password', 'is_admin')

user_schema = UserSchema(exclude=['password'])
users_schema = UserSchema(many=True, exclude=['password'])
    