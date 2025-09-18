import click
from flask.cli import with_appcontext
from app import db
from app.database.seed.factories import CarFactory, UserFactory
from app.models.car import Car, EngineType, TransmissionType, BodyType, DriveType
from app.models.user import  UserType
from app.enum.user_type_enum import UserTypeEnum

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
    user_type_objs = {}
    USER_TYPE_LABELS = {
            UserTypeEnum.ADMIN: "admin",
            UserTypeEnum.CUSTOMER: "user", 
    }

    for enum_member, label in USER_TYPE_LABELS.items():
        obj = UserType.query.get(enum_member.value)
        if not obj:
            obj = UserType(id=enum_member.value, name=label)
            db.session.add(obj)
        user_type_objs[enum_member] = obj

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
    
    click.echo("Seeding admin and user...")
    UserFactory(user_type=user_type_objs["admin"])
    UserFactory(user_type=user_type_objs["user"])
    db.session.commit()
    
    # use the factories to create fake data
    click.echo("Seeding database with fake users...")
    UserFactory.create_batch(5)

    click.echo("Seeding database with fake cars...")
    CarFactory.create_batch(20)

    # save all changes to the
    db.session.commit()
    click.echo("Database seeded successfully!")