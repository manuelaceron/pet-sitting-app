from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from celery import Celery, Task
import logging 
from .config import Config

db = SQLAlchemy()
login_manager = LoginManager()
mail = Mail() 

# Create flask instance
def create_app() -> Flask:
    
    # Instance of flask app
    app = Flask(__name__)

    # Flask configuration settings
    app.config['SECRET_KEY'] = Config.SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI

    # Celery settings
    app.config['CELERY'] = dict(
        broker_url=Config.CELERY_BROKER_URL,
        result_backend=Config.CELERY_RESULT_BACKEND,
        task_ignore_result=False,
    )
    app.config.from_prefixed_env()
    app.logger.setLevel(logging.INFO)
    
    # Initialize extensions
    db.init_app(app)  
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)    

    """ 
    - LoginManager manages sessions, user authentication, and redirection for login-required routes.
    - login_view specifies the page to which unauthenticated users are redirected.
    - init_app(app) integrates the login manager with the Flask application instance. """
    
    app.config['MAIL_SERVER'] = Config.MAIL_SERVER
    app.config['MAIL_PORT'] = Config.MAIL_PORT
    app.config['MAIL_USERNAME'] = Config.MAIL_USERNAME
    app.config['MAIL_PASSWORD'] = Config.MAIL_PASSWORD
    app.config['MAIL_USE_TLS'] = Config.MAIL_USE_TLS
    app.config['MAIL_USE_SSL'] = Config.MAIL_USE_SSL     

    mail.init_app(app)          

    from .models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    # Register Blueprints into our app instance
    from .main import mainBp as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import authBp as auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    celery_init_app(app)

    return app

def celery_init_app(app: Flask) -> Celery:
    class FlaskTask(Task):
        def __call__(self, *args: object, **kwargs: object) -> object:
            with app.app_context():
                return self.run(*args, **kwargs)

    celery_app = Celery(app.name, task_cls=FlaskTask)
    celery_app.config_from_object(app.config["CELERY"])
    celery_app.set_default()
    app.extensions["celery"] = celery_app
    return celery_app