from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.ext.associationproxy import association_proxy

from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

'''
ERRORS

Usage: flask [OPTIONS] COMMAND [ARGS]...
Try 'flask --help' for help.

Error: No such command 'db'.

- may not be in the right folder
- your pipenv shell may not be running
- or flask may not be installed
'''


'''
associaton_proxy('relationship to intermediary', 'relationship from intermediary to target')
'''

# create model cars
class Car(db.Model):
    # create table name cars
    __tablename__ = "cars"

    # create id, created_at, and updated_at columns
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # create column manufacturer
    manufacturer = db.Column(db.String)

    # create relationship to license
    licenses = db.relationship('License', back_populates='car')
    # create relationship to color
    colors_of_cur_car = association_proxy('licenses', 'color')

    def __repr__(self):
        return f'<Car manufacturer={self.manufacturer} id={self.id} />'

# create model colors
class Color(db.Model):
    # create tablename colors
    __tablename__ = "colors"

    # create id, created_at, and updated_at columns
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # create column color
    color = db.Column(db.String)

    # create relationship to license
    licenses = db.relationship('License', back_populates="color")
    # create relationship to car
    # associaton_proxy('relationship to intermediary', 'relationship from intermediary to target')
    # licenses refers to Color.licenses
    # car refers to License.car

    # Color.licenses -> License.car -> Car
    cars_with_cur_color = association_proxy('licenses', 'car')

    def __repr__(self):
        return f'<Color color={self.color} />'

# create model license
class License(db.Model):
    # create tablename licenses
    __tablename__ = "licenses"

    # create id, created_at, and updated_at columns
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    #create column license_plate
    license_plate = db.Column(db.String)
    # foreign key to color
    color_id = db.Column(db.Integer, db.ForeignKey('colors.id'))
    # foreign key to cars 
    car_id = db.Column(db.Integer, db.ForeignKey('cars.id'))


    # relationship between car and license
    car = db.relationship('Car', back_populates='licenses')
    # relationship between color and license
    color = db.relationship('Color', back_populates='licenses')

    def __repr__(self):
        return f'<License plate={self.license_plate} car={self.car_id} color={self.color_id}/>'


