from django.urls import path
from . import views

app_name = 'news_data'
urlpatterns = [

    path('', views.news, name='news'),
]