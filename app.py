from flask import Flask
from database_helper import DatabaseHelper
app=Flask(__name__)
db_instance=DatabaseHelper()

@app.route('/api/tasks',methods=["GET"])
def get():
    db_instance.get_a_todo()

@app.route('/api/tasks/bystatus/<status>',methods=["GET"])
def get_by_status(status):
    db_instance.get_a_todo_by_status(status)

@app.route('/api/tasks/byid/<id>',methods=["GET"])
def get_a_todo_by_id(id):
    db_instance.get_a_todo_by_id(id)


@app.route('/api/tasks/delete/<id>',methods=["DELETE"])
def delete(id):
    db_instance.delete_a_to_do(id)

@app.route('/api/tasks/post', methods=["POST"])
def post():
    db_instance.add_a_todo()

@app.route('/api/tasks/update/<id>', methods=["PUT"])
def update(id):
    db_instance.update_a_to_do(id)
if __name__ == '__main__':


    app.run(debug=True)