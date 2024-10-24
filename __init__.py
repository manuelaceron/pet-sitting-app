from flask import Flask

# Create flask instance
def create_app():
    
    # Instance of flask app
    app = Flask(__name__)
    
    # Register Blueprints into our app instance
    from .main import mainBp as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import authBp as auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    return app