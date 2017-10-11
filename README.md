# jaram_wiki

Wiki Application for archiving study, seminar, workshop documents, powered by [Django](https://github.com/django/django) framework.

Prerequisites
---
Python version 3.x

Installation
---
```
# Clone this repo on your working directory
$ git clone https://github.com/Jaram2017/jaram-wiki

# Change directory into the cloned repository
$ cd jaram-wiki

# Create a virtualenv
$ pip install virtualenv
$ virtualenv venv 

# activate the virtualenv
$ . venv/bin/activate

# Install the packages.
$ pip install -r requirements.txt
```

Start the server
---

```
# Migrate models
$ python manage.py migrate
# Run Django Server
$ python manage.py runserver
```
