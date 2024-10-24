from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

# Create flask instance
def create_app():
    
    # Instance of flask app
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret-key' #strong, random key in production to prevent attacks like session hijacking or cross-site request forgery, typically in config files
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    # Initialize the database with the app
    db.init_app(app) 

    with app.app_context():  
        db.create_all()

    
    # Register Blueprints into our app instance
    from .main import mainBp as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import authBp as auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    return app