from flask import Blueprint, request, jsonify
from service.tasks import TasksActions
from functools import wraps
import jwt

main = Blueprint("main",__name__)

def token_verification(func):
    wraps(func)
    def verification(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        # return 401 if token is not passed
        if not token:
            return jsonify({'message' : 'Token is missing !!'}), 401
        try:
            data = jwt.decode(token, app.config['SECRETKEY'])
        except:
            return jsonify({
                'message' : 'Token is invalid !!'
            }), 401
        return  func(*args, **kwargs)
    verification.__name__ = func.__name__
    return verification


@main.route("/tasks",methods=["GET"])
@token_verification
def get():
    return TasksActions().get_tasks(request)
    

@main.route("/addTask", methods=["POST"])
@token_verification
def addTask():
    task = TasksActions().add_tasks(request)
    return task

# update description of the task
@main.route("/modifyTask", methods=['PUT'])
@token_verification
def modifyTask():
    return TasksActions().update_task(request)

# delete task
@main.route("/deleteTask", methods=["DELETE"])
@token_verification
def deleteTask():
    return TasksActions().delete_task(request)