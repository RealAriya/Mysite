from django.contrib import admin
from website.models import Contact,Newsletter

# @admin.register(Contact)

class ContactAdmin(admin.ModelAdmin):
    list_display = ['subject','name','email','created_date','updated_date']
    list_filter = ('subject',)

# Register your models here.

admin.site.register(Contact,ContactAdmin)
admin.site.register(Newsletter)