from django.db import models

class News(models.Model):
	title = models.CharField("Название", max_length=256)
	content = models.TextField("Контент")
	created_at = models.DateTimeField(auto_now_add=True)