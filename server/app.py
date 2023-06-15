from flask import Flask, make_response, request
from flask_migrate import Migrate 
from flask_restful import Api, Resource

from models import db, Car, License, Color

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)
api = Api(app)

@app.route('/')
def home():
    return "C A R S"
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
class Cars(Resource):
    def get(self):
        cars = Car.query.all()
        return make_response(cars.to_dict(), 200)
    def post(self):
        data = request.get_json()
        car = Car(manufacturer=data.get('manufacturer'))
        db.session.add(car)
        db.session.commit()
        return make_response(car.to_dict(), 201)
api.add_resource(Cars, '/cars')

class OneCar(Resource):
    def get(self, id):
        car = Car.query.filter_by(id=id).first()
        return make_response(car.to_dict(), 200)
    def patch(self, id):
        data = request.get_json()
        car = Car.query.filter_by(id=id).first()
        for attr in data:
            setattr(car, attr, data.get(attr))
        db.session.add(car)
        db.session.commit()
        return make_response(car.to_dict(), 200)
    def delete(self, id):
        car = Car.query.filter_by(id=id).first()
        db.session.delete(car)
        db.session.commit()
        return make_response({}, 204)
api.add_resource(OneCar, '/cars/<int:id>')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Colors(Resource):
    def get(self):
        colors = Color.query.all()
        return make_response(colors.to_dict(), 200)
    def post(self):
        data = request.get_json()
        color = Color(color=data.get('color'))
        db.session.add(color)
        db.session.commit()
        return make_response(color.to_dict(), 201)
api.add_resource(Colors, '/colors')

class OneColor(Resource):
    def get(self, id):
        color = Color.query.filter_by(id=id).first()
        return make_response(color.to_dict(), 200)
    def patch(self, id):
        data = request.get_json()
        color = Color.query.filter_by(id=id).first()
        for attr in data:
            setattr(color, attr, data.get(attr))
        db.session.add(color)
        db.session.commit()
        return make_response(color.to_dict(), 200)
    def delete(self, id):
        color = Color.query.filter_by(id=id).first()
        db.session.delete(color)
        db.session.commit()
        return make_response({}, 204)
api.add_resource(OneColor, '/colors/<int:id>')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Licenses(Resource):
    def get(self):
        licenses = License.query.all()
        return make_response(licenses.to_dict(), 200)
    def post(self):
        data = request.get_json()
        license = License(license_plate=data.get('license_plate'))
        db.session.add(license)
        db.session.commit()
        return make_response(license.to_dict(), 201)
api.add_resource(Licenses, '/licenses')

class OneLicense(Resource):
    def get(self, id):
        license = License.query.filter_by(id=id).first()
        return make_response(license.to_dict(), 200)
    def patch(self, id):
        data = request.get_json()
        license = License.query.filter_by(id=id).first()
        for attr in data:
            setattr(license, attr, data.get(attr))
        db.session.add(license)
        db.session.commit()
        return make_response(license.to_dict(), 200)
    def delete(self, id):
        license = License.query.filter_by(id=id).first()
        db.session.delete(license)
        db.session.commit()
        return make_response({}, 204)
api.add_resource(OneLicense, '/licenses/<int:id>')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

if __name__ == ("__main__"):
    app.run(port=5555, debug=True)
