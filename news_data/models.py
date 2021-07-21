from django.db import models

class NewsData(models.Model):
    title = models.CharField(max_length=200,unique=True)
    link = models.URLField(unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.pk}'