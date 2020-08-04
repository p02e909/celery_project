from . import my_config


# celery parameter
BROKER_URL = 'pyamqp://'
CELERY_RESULT_BACKEND = 'rpc://'
CELERY_IMPORTS=("celery_prj.tasks",)
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

PERIOD = my_config.PERIOD

CELERYBEAT_SCHEDULE = {
    'schedule_period': {
        'task': 'celery_prj.tasks.update_db',
        'schedule': PERIOD,
        'args': (),
    },
}

