import requests
from bs4 import BeautifulSoup
import json
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "teamProcject_modaco_SPF.settings")
import django
django.setup()
from news_data.models import NewsData

#python파일 위치
#BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def news():

    req = requests.get('https://cc.naver.com/cc?a=new.main&r=&i=&bw=1085&px=112&py=298&sx=112&sy=298&m=1&nsc=finance.news&u=https%3A%2F%2Ffinance.naver.com%2Fnews%2Fmainnews.nhn')
    ## HTML 소스 가져오기
    html = req.text
    soup = BeautifulSoup(html,'html.parser')
    my_titles =  soup.select(
        'dd > a'
    )

    data = {}

    ## my_titles는 list 객체
    for title in my_titles:
        data[title.text] = title.get('href')

    return data

if __name__ == '__main__':
    news_data_dict = news()
    for t, l in news_data_dict.items():
        NewsData(title = t, link = l).save()