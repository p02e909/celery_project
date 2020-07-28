from celery import Celery
from . import celeryconfig


app = Celery(
    "celery_prj",
    # broker="amqp://",
    include=['celery_prj.tasks']
)
app.config_from_object(celeryconfig)


if __name__=="__main__":
    app.start()

