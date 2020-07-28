install rabbitmq server (need for celery broker)
$ sudo apt-get install rabbitmq-server

install virtualenv:
$ python3 -m pip install virtualenv

make retangle virtualenv, name env:
$ virtualenv -p python3 env

active virtualenv:
$ source env/bin/activate

install celery, sqlalchemy:
$ pip install celery sqlalchemy

