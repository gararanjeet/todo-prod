from flask import Blueprint, request
from service.authenticate import Authenticate


user = Blueprint("user", __name__)

@user.route("/",methods=["POST"])
def login():
    try:
        token = Authenticate().login_action(request)
        return {"token":token}
    except KeyError:
        return "email and password is required", 400
    except ValueError:
        return "Incorrect Credentials", 400

@user.route("/register", methods=['POST'])
def register():
    try:
        token = Authenticate().register_action(request)
        return token
    except KeyError:
        return "provide all the details", 400
    except ValueError:
        return "provide valid details", 400