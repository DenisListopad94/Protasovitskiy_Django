import os
from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self, *args, **kwargs):
    print(f'Request: {self.request!r}')


app.conf.beat_schedule = {
    'task_every_3m40s': {
        'task': 'booking_app.tasks.task_every_3m40s',
        'schedule': 220,  # 3 minutes and 40 seconds
    },
    'task_three_times_hourly': {
        'task': 'booking_app.tasks.task_three_times_hourly',
        'schedule': crontab(minute=0, hour='19-21'),
        'options': {'max_retries': 3},
    },
}
