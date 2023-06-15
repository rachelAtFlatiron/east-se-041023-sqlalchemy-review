from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.ext.associationproxy import association_proxy

from sqlalchemy_serializer import SerializerMixin

# create model cars

    # create table name cars

    # create id, created_at, and updated_at columns

    # create column company
    # create relationship to license
    # create relationship to color



# create model colors

    # create tablename colors

    # create id, created_at, and updated_at columns

    # create column color
    # create relationship to license
    # create relationship to car

# create model license

    # create tablename licenses

    # create id, created_at, and updated_at columns

    #create column license_plate
    # create foreign keys to color, car
    # create relationship to color, car


