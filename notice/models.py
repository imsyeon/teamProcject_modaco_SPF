from django.db import models
from django.contrib.auth.models import User
from markdown import markdown
from markdownx.models import MarkdownxField
import os

# Create your models here.



class Notice(models.Model):
    subject = models.CharField(max_length=200)
    content = MarkdownxField()

    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    head_image = models.ImageField(upload_to='notice/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='notice/files/%Y/%m/%d/', blank=True)

    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]

    def get_content_markdown(self):
        return markdown(self.content)

    def __str__(self):
            return f'[{self.pk}]{self.subject} :: {self.author}'

    def get_absolute_url(self):
        return f'/notice/{self.pk}/'


