from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
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

    # TO DICT #

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "expiration_year": self.expiration_year
        }


# CERTIFICATE CLASS #

class Certificate(db.Model):

    __tablename__ = "certificates"

    # COLUMNS #

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String)
    expiration_year = db.Column(db.Integer)
    engineer_id = db.Column(db.Integer, db.ForeignKey('engineers.id'))

    # RELATIONSHIPS #

    engineer = db.relationship('Engineer', back_populates='certificates')

    # TO DICT #

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "expiration_year": self.expiration_year
        }
