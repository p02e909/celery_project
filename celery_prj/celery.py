from celery import Celery
from . import celeryconfig


app = Celery()
app.config_from_object(celeryconfig)

