from django.urls import path, include
from rest_framework import routers
from News.views import NewsViewSet

router = routers.DefaultRouter()
router.register('news', NewsViewSet)

urlpatterns = [
	path('', include(router.urls))
]