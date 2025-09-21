from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from flask_migrate import Migrate 
from flask_jwt_extended import JWTManager
from .common.logger import get_logger
from flask_cors import CORS


db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    """
    An application factory, which creates and configures the app.
    """
    app = Flask(__name__)
    CORS(app)  # Enable CORS for all routes
    app.config.from_object(Config)

    # Configure logging
    logger = get_logger(__name__)
    logger.setLevel(logging.INFO)
    app.logger = logger
    jwt.init_app(app)


    db.init_app(app)
    migrate.init_app(app, db)

    from .cars.routes import car_bp
    from .users.routes import users_bp

    app.register_blueprint(car_bp, url_prefix='/api/cars')
    app.register_blueprint(users_bp, url_prefix='/api/users')

    # --- Import Commands and Create DB ---
    with app.app_context():
         # Lazy import to avoid circular dependency
        from app.commands import seed_db
        app.cli.add_command(seed_db)
        db.create_all()

    return app