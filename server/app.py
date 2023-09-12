#!/usr/bin/env python3

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db, Engineer, Certificate, Instructor

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.get('/')
def index():
    return "Hello world"

# ENGINEERS CRUD #

@app.get('/engineers')
def engineers_index():
    engineers = Engineer.query.all()
    return [eng.to_dict() for eng in engineers], 200

@app.get('/engineers/<int:id>')
def engineers_show(id):
    engineer = Engineer.query.filter(Engineer.id == id).first()
    if engineer:
        return engineer.to_dict(), 200
    else:
        return {"message": "404 Not Found"}, 404

# CERTIFICATES CRUD #

@app.get('/certificates')
def certificates_index():
    certificates = Certificate.query.all()
    return [cert.to_dict() for cert in certificates], 200

@app.get('/certificates/<int:id>')
def certificates_show(id):
    certificate = Certificate.query.filter(Certificate.id == id).first()
    if certificate:
        return certificate.to_dict(), 200
    else:
        return {"message": "404 Not Found"}, 404

<<<<<<< HEAD
# BONUS --- INSTRUCTORS CRUD #

@app.get('/instructors')
def instructors_index():
    instructors = Instructor.query.all()
    return [instructor.to_dict() for instructor in instructors], 200

@app.get('/instructors/<int:id>')
def instructors_show(id):
    instructor = Instructor.query.filter(Instructor.id == id).first()
    if instructor:
        return instructor.to_dict(), 200
    else:
        return {"message": "404 Not Found"}, 404

=======
>>>>>>> main
# DEBUG ROUTE #

@app.get('/debug')
def debug():
    import ipdb; ipdb.set_trace()
    return {"message": "Debugging completed!"}

if __name__ == '__main__':
    app.run(port=5555, debug=True)
