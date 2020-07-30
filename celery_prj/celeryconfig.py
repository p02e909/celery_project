# CELERY
BROKER_URL = 'pyamqp://'
CELERY_RESULT_BACKEND = 'rpc://'
CELERY_IMPORTS=("celery_prj.tasks",)
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
# CELERY_TIMEZONE = 'US/Eastern'
# app.conf.timezone = 'UTC'

CELERYBEAT_SCHEDULE = {
    'every-half-minute': {
        'task': 'celery_prj.tasks.update_db',
        'schedule': 5.0, # schedule for 5s
        'args': (),
    },
}

