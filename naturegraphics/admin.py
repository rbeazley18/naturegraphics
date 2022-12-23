from django.contrib import admin
from .models import Contact, Portfolio, Gallery, Project1, Project2, Project3, Project4

class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'subject')
    search_fields = ['email']

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'portfolio_image', 'order')
    search_fields = ('description',)

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('alt_tag', 'gallery_image', 'order')
    search_fields = ('title',)

class Project1Admin(admin.ModelAdmin):
    list_display = ('category', 'alt_tag', 'project_image', 'order')
    search_fields = ('category', 'alt_tag')

class Project2Admin(admin.ModelAdmin):
    list_display = ('category', 'alt_tag', 'project_image', 'order')
    search_fields = ('category', 'alt_tag')

class Project3Admin(admin.ModelAdmin):
    list_display = ('category', 'alt_tag', 'project_image', 'order')
    search_fields = ('title', 'alt_tag')

class Project4Admin(admin.ModelAdmin):
    list_display = ('category', 'alt_tag', 'project_image', 'order')
    search_fields = ('category', 'alt_tag')

admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Project1, Project1Admin)
admin.site.register(Project2, Project2Admin)
admin.site.register(Project3, Project3Admin)
admin.site.register(Project4, Project4Admin)
admin.site.register(Contact, ContactAdmin)
