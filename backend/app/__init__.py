from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from flask_migrate import Migrate 
from flask_jwt_extended import JWTManager


db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    """
    An application factory, which creates and configures the app.
    """
    app = Flask(__name__)
    app.config.from_object(Config)
    jwt.init_app(app)


    db.init_app(app)
    migrate.init_app(app, db)

    from .routes.car_route import car_bp
    from .routes.auth_route import auth_bp

    app.register_blueprint(car_bp, url_prefix='/api/cars')
    app.register_blueprint(auth_bp, url_prefix='/api/auth')

    # --- Import Commands and Create DB ---
    with app.app_context():
         # Lazy import to avoid circular dependency
        from app.commands import seed_db
        app.cli.add_command(seed_db)
        db.create_all()

    return app