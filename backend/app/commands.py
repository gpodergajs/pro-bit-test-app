import click
from flask.cli import with_appcontext
from . import db
from .models import Car

@click.command(name='seed_db')
@with_appcontext
def seed_db():
    """Seeds the database with initial data."""
    if Car.query.first():
        click.echo("Database already seeded. Skipping.")
        return

    click.echo("Seeding database...")
    # Your SQLAlchemy objects are created and committed here
    car1 = Car(make="Toyota", model="Camry", year=2021, price=20000)
    db.session.add(car1)
    db.session.commit()
    click.echo("Database seeded successfully.")