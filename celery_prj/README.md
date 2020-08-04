install rabbitmq server (need for celery broker)
$ sudo apt-get install rabbitmq-server

install virtualenv:
$ python3 -m pip install virtualenv

create virtualenv, name env:
$ virtualenv -p python3 env

active virtualenv:
$ source env/bin/activate

install celery, sqlalchemy:
$ pip install celery sqlalchemy

test calcular perimeter and area command:
$ python3 -m unittest celery_prj.tests.test_calcular_rectangle -vvv

all test case in celery_prj/tests:
"test_calcular_rectangle" is name of file test

run celery schedule update area and perimeter:
$ celery -A celery_prj worker -B -c=1 --config=celeryconfig

setup time schedule in celery_prj/celeryconfig.py
default config is everyday
ref: https://docs.celeryproject.org/en/stable/reference/celery.schedules.html
