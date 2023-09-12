# Flask SQLAlchemy Practice

You've been tasked with creating a flask database that tracks all engineers and the certifications they've gotten for services like AWS.

Don't worry too much about the routing, your focus here should be on building the models and the database itself.

## Getting Started

Fork and clone the repo. In your terminal run `pipenv install` and `pipenv shell`.

From here `cd server` and you can run the server with `python3 app.py`.

You have a seed file. The purpose of this file is to quickly and efficiently create testing data. You may run the seed file with `python3 seed.py`.

Please note the seed file won't work until you've completed your models.

## Models

You have two models, an engineer and a certificate. Engineers have many certificates and a certificate belongs to an engineer. You'll have to create a `relationship` between the two and be mindful of the foreign key, it's not included in the table columns listed below!

Your goal is to build out the models and the relationship between them being sure to run all proper migrations and upgrades. You'll know that you're on the right track if you're able to seed properly.

### Engineer

An engineer has at least three attributes:

| Column    | Type    |
|-----------|---------|
| id        | integer |
| name      | string  |
| specialty | string  |
| age       | integer |

An engineer has many certificates.

### Certificate

A certificate has at least two attributes:

| Column          | Type     |
|-----------------|----------|
| id              | integer  |
| title           | string   |
| expiration_year | integer  |

A certificate belongs to an engineer.

## Given Routes

You currently have two routes for each model. You may build additional routes if you feel confident however the routes are mainly for testing purposes.

You can hit your routes by first running the server and then making a request with Postman or another utility to `http://localhost:5555/engineers` (replace engineers with the route of your choice).

Please note the routes will throw an error if you don't complete your models first.

### GET /engineers and GET /certificates

These are set up to send back data for either every engineer or every certificate as a dictionary.

### GET /engineers/:id and GET /certificates/:id

These are set up to send back data for a single engineer or certificate by id.

Will respond with a 404 error if no engineer or certificate is found.
