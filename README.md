[![Maintainability](https://api.codeclimate.com/v1/badges/f07185dddb5a12f9f15f/maintainability)](https://codeclimate.com/github/niomwungeri-fabrice/questionnaire-api/maintainability)
[![Coverage Status](https://coveralls.io/repos/github/niomwungeri-fabrice/questionnaire-api/badge.svg?branch=master)](https://coveralls.io/github/niomwungeri-fabrice/questionnaire-api?branch=master)
[![Build Status](https://travis-ci.com/niomwungeri-fabrice/questionnaire-api.svg?branch=master)](https://travis-ci.com/niomwungeri-fabrice/questionnaire-api)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
# Questionnaire REST API
Crowd-source questions for a meetup. ​Questioner​​ helps the meetup organizer prioritize questions to be answered. Other users can vote on asked questions and they bubble to the top or bottom of the log.

## Resources

| EndPoint| Functionality|
| --------| -------------|
|`GET /api/v1/admin`| Admin page |
|`POST /api/v1/register`| Create user account|
|`POST /api/v1/token`|Obtain authentication JWT token / SignIn|
|`GET /api/v1/token/refresh`|Refresh token|
|`GET /api/v1/users`|Get all users|
|`GET /api/v1/users/{id}`|Get specific user details|
|`GET /api/v1/me`|Current logged In user|
|`POST /api/v1/meetup/new/`|Create new meetUp|
|`GET /api/v1/meetup/{id}`|Get a specific meetUp using Id|
|`GET /api/v1/meeup`|Get all available meetUps|
|`POST /api/v1/tags`|Create list of tags|
|`POST api/v1/questions/`|Create a question|
|`GET api/v1/questions/`|Get list of all questions|
|`PUT/PATCH api/v1/questions/{id}`| Update a question|
|`DELETE api/v1/questions/{id}`|Delete a question|
|`GET api/v1/questions/{id}`|Get a specific question|
## Getting Started(With Docker)
* Install [Docker](https://docs.docker.com/docker-for-mac/install/)
```sh
$ git clone https://github.com/niomwungeri-fabrice/questionnaire-api.git
$ cd questionnaire-api
$ pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

### Build image
```sh
$ docker-compose build
```

### Run
```sh
$ docker-compose up # It will run migrations and start the server
```

## Getting Started(Without Docker)
```sh
$ git clone clone https://github.com/niomwungeri-fabrice/questionnaire-api.git
$ cd questionnaire-api
$ pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```
* Create a .env file and copy/paste the environment variables from the .env_example file that's already existent in the root project directory.
```sh
$ python manage.py migrate
```

### Run
```.sh
$ python manage.py runserver
```

### Tests
```sh
$ python manage.py test # Without coverage report
$ coverage run manage.py test && coverage report # With coverage report
```

## Built with 
- [Python](https://www.python.org/) - Python is an interpreted, high-level, general-purpose programming language. 
- [Django](https://www.djangoproject.com/) -  Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.
- [Django REST framework](https://www.django-rest-framework.org/) - is a powerful and flexible toolkit for building Web APIs
- [PostgreSQL](https://www.postgresql.org) - PostgreSQL is a powerful, open source object-relational database system that uses and extends the SQL language combined with many features that safely store and scale the most complicated data workloads.
