import click
from flask.cli import with_appcontext
from app import db
from app.models.car_model import Car
from app.database.seed.car_factory import CarFactory

@click.command(name="seed_db")
@with_appcontext
def seed_db():
    """Seeds the database with fake Car data using Factory Boy."""
    if Car.query.first():
        click.echo("Database already seeded. Skipping.")
        return

    click.echo("Seeding database with fake cars...")

    # Generate 20 fake cars
    CarFactory.create_batch(20)

    db.session.commit()
    click.echo("Database seeded successfully with fake cars!")
