from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'subject')
    search_fields = ['email']

admin.site.register(Contact, ContactAdmin)
