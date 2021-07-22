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

    req = requests.get('https://finance.naver.com/news/news_list.nhn?mode=LSS2D&section_id=101&section_id2=258')
    ## HTML 소스 가져오기
    html = req.text
    soup = BeautifulSoup(html,'html.parser')
    my_titles =  soup.select(
        'dd > a'
    )

    data = {}

    ## my_titles는 list 객체
    for title in my_titles:
        data[title.text] = title.get('href').replace('§','&sect')

    return data

if __name__ == '__main__':
    news_data_dict = news()
    for t, l in news_data_dict.items():
        NewsData(title = t, link = l).save()