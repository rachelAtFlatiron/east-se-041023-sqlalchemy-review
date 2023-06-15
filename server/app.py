from flask import Flask, make_response, request
from flask_migrate import Migrate 
from flask_restful import Api, Resource

from models import db, Car, License, Color

# initialize flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

# db is the SQLAlchemy instance coming from models.py
migrate = Migrate(app, db)

db.init_app(app)
# enable flask_restful
api = Api(app)

@app.route('/')
def home():
    return "Code Challenge"

'''
Error: 404 Not Found: The requested URL was not found on the server. If you entered the URL manually please check your spelling and try
	again.

- double check you did api.add_resource
'''

'''
Error: AttributeError: type object Car has no attribute query
- class name is overwriting the model name
'''

'''
Error: 'Car' object has no attribute 'to_dict'
- make sure you imported SerializerMixin in your models.py
'''

'''
Error: RecursionError: maximum recursion depth exceeded in comparison
- add your serialize_rules to prevent this
'''

'''
Error: TypeError: The view function did not return a valid response. The return type must be a string, dict, list,
		tuple with headers or status, Response instance, or WSGI callable, but it was a Car

- did you return your response?
- did you use .to_dict() / turn the response into a dictionary?
'''

'''
Error: 405: "The method is not allowed for the requested URL."

- did you write the method for the route?
'''
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Cars(Resource):
    def get(self):
        #1. query for all the cars
        cars = Car.query.all()
        #2. convert to dictionary
        cars_dict = [c.to_dict() for c in cars]
        #3. return the response
        res = make_response(cars_dict, 200)
        return res 
    def post(self):
        #1. get the data
        data = request.get_json() #due to using header content-type: application/json in front-end
        #2. create a Car instance with said data
        new_car = Car(manufacturer=data.get('manufacturer'))
        #3. add/commit new car to db
        db.session.add(new_car)
        db.session.commit()
        #4. response
        res = make_response(new_car.to_dict(), 201)
        return res 
#Cars refers to the Resource class
api.add_resource(Cars, '/cars')

class OneCar(Resource):
    def get(self, id):
        #1. get car by id
        car = Car.query.filter_by(id=id).first() #filter_by returns a list
        #2. convert to dict
        car_dict = car.to_dict()
        #3. res
        return make_response(car_dict, 200)
    def delete(self, id):
        #1. get car by id
        car = Car.query.filter_by(id=id).first()
        #2. delete from database
        db.session.delete(car)
        db.session.commit()
        #3. empty response
        return make_response({}, 204)
    def patch(self, id):
        #1. get car by id
        car = Car.query.filter_by(id=id).first()
        #2. get data from request
        data = request.get_json()
        #3. update values in car
        for attr in data:
            setattr(car, attr, data.get(attr)) #pass in attr as the variable
        #4. update the database
        db.session.add(car)
        db.session.commit()
        #5. res
        return make_response(car.to_dict(), 200)

api.add_resource(OneCar, '/cars/<int:id>')



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Colors(Resource):
    def get(self):
        colors = Color.query.all()
        colors_dict = [c.to_dict() for c in colors]
        res = make_response(colors_dict, 200)
        return res 
    def post(self):
        #1. get the data
        data = request.get_json() #due to using header content-type: application/json in front-end
        #2. create a Color instance with said data
        new_color = Color(color=data.get('color'))
        #3. add/commit new car to db
        db.session.add(new_color)
        db.session.commit()
        #4. response
        res = make_response(new_color.to_dict(), 201)
        return res 
api.add_resource(Colors, '/colors')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Licenses(Resource):
    def get(self):
        #1. query
        licenses = License.query.all()
        #2. dictionary
        licenses_dict = [l.to_dict() for l in licenses]
        #3.response
        res = make_response(licenses_dict, 200)
        return res 
    def post(self):
        #1. get the data
        data = request.get_json()
        #2. create a License instance with said data
        license = License(license_plate=data.get('license_plate'), car_id=data.get('car_id'), color_id=data.get('color_id'))
        #3. add/commit new license to db
        db.session.add(license)
        db.session.commit()
        #4. response
        return make_response(license.to_dict(), 201)

#add_resource
api.add_resource(Licenses, '/licenses')

if __name__ == ("__main__"):
    app.run(port=5555, debug=True)
