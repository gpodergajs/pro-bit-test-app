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

    # --- Import and Register Blueprints ---

    # Import the blueprint object from your routes file
    from .routes import api_bp
    
    # Register the blueprint with the app and set a URL prefix.
    # All routes in api_bp will now be prefixed with /api.
    # So, '/cars' becomes '/api/cars'.
    app.register_blueprint(api_bp, url_prefix='/api')

    # --- Import Commands and Create DB ---
    
    from .commands import seed_db
    app.cli.add_command(seed_db)

    with app.app_context():
        # You need to import models here so create_all knows about them
        from . import models
        db.create_all()

    return app