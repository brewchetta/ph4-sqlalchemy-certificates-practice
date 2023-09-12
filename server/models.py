from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

# this metadata does some additional work for naming foreign keys #
# you can read the docs if you'd like:
# https://docs.sqlalchemy.org/en/13/core/constraints.html#constraint-naming-conventions
metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)


class Engineer(db.Model):

    # WRITE YOUR CODE HERE #

    # this is a custom to_dict method,
    # you may delete this and use the SerializerMixin if you prefer
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "expiration_year": self.expiration_year
        }


class Certificate(db.Model):

    # WRITE YOUR CODE HERE #

    # this is a custom to_dict method
    # you may delete this and use the SerializerMixin if you prefer
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "expiration_year": self.expiration_year
        }
