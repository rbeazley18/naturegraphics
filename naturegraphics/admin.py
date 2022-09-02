from django.contrib import admin
from .models import Contact, Project

class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'subject')
    search_fields = ['email']

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'project_image', 'order')
    search_fields = ('title', 'description')

admin.site.register(Project, ProjectAdmin)
admin.site.register(Contact, ContactAdmin)
