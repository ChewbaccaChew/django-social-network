from django.contrib import admin
from .models import Discussion


# admin.site.register(Discussion)
@admin.register(Discussion)
class DiscussionAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_created', 'date_updated', 'author']
    prepopulated_fields = {'slug': ('title',)}
