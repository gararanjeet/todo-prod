# from flask import register_blueprint
from route.task import main
from route.user import user
def register_blueprints(app):
    app.register_blueprint(main)
    app.register_blueprint(user)
    return app
