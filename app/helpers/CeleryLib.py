from celery import Celery
from app.config.config import Config
import os

def make_celery(app):
    test1 = "{}".format(os.environ.get('CELERY_BACKEND_URL'))
    test2 = "{}".format(os.environ.get('CELERY_BROKER_URL'))
    celery = Celery(app.import_name, backend="redis://localhost:6379/0",
                    broker="redis://localhost:6379/0")
    celery.conf.update(Config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery