from django.contrib import admin
from .models import post

@admin.register(post)

class postAdmin(admin.ModelAdmin):
    pass

# admin.site.register(post,postAdmin)