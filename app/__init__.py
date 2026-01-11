from flask import Flask
from app.extensions import db, ma, limiter, cache
from flask_migrate import Migrate

# Import blueprints
from app.customers import customers_bp
from app.mechanics import mechanics_bp
from app.service_tickets import service_tickets_bp
from app.service_ticket_mechanics import service_ticket_mechanics_bp
from app.vehicles import vehicles_bp
from app.inventory import inventory_bp


def create_app():
    app = Flask(__name__)

    # ----------------------------
    # Configuration
    # ----------------------------
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:Secretgarden@localhost/mechanic_shop"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Cache configuration
    app.config["CACHE_TYPE"] = "SimpleCache"
    app.config["CACHE_DEFAULT_TIMEOUT"] = 60

    # Required for sessions / security
    app.config["SECRET_KEY"] = "super-secret-key"  # replace for prod

    # ----------------------------
    # Initialize extensions
    # ----------------------------
    db.init_app(app)
    ma.init_app(app)
    limiter.init_app(app)
    cache.init_app(app)

    migrate = Migrate(app, db)

    # ----------------------------
    # Register Blueprints
    # ----------------------------
    app.register_blueprint(customers_bp, url_prefix="/customers")
    app.register_blueprint(mechanics_bp, url_prefix="/mechanics")
    app.register_blueprint(service_tickets_bp, url_prefix="/service_tickets")
    app.register_blueprint(service_ticket_mechanics_bp, url_prefix="/service_ticket_mechanics")
    app.register_blueprint(vehicles_bp, url_prefix="/vehicles")
    app.register_blueprint(inventory_bp, url_prefix="/inventory")

    return app

