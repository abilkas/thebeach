import os
from celery import Celery 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'thebeach.settings')

app = Celery('thebeach')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
	print('Request: {0!r}'.format(self.request))

app.conf.beat_schedule = {
	'create_random_news': {
	'task': 'News.tasks.create_news',
	'schedule': 2.0,
	},
}