from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    CORS(app)

    from .models import User, Donation

    # Register Blueprints
    from .routes.user_routes import user_bp
    from .routes.ngo_routes import ngo_bp
    from .routes.admin_routes import admin_bp

    app.register_blueprint(user_bp, url_prefix='/user')
    app.register_blueprint(ngo_bp, url_prefix='/ngo')
    app.register_blueprint(admin_bp, url_prefix='/admin')

    with app.app_context():
        db.create_all()

    return app
