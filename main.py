from flask import Flask, jsonify, request, Response, render_template, redirect, url_for
from settings import *
from domain import *

app = Flask(__name__)

@app.route('/tasks')
def getTasks():
    return render_template('tasks.html', tasks=Task.getAllTasks())


@app.route('/tasks', methods=['POST'])
def addTask():
    data = request.form['description']
    Task.addTask(_description=data)
    return Response("", 201)


@app.route('/tasks/<int:id>', methods=['DELETE'])
def deleteTask(id):
    Task.deleteTask(_id=id)
    return Response("", 204)


@app.route('/tasks/<int:id>/complete', methods=['PUT'])
def toggleTaskComplete(id):
    Task.toggleComplete(id)
    return Response("", 201)


@app.route('/tasks/<int:id>', methods=['PATCH'])
def updateTask(id):
    data = request.form['description']
    Task.updateTask(_id=id, _description=data)
    return Response("", 201)


if __name__ == "__main__":
    app.run(port=5000)