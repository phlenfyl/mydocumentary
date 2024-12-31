from django.contrib import admin
from .models import Documentation
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

class DocumentationAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

admin.site.register(Documentation, DocumentationAdmin)

