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

<p>test calcular perimeter and area command (move to folder celery_project):<br>
$ python3 -m unittest celery_prj.tests.test_calcular_rectangle -vvv</p>

<p>all test case in celery_prj/tests:<br>
"test_calcular_rectangle" is name of file test</p>

<p>run celery schedule update area and perimeter:<br>
$ celery -A celery_prj worker -B -c=1 --config=celeryconfig</p>

<p>ex:<br>
$ cd celery_project<br>
$ source env/bin/activate<br>
$ python<br>
>>> from celery_prj import tasks<br>
>>> tasks.query_rectangle(5)<br>
{'a': 5, 'b': 5, 'perimeter': 20, 'area': 25}<br>
>>> tasks.update_db.delay(5)<br>
<AsyncResult: 55f88bea-1e1d-4de6-a8fd-7e6f40ebc3c3><br>
>>> tasks.update_db.delay(5).get()<br>
'not update'<br>
>>> tasks.query_rectangle(6)<br>
{'a': 6, 'b': 6, 'perimeter': 2224, 'area': 36}<br>
>>> tasks.update_db.delay(6).get()<br>
'updated'<br>
>>> tasks.query_rectangle(6)<br>
{'a': 6, 'b': 6, 'perimeter': 24, 'area': 36}<br>
>>> tasks.query_rectangle(7)<br>
{'a': 7, 'b': 7, 'perimeter': 28, 'area': 49}<br>
>>> tasks.update_db.delay(7).get()<br>
'not update'<br>
>>> tasks.query_rectangle(7)<br>
{'a': 7, 'b': 7, 'perimeter': 28, 'area': 49}<br>
>>> tasks.query_rectangle(8)<br>
{'a': 8, 'b': 8, 'perimeter': 32, 'area': 64}<br>
>>> tasks.query_rectangle(9)<br>
{'a': 9, 'b': 9, 'perimeter': 36, 'area': 81}<br>
>>> tasks.query_rectangle(11)<br>
>>> tasks.update_db.delay(11).get()<br>
celery_prj.my_exception.WrongInput: wrong input!<br>
</p>
