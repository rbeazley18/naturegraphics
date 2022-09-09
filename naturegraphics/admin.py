from django.contrib import admin
from .models import Contact, Project, Category

class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'subject')
    search_fields = ['email']

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('category', 'description', 'project_image', 'order')
    search_fields = ('category', 'description')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category_description')

admin.site.register(Project, ProjectAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Category, CategoryAdmin)
