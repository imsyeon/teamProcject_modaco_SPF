from django.shortcuts import render
from news_data.models import NewsData

# Create your views here.

def landing(request):
    recent_news = NewsData.objects.order_by('-title')[:3]

    return render(
        request,
        'index/landing.html',
        {
            'recent_news': recent_news,
        }
    )

def analysis(request):
    return render(
        request,
        'index/analysis.html',
    )

def kakao2019_02(request):
    return render(request,
                  'index/kakao/kakao2019_02~_project.html', )
def kakao2020_01(request):
    return render(request,
                  'index/kakao/kakao2020_01~_project.html', )

def kakao2020_07(request):
    return render( request,
                   'index/kakao/kakao2020_07~_project.html',)

def kakao2021_01(request):
    return render(request,
                  'index/kakao/kakao2021_01~_project.html', )

def kakao2021_03(request):
    return render(request,
                  'index/kakao/kakao2021_03~_project.html', )

def lg2019_02(request):
    return render(request,
                  'index/lg/lg2019_02~_project.html', )

def lg2020_01(request):
    return render(request,
                  'index/lg/lg2020_01~_project.html', )

def lg2020_07(request):
    return render(request,
                  'index/lg/lg2020_07~_project.html', )

def lg2021_01(request):
    return render(request,
                  'index/lg/lg2021_01~_project.html', )

def lg2021_03(request):
    return render(request,
                  'index/lg/lg2021_03~_project.html', )


def samsung2019_02(request):
    return render(request,
                  'index/samsung/samsung2019_02~_project.html', )

def samsung2020_01(request):
    return render(request,
                  'index/samsung/samsung2020_01~_project.html', )


def samsung2020_07(request):
    return render(request,
                  'index/samsung/samsung2020_07~_project.html', )

def samsung2021_01(request):
    return render(request,
                  'index/samsung/samsung2021_01~_project.html', )

def samsung2021_03(request):
    return render(request,
                  'index/samsung/samsung2021_03~_project.html', )

def sk2019_02(request):
    return render(request,
                  'index/sk/sk2019_02~_project.html', )

def sk2020_01(request):
    return render(request,
                  'index/sk/sk2020_01~_project.html', )

def sk2020_07(request):
    return render(request,
                  'index/sk/sk2020_07~_project.html', )

def sk2021_01(request):
    return render(request,
                  'index/sk/sk2021_01~_project.html', )

def sk2021_03(request):
    return render(request,
                  'index/sk/sk2021_03~_project.html', )

def hyundai2019_02(request):
    return render(request,
                  'index/hyundai/hyundai2019_02~_project.html', )

def hyundai2020_01(request):
    return render(request,
                  'index/hyundai/hyundai2020_01~_project.html', )

def hyundai2020_07(request):
    return render(request,
                  'index/hyundai/hyundai2020_07~_project.html', )

def hyundai2021_01(request):
    return render(request,
                  'index/hyundai/hyundai2021_01~_project.html', )

def hyundai2021_03(request):
    return render(request,
                  'index/hyundai/hyundai2021_03~_project.html', )

