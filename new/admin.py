from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import New, Comment

@admin.register(New)
class NewAdmin(SummernoteModelAdmin):
    pass
admin.site.register(Comment)