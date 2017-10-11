jaram_wiki
---
자람의 스터디, 세미나, 워크샵 내용을 아카이브하는 위키 사이트를 개발하는 스터디

installation
---
```
# Clone this repo on your working directory
$ git clone https://github.com/Jaram2017/jaram-wiki

# Change directory into the cloned repository
$ cd jaram-wiki

# Create a virtualenv
$ virtualenv venv 

# activate the virtualenv
$ . venv/bin/activate

# Install the packages.
$ pip install -r requirements.txt

# Run Django Server
$ python manage.py migrate
$ python manage.py runserver
```
