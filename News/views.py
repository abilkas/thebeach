from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from News.serializers import NewsSerializer
from News.models import News

class NewsViewSet(ModelViewSet):
	serializer_class = NewsSerializer
	queryset = News.objects.all()

	