from app.portafolio.models import Project, Item
from django.contrib import admin

class ProjectAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'description', 'extra', 'status', 'weight', 'date_created')
	search_fields = ['title', 'slug', 'slug', 'description', 'extra']
	list_filter = ['status', 'weight', 'date_created']
	prepopulated_fields = {"slug": ("title",)}


class ItemAdmin(admin.ModelAdmin):
	list_display = ('id', 'image', 'title', 'project', 'weight',)
	list_filter = ['project', 'weight']


admin.site.register(Project, ProjectAdmin)
admin.site.register(Item, ItemAdmin)

