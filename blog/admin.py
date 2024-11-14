from django.contrib import admin
from blog.models import post,Category
from django_summernote.admin import SummernoteModelAdmin
from blog.models import post

# @admin.register(post)

class postAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = "-empty-"
    list_display = ['title','author','counted_view','status','published_date','created_date']
    list_filter = ('status','counted_view')
    # ordering = ["created_date"]  # we can put mines behind the name to get reverse output ["-created_date"]
    search_fields = ["title",'content']
    summernote_fields = ('content',)


admin.site.register(post,postAdmin)
admin.site.register(Category)