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
    # create table name cars

    # create id, created_at, and updated_at columns
    # create column manufacturer

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
    # foreign key to color
    # foreign key to cars 


    # relationship between car and license
    # relationship between color and license


