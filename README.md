<p>Step to install and run:</p>
<p>clone project<br>
At celery_project/ folder:</p>

<p>install rabbitmq server (need for celery broker)<br>
$ sudo apt-get install rabbitmq-server</p>

<p>install virtualenv:<br>
$ python3 -m pip install virtualenv</p>

<p>create virtualenv, name env:<br>
$ virtualenv -p python3 env</p>

<p>active virtualenv:<br>
$ source env/bin/activate</p>

<p>install celery, sqlalchemy:<br>
$ pip install celery sqlalchemy</p>

<p>test calcular perimeter and area command:<br>
$ python3 -m unittest celery_prj.tests.test_calcular_rectangle -vvv</p>

<p>all test case in celery_prj/tests:<br>
"test_calcular_rectangle" is name of file test</p>

<p>run celery schedule update area and perimeter:<br>
$ celery -A celery_prj worker -B -c=1 --config=celeryconfig</p>

<p>setup time schedule in celery_prj/celeryconfig.py<br>
Default config is everyday (24h from the time run command)<br>
ref: https://docs.celeryproject.org/en/stable/reference/celery.schedules.html</p>
