from app import db
from app.models.car import Car

# Create a car
def create_car(make, model, year, price):
    car = Car(make=make, model=model, year=year, price=price)
    db.session.add(car)
    db.session.commit()
    return car

# Get all cars
def get_all_cars():
    return Car.query.all()

# Get car by ID
def get_car_by_id(car_id):
    return Car.query.get(car_id)

# Update a car
def update_car(car_id, make=None, model=None, year=None, price=None):
    car = get_car_by_id(car_id)
    if not car:
        return None
    if make:
        car.make = make
    if model:
        car.model = model
    if year:
        car.year = year
    if price:
        car.price = price
    db.session.commit()
    return car

# Delete a car
def delete_car(car_id):
    car = get_car_by_id(car_id)
    if not car:
        return False
    db.session.delete(car)
    db.session.commit()
    return True