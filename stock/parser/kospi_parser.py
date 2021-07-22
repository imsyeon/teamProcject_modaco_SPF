#1.라이브러리 호출
from datetime import datetime

import requests
from bs4 import BeautifulSoup as bs
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "teamProcject_modaco_SPF.settings")
import django
django.setup()
from stock.models import KospiData


#2. 데이터 요청
dict = {}
data = []
def kospi():
    for page in range(1, 30):
        req = requests.get(f"https://finance.naver.com/sise/sise_index_day.nhn?code=KOSPI&page={page}")
        html = req.text
        soup = bs(html, "lxml")


    # 3. 데이터 추출(파싱)단계
        kospiContents = soup.select("body > div > table.type_1 > tr")
        for kc in kospiContents:
            try:
                # tmp= kc.select_one("td.date").text
                # dict['kospiDate'] = datetime.strptime(tmp, '%Y.%m.%d').strftime('%Y-%m-%d')
                kospiDate = kc.select_one("td.date").text
                tem2=kc.select_one("td:nth-child(2)").text
                kospiConclusion = tem2.replace(",", "")
                tem3=kc.select_one("td:nth-child(5)").text
                kospiVolume=tem3.replace(",", "")
                tem4=kc.select_one("td:nth-child(6)").text
                kospiTradeValue=tem4.replace(",", "")

                dict = {'kospiDate': kospiDate, 'kospiConclusion': kospiConclusion, 'kospiVolume': kospiVolume,
                        'kospiTradeValue': kospiTradeValue}

                data.append(dict)

            except AttributeError:  # None 은 그냥 넘어가
                continue
    return data

if __name__== '__main__':
     kospi_data_list = kospi()
     for d in kospi_data_list:
         KospiData(kospi_date=d['kospiDate'], conclusion=d['kospiConclusion'], volume=d['kospiVolume'], trade_value=d['kospiTradeValue']).save()


