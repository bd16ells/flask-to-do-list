from flask_sqlalchemy import SQLAlchemy
from settings import app
import json

db = SQLAlchemy(app)


class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(300), nullable=False)
    complete = db.Column(db.Boolean, default=False)
    

    def getTaskById(_id):
        return Task.query.filter_by(id=_id).first()


    def addTask(_description):
        db.session.add(Task(description=_description))
        db.session.commit()


    def updateTask(_id, _description):
        task = Task.query.filter_by(id=_id).first()
        task.description = _description
        db.session.commit()


    def toggleComplete(id):
        task = Task.getTaskById(id)
        task.complete = not task.complete
        db.session.commit()

    
    def getAllTasks():
        return Task.query.all()


    def deleteTask(_id):
        is_successful = Task.query.filter_by(id=_id).delete()
        db.session.commit()
        return bool(is_successful)


    def __repr__(self):
        task = {
            'id': self.id,
            'description': self.description,
            'complete': self.complete
        }
        return json.dumps(task)