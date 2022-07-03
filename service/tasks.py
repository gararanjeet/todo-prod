from model.manage import Tasks, task_schema, tasks_schema
from extension.manage import db

class TasksActions():
    def get_tasks(self, request):
        tasks = Tasks.query.all()
        return tasks_schema.jsonify(tasks)

    def add_tasks(self, request):
        task = request.json.get('task')
        isImportant = False
        isCompleted = False
        new_task = Tasks(task, isImportant, isCompleted)
        db.session.add(new_task)
        db.session.commit()
        return task_schema.jsonify(new_task)

    def update_task(self, request):
        id = request.json.get("id")
        newTask = request.json.get("newTask")
        if id == None:
            return jsonify({"message":"Please provide id"}), 400
        elif newTask == "":
            return jsonify({"message":"Cannot update empty string"}), 400
        task = Tasks.query.get(id)
        task.task = newTask
        db.session.commit()
        return jsonify({"message":"success"})

    def delete_task(self, request):
        id = request.json.get("id")
        if id == None:
            return jsonify({"message":"Please provide id"}), 400
        task = Tasks.query.filter_by(id=id).delete()
        db.session.commit()
        return jsonify({"message":"success"})