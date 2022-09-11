from django.contrib import admin
from .models import Contact, Project1, Project2, Project3, Project4

class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'subject')
    search_fields = ['email']

class Project1Admin(admin.ModelAdmin):
    list_display = ('category', 'description', 'project_image', 'order')
    search_fields = ('category', 'description')

class Project2Admin(admin.ModelAdmin):
    list_display = ('category', 'description', 'project_image', 'order')
    search_fields = ('category', 'description')

class Project3Admin(admin.ModelAdmin):
    list_display = ('category', 'description', 'project_image', 'order')
    search_fields = ('title', 'description')

class Project4Admin(admin.ModelAdmin):
    list_display = ('category', 'description', 'project_image', 'order')
    search_fields = ('category', 'description')

admin.site.register(Project1, Project1Admin)
admin.site.register(Project2, Project2Admin)
admin.site.register(Project3, Project3Admin)
admin.site.register(Project4, Project4Admin)
admin.site.register(Contact, ContactAdmin)
