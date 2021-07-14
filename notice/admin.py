from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Notice
# Register your models here.

admin.site.register(Notice, MarkdownxModelAdmin)