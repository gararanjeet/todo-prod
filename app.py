from flask import Flask
from extension.manage import db, ma
from route import register_blueprints
import os

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI")

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECRETKEY'] = os.environ.get("SECRETKEY")

db.init_app(app)

ma.init_app(app)

app = register_blueprints(app)

if __name__ == "__main__":
    app.run(debug=True)