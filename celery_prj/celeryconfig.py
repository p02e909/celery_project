from . import my_config


# celery parameter
BROKER_URL = 'pyamqp://'
CELERY_RESULT_BACKEND = 'rpc://'
CELERY_IMPORTS=("celery_prj.tasks",)
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

