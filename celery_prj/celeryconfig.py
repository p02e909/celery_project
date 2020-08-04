# celery parameter
BROKER_URL = 'pyamqp://'
CELERY_RESULT_BACKEND = 'rpc://'
CELERY_IMPORTS=("celery_prj.tasks",)
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# set period everyday
PERIOD = 24 * 60 * 60
# ref: https://docs.celeryproject.org/en/stable/reference/celery.schedules.html

CELERYBEAT_SCHEDULE = {
    'schedule_period': {
        'task': 'celery_prj.tasks.update_db',
        'schedule': PERIOD,
        'args': (),
    },
}

