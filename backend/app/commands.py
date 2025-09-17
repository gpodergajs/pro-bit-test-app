import click
from flask.cli import with_appcontext
from app import db
from app.database.seed.factories import CarFactory, UserFactory
from app.models.car import Car, EngineType, TransmissionType, BodyType, DriveType
from app.models.user import  UserType

@click.command(name="seed_db")
@with_appcontext
def seed_db():
    """Seeds the database with fake Car data using Factory Boy."""
    if Car.query.first():
        click.echo("Database already seeded. Skipping.")
        return

    click.echo("Seeding lookup tables...")
    # Seed lookup tables if they are empty
    click.echo("Seeding database lookup tables...")
    for ut in ["user", "admin"]:
        if not UserType.query.filter_by(name=ut).first():
            db.session.add(UserType(name=ut))

    for btype in ["SUV", "Sedan", "Hatchback"]:
        if not BodyType.query.filter_by(type=btype).first():
            db.session.add(BodyType(type=btype))

    for etype in ["Petrol", "Diesel", "Electric", "Hybrid"]:
        if not EngineType.query.filter_by(type=etype).first():
            db.session.add(EngineType(type=etype))

    for ttype in ["Automatic", "Manual", "CVT"]:
        if not TransmissionType.query.filter_by(type=ttype).first():
            db.session.add(TransmissionType(type=ttype))

    for dtype in ["FWD", "AWD", "RWD"]:
        if not DriveType.query.filter_by(type=dtype).first():
            db.session.add(DriveType(type=dtype))
    
    # commit so that factories can use these entries
    db.session.commit()    
    
    # use the factories to create fake data
    click.echo("Seeding database with fake users...")
    UserFactory.create_batch(5)

    click.echo("Seeding database with fake cars...")
    CarFactory.create_batch(20)

    # save all changes to the
    db.session.commit()
    click.echo("Database seeded successfully!")