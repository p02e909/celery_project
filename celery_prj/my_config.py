"""
This file include user config
"""


DB_PATH = "sqlite:///rectangle.db" # replace this path to your db

# config PERIOD
# ref: https://docs.celeryproject.org/en/stable/reference/celery.schedules.html
# PERIOD = 24 * 60 * 60 # config for 24h from start run
PERIOD = 5 # config 5s from start run

