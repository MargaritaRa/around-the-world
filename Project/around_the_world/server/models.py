from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class User(db.Model, SerializerMixin):

    __tablename__ = 'users_table'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    _hashed_password = db.Column(db.String)

    countries = db.relationship('Countries', back_populates='user')
    favorites = db.relationship('Favorite', back_populates='user')

class Favorite(db.Model, SerializerMixin):

    __tablename__ = 'favorites_table'

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('users_table.id'))
    country_id = db.Column(db.Integer, db.ForeignKey('countries_table.id'))

    user = db.relationship('User', back_populates='favorites')
    country = db.relationship('Countries', back_populates='favorite')

class Countries(db.Model, SerializerMixin):

    __tablename__ = 'countries_table'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    contenent = db.Column(db.String)
    image = db.Column(db.String)
    currency = db.Column(db.String)
    language = db.Column(db.String)
    mannerism = db.Column(db.String)
    visa = db.Column(db.String)
    tipping = db.Column(db.String)
    when = db.Column(db.String)
    links = db.Column(db.String)

    user_id = db.Column(db.Integer, db.ForeignKey('users_table.id'))
    favorite_id = db.Column(db.Integer, db.ForeignKey('favorites_table.id'))

    user = db.relationship('User', back_populates='countries')
    favorite =  db.relationship('Favorite', back_populates='country')