from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from flask_migrate import Migrate 

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    """
    An application factory, which creates and configures the app.
    """
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes.car_route import car_bp

    app.register_blueprint(car_bp, url_prefix='/api/cars')

    # --- Import Commands and Create DB ---
    with app.app_context():
         # Lazy import to avoid circular dependency
        from app.commands import seed_db
        app.cli.add_command(seed_db)
        db.create_all()

    return app