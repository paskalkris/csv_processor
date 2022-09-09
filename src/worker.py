from typing import Callable

from celery import Celery

from src import config


celery = Celery(__name__)
celery.config_from_object(config.get_settings(), namespace="CELERY")
celery.autodiscover_tasks()
