# jaram_wiki

Wiki Application for archiving study, seminar, workshop documents, powered by [Django](https://github.com/django/django) framework.

Prerequisites
---
Python version 3.x
PostgreSQL Server

Installation
---
```
# Clone this repo on your working directory
$ git clone https://github.com/Jaram2017/jaram-wiki

# Change directory into the cloned repository
$ cd jaram-wiki

# Install required packages
$ pip install pipenv
$ pipenv install
```

Start the server
---

```
# activate the virtualenv
$ pipenv shell
# Migrate models
$ python manage.py migrate
# Run Django Server
$ python manage.py runserver
```
