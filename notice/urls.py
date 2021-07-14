from django.urls import path
from . import views

urlpatterns = [
    path('update_notice/<int:pk>/', views.NoticeUpdate.as_view()),
    path('create_post/', views.NoticeCreate.as_view()),
    path('<int:pk>/',views.NoticeDetail.as_view()),
    path('', views.NoticeList.as_view()),
]