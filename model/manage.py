from extension.manage import db, ma

class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    task = db.Column(db.String(250))
    isCompleted = db.Column(db.Boolean, default = False)
    isImportant = db.Column(db.Boolean, default = False)

    def __init__(self, task, isCompleted = False, isImportant = False):
        self.task = task
        self.isCompleted = isCompleted
        self.isImportant = isImportant

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

# Schema
class TasksSchema(ma.Schema):
    class Meta:
        fields = ("id", "task", "isCompleted", "isImportant")

class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "email", "password")

task_schema = TasksSchema()
tasks_schema = TasksSchema(many=True)
user_schema = UserSchema()
users_schema = UserSchema(many=True)