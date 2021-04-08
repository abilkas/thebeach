from thebeach.celery import app
from celery import shared_task
from .models import News

@shared_task
def create_news():
	news = News.objects.create(title="Lorem", content="xxx")
	print("heelo")