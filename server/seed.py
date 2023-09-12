#!/usr/bin/env python3

from app import app
from models import db, Engineer, Certificate
from faker import Faker
import random

faker = Faker()

if __name__ == '__main__':
    with app.app_context():
        print("Seeding database...")

        print("Removing old data...")
        Certificate.query.delete()
        Engineer.query.delete()

        print("Creating engineers...")

        specialties = ("fullstack", "frontend", "backend", "quality assurance", "devops")
        engineers = []

        for num in range(10):
            engineer = Engineer(name=faker.name(), specialty=random.choice(specialties), age=random.randint(19, 70))
            engineers.append(engineer)

        db.session.add_all(engineers)
        db.session.commit()

        print("Creating certificates...")

        cert_titles = ("AWS", "Azure", "Github")
        certs = []

        for num in range(40):
            cert = Certificate(title=random.choice(cert_titles), expiration_year=random.randint(2022, 2030))
            cert.engineer = random.choice(engineers)
            certs.append(cert)

        db.session.add_all(certs)
        db.session.commit()

        print("Seeding complete!")
