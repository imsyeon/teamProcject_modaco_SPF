from django.urls import path
from . import views

app_name='stock'

urlpatterns = [

    path('', views.KospiList.as_view(), name='kospi'),
    path('kosdaq/', views.KosdaqList.as_view(), name='kosdaq'),
    path('report/', views.ReportList.as_view(), name='report'),
    path('capitalzation/', views.CapitalzationList.as_view(), name='capitalzation'),
    path('kospicap/', views.KospicapList.as_view(), name='kospicap'),


]