from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogData


def index(request):
    '''
    news 리스트 출력
    '''
    news_list = BlogData.objects.all()
    context = {'news_list': news_list }
    return render(request,'news/news_list.html', context)
