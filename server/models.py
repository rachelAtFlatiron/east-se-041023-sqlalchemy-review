from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.ext.associationproxy import association_proxy

from sqlalchemy_serializer import SerializerMixin


db = SQLAlchemy()

class Car(db.Model, SerializerMixin):
    __tablename__ = "cars"

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    company = db.Column(db.String)
    license = db.relationship('License', back_populates='car')



class Color(db.Model, SerializerMixin):
    __tablename__ = "colors"

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    color = db.Column(db.String)
    license = db.relationship('License', back_populates='color')
    

class License(db.Model, SerializerMixin):
    __tablename__ = "licenses"

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    license_plate = db.Column(db.String)
    color_id = db.Column(db.Integer, db.ForeignKey('colors.id'))
    color = db.relationship('Color', back_populates='license')
    car_id = db.Column(db.Integer, db.ForeignKey('cars.id'))
    car = db.relationship('Car', back_populates='license')


