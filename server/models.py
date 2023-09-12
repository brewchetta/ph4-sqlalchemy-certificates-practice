from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.sql import func
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

# INITIALIZATION #

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

# ENGINEER CLASS #

class Engineer(db.Model):

    __tablename__ = "engineers"

    # COLUMNS #

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    specialty = db.Column(db.String)
    age = db.Column(db.Integer)

    # RELATIONSHIPS #

    certificates = db.relationship('Certificate', back_populates='engineer')
    instructors = association_proxy('certificates', 'instructor')

    # TO DICT #

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "specialty": self.specialty,
            "age": self.age,
            "certificates": [ cert.to_dict() for cert in self.certificates ]
        }


# CERTIFICATE CLASS #

class Certificate(db.Model):

    __tablename__ = "certificates"

    # COLUMNS #

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String)
    expiration_year = db.Column(db.Integer)
    engineer_id = db.Column(db.Integer, db.ForeignKey('engineers.id'))
    instructor_id = db.Column(db.Integer, db.ForeignKey('instructors.id'))

    # RELATIONSHIPS #

    engineer = db.relationship('Engineer', back_populates='certificates')
    instructor = db.relationship('Instructor', back_populates='certificates')

    # TO DICT #

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "expiration_year": self.expiration_year
        }

# INSTRUCTOR CLASS #

class Instructor(db.Model):

    __tablename__ = "instructors"

    # COLUMNS #

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    # RELATIONSHIPS #

    certificates = db.relationship('Certificate', back_populates='instructor')
    engineers = association_proxy('certificates', 'engineer')

    # TO DICT #

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "engineers": [eng.to_dict() for eng in self.engineers]
        }
