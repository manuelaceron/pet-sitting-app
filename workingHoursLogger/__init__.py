from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()

# Create flask instance
def create_app():
    
    # Instance of flask app
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret-key' #strong, random key in production to prevent attacks like session hijacking or cross-site request forgery, typically in config files
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    # Initialize the database with the app
    db.init_app(app)

    """ 
    - LoginManager manages sessions, user authentication, and redirection for login-required routes.
    - login_view specifies the page to which unauthenticated users are redirected.
    - init_app(app) integrates the login manager with the Flask application instance. """
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    # Register Blueprints into our app instance
    from .main import mainBp as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import authBp as auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    return app