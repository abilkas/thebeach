from django.contrib import admin
from News.models import News
# Register your models here.

class NewsAdmin(admin.ModelAdmin):
	list_display = ('title', 'created_at')
	list_filter = ('title', 'created_at')
	#prepopulated_fields = {'slug': ('title', )}

admin.site.register(News, NewsAdmin)