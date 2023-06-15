from random import choice as rc

from app import app
from models import db, Color, Car, License
from faker import Faker

if __name__ == '__main__':

    fake = Faker()

    with app.app_context():
        print("Clearing db...")
        Car.query.delete()
        Color.query.delete()
        License.query.delete()

        ford = Car(manufacturer="ford")
        cadillac = Car(manufacturer="cadillac")
        porsche = Car(manufacturer="porsche")
        subaru = Car(manufacturer="subaru")
        volkswagon = Car(manufacturer="volkswagon")
        toyota = Car(manufacturer="toyota")
        jeep = Car(manufacturer="jeep")
        fiat = Car(manufacturer="fiat")
        audi = Car(manufacturer="audi")
        bentley = Car(manufacturer="bentley")
        bmw = Car(manufacturer="bmw")
        mercedes = Car(manufacturer="mercedes")

        cars = [ford, cadillac, porsche, subaru, volkswagon, toyota, jeep, fiat, audi, bentley, bmw, mercedes]

        db.session.add_all(cars)
        db.session.commit()


        yellow = Color(color="yellow")
        blue = Color(color="blue")
        red = Color(color="red")
        black = Color(color="black")
        green = Color(color="green")
        orange = Color(color="orange")
        purple = Color(color="purple")
        grey = Color(color="grey")
        brown = Color(color="brown")
        violet = Color(color="violet")
        white = Color(color="white")
        pink = Color(color="pink")
        silver = Color(color="silver")

        colors = [yellow, blue, red, black, green, orange, purple, grey, brown, violet, white, pink, silver]

        db.session.add_all(colors)
        db.session.commit()

        licenses = []
        for i in range(50):
            license = License(license_plate=fake.license_plate(), car=rc(cars), color=rc(colors))
            licenses.append(license)
        
        db.session.add_all(licenses)
        db.session.commit()

        

        print("Done seeding!")
