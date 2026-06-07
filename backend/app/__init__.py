from flask import Flask
from .extensions import db, jwt, migrate, cors
from dotenv import load_dotenv

def create_app():
    load_dotenv()

    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    cors.init_app(app)

    # Register blueprints
    from .routes.auth import auth_bp
    app.register_blueprint(auth_bp)

    return app
