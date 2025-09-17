from typing import Optional, List, Tuple
from app import db
from app.models.car import Car

# Create a car
def create_car(make: str, model: str, year: int, price: float) -> Car:
    car = Car(make=make, model=model, year=year, price=price)
    db.session.add(car)
    db.session.commit()
    return car

# Get all cars with pagination
def get_all_cars(page: int = 1, per_page: int = 10) -> Tuple[List[Car], int]:
    """
    Returns a tuple of (cars, total_pages)
    """
    paginated = Car.query.paginate(page=page, per_page=per_page, error_out=False)
    return paginated.items, paginated.pages

# Get car by ID
def get_car_by_id(car_id: int) -> Optional[Car]:
    return Car.query.get(car_id)

# Update a car
def update_car(car_id: int, make: Optional[str] = None, model: Optional[str] = None, 
               year: Optional[int] = None, price: Optional[float] = None) -> Optional[Car]:
    car = get_car_by_id(car_id)
    if not car:
        return None
    if make is not None:
        car.make = make
    if model is not None:
        car.model = model
    if year is not None:
        car.year = year
    if price is not None:
        car.price = price
    db.session.commit()
    return car

# Delete a car
def delete_car(car_id: int) -> bool:
    car = get_car_by_id(car_id)
    if not car:
        return False
    db.session.delete(car)
    db.session.commit()
    return True
