from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/',views.QuestionDetail.as_view()),
    path('', views.QuestionList.as_view()),

]