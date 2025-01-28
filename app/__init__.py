from flask import Config, Flask
# from .config import Config


def create_app():
    app = Flask(__name__)
    # Load configurations
    app.config.from_object(Config)
    
    # Register routes
    from .api import main
    app.register_blueprint(main)
    
    return app