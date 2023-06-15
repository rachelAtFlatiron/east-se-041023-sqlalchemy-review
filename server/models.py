from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

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
- Error: cursor.execute(statement, parameters) sqlite3.OperationalError: no such table: plants

> flask db init (creates migrations and instance folders)
> flask db migrate/revision (creates alembic file and app.db with instructions on how to create db with SQL)
> flask db upgrade (runs alembic file and creates our additional db tables)
> python seed.py
'''

'''
Error: exc.InvalidRequestError: When initializing mapper Mapper[Color(colors)], expression 'Licenses' failed to locate a name ('Licenses'). If this is a class name, consider adding this relationship() to the <class 'models.Color'> class after both dependent classes have been defined.

- double check relationship class names and any spelling errors for class names or back_populates, etc.
'''

'''
Error: TypeError: 'color' is an invalid keyword argument for License
- because my relationship in License was 'colors' and not 'color' which is what the seed.py wanted
'''

'''
Error: AttributeError: Color object has no attribute

- double check tuple has comma at the end (for serialize_rules)
'''

# create model cars
class Car(db.Model, SerializerMixin):
    # create table name cars
    __tablename__ = "cars"

    # create id, created_at, and updated_at columns
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # create column manufacturer
    manufacturer = db.Column(db.String)

    # create relationship to license
    car_licenses = db.relationship('License', back_populates='car')
    # create relationship to color
    '''
    associaton_proxy('relationship to intermediary', 'relationship from intermediary to target')
    '''
    colors_of_cur_car = association_proxy('car_licenses', 'color')

    #serialize_rule to prevent max recursion
    # -relationship_that_exists_in_current_model.bidirectional_relationship_in_associated_model
    serialize_rules = ('-car_licenses.car', '-colors_of_cur_car.cars_with_cur_color')

    def __repr__(self):
        return f'<Car manufacturer={self.manufacturer} id={self.id} />'


# create model colors
class Color(db.Model, SerializerMixin):
    # create tablename colors
    __tablename__ = "colors"

    # create id, created_at, and updated_at columns
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # create column color
    color = db.Column(db.String)

    # create relationship to license
    color_licenses = db.relationship('License', back_populates="color")
    # create relationship to car
    # associaton_proxy('relationship to intermediary', 'relationship from intermediary to target')
    # licenses refers to Color.licenses
    # car refers to License.car

    # Color.licenses -> License.car -> Car
    cars_with_cur_color = association_proxy('color_licenses', 'car')

    serialize_rules = ('-color_licenses.color', '-cars_with_cur_color.colors_of_cur_car')

    def __repr__(self):
        return f'<Color color={self.color} />'

# create model license
class License(db.Model, SerializerMixin):
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
    car = db.relationship('Car', back_populates='car_licenses')
    # relationship between color and license
    color = db.relationship('Color', back_populates='color_licenses')

    serialize_rules = ('-car.car_licenses', '-color.color_licenses')

    def __repr__(self):
        return f'<License plate={self.license_plate} car={self.car_id} color={self.color_id}/>'


