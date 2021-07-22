from django.urls import path
from . import views

app_name = 'index'
urlpatterns = [

    path('', views.landing),
    path('analysis/', views.analysis),
    path('kakao2019_02/', views.kakao2019_02, name='kakao2019_02'),
    path('kakao2020_01/', views.kakao2020_01, name='kakao2020_01'),
    path('kakao2020_07/', views.kakao2020_07, name='kakao2020_07'),
    path('kakao2021_01/', views.kakao2021_01, name='kakao2021_01'),
    path('kakao2021_03/', views.kakao2021_03, name='kakao2021_03'),
    path('lg2019_02/', views.lg2019_02, name='lg2019_02'),
    path('lg2020_01/', views.lg2020_01, name='lg2020_01'),
    path('lg2020_07/', views.lg2020_07, name='lg2020_07'),
    path('lg2021_01/', views.lg2021_01, name='lg2021_01'),
    path('lg2021_03/', views.lg2021_03, name='lg2021_03'),
    path('samsung2019_02/', views.samsung2019_02, name='samsung2019_02'),
    path('samsung2020_01/', views.samsung2020_01, name='samsung2020_01'),
    path('samsung2020_07/', views.samsung2020_07, name='samsung2020_07'),
    path('samsung2021_01/', views.samsung2021_01, name='samsung2021_01'),
    path('samsung2021_03/', views.samsung2021_03, name='samsung2021_03'),
    path('sk2019_02/', views.sk2019_02, name='sk2019_02'),
    path('sk2020_01/', views.sk2020_01, name='sk2020_01'),
    path('sk2020_07/', views.sk2020_07, name='sk2020_07'),
    path('sk2021_01/', views.sk2021_01, name='sk2021_01'),
    path('sk2021_03/', views.sk2021_03, name='sk2021_03'),
    path('hyundai2019_02/', views.hyundai2019_02, name='hyundai2019_02'),
    path('hyundai2020_01/', views.hyundai2020_01, name='hyundai2020_01'),
    path('hyundai2020_07/', views.hyundai2020_07, name='hyundai2020_07'),
    path('hyundai2021_01/', views.hyundai2021_01, name='hyundai2021_01'),
    path('hyundai2021_03/', views.hyundai2021_03, name='hyundai2021_03'),

]