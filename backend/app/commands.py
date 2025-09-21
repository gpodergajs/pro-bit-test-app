import click
from flask.cli import with_appcontext
from app import db
from app.database.seed.factories import CarFactory, UserFactory
from app.common.logger import get_logger

logger = get_logger(__name__)

from app.common.enums.user_type_enum import UserTypeEnum
from app.cars.models import Car, BodyType, EngineType, TransmissionType, DriveType
from app.users.models import UserType



@click.command(name="seed_db")
@with_appcontext
def seed_db():
    """
    CLI command to seed the database with initial data.

    This command creates default user types (Admin, User), various car-related lookup data
    (BodyType, EngineType, TransmissionType, DriveType), and then generates
    fake user and car data using Factory Boy.
    """
    logger.info("Starting database seeding process.")
    if Car.query.first():
        logger.info("Database already seeded. Skipping.")
        click.echo("Database already seeded. Skipping.")
        return

    try:
        click.echo("Seeding lookup tables...")
        logger.info("Seeding lookup tables...")
        # Seed lookup tables if they are empty
        click.echo("Seeding database lookup tables...")
        logger.info("Seeding database lookup tables...")
        user_type_objs = {}
        USER_TYPE_LABELS = {
                UserTypeEnum.ADMIN: "admin",
                UserTypeEnum.USER: "user", 
        }

        for enum_member, label in USER_TYPE_LABELS.items():
            obj = UserType.query.get(enum_member.value)
            if not obj:
                obj = UserType(id=enum_member.value, name=label)
                db.session.add(obj)
            user_type_objs[enum_member] = obj

        for btype in ["SUV", "Sedan", "Hatchback"]:
            if not BodyType.query.filter_by(name=btype).first():
                db.session.add(BodyType(name=btype))

        for etype in ["Petrol", "Diesel", "Electric", "Hybrid"]:
            if not EngineType.query.filter_by(name=etype).first():
                db.session.add(EngineType(name=etype))

        for ttype in ["Automatic", "Manual", "CVT"]:
            if not TransmissionType.query.filter_by(name=ttype).first():
                db.session.add(TransmissionType(name=ttype))

        for dtype in ["FWD", "AWD", "RWD"]:
            if not DriveType.query.filter_by(name=dtype).first():
                db.session.add(DriveType(name=dtype))

        # commit so that factories can use these entries
        db.session.commit()    
        
        click.echo("Seeding admin and user...")
        logger.info("Seeding admin and user...")
        UserFactory(user_type=user_type_objs[UserTypeEnum.ADMIN])
        UserFactory(user_type=user_type_objs[UserTypeEnum.USER])
        db.session.commit()
        
        # use the factories to create fake data
        click.echo("Seeding database with fake users...")
        logger.info("Seeding database with fake users...")
        UserFactory.create_batch(5)

        click.echo("Seeding database with fake cars...")
        logger.info("Seeding database with fake cars...")
        CarFactory.create_batch(20)

        # save all changes to the
        db.session.commit()
        click.echo("Database seeded successfully!")
        logger.info("Database seeded successfully!")
    except Exception as e:
        db.session.rollback()
        logger.error(f"Error during database seeding: {e}")
        click.echo(f"Error during database seeding: {e}")