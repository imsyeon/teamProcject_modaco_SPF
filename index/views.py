from django.shortcuts import render
from news_data.models import NewsData

# Create your views here.

def landing(request):
    recent_news = NewsData.objects.order_by('-pk')[:3]

    return render(
        request,
        'index/landing.html',
        {
            'recent_news': recent_news,
        }
    )