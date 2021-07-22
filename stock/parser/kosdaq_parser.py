#1.라이브러리 호출
from datetime import datetime

import requests
from bs4 import BeautifulSoup as bs
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "teamProcject_modaco_SPF.settings")
import django
django.setup()
from stock.models import Kosdaq


#2. 데이터 요청
dict = {}
data = []
def kosdaq():
    for page in range(1, 30):
        req = requests.get(f"https://finance.naver.com/sise/sise_index_day.nhn?code=KOSDAQ&page={page}")
        html = req.text
        soup = bs(html, "lxml")


    # 3. 데이터 추출(파싱)단계
        kosdaqContents = soup.select("body > div > table.type_1 > tr")
        for kc in kosdaqContents:
            try:

                kosdaqDate = kc.select_one("td.date").text
                tem2=kc.select_one("td:nth-child(2)").text
                kosdaqConclusion = tem2.replace(",", "")
                tem3=kc.select_one("td:nth-child(5)").text
                kosdaqVolume=tem3.replace(",", "")
                tem4=kc.select_one("td:nth-child(6)").text
                kosdaqTradeValue=tem4.replace(",", "")

                dict = {'kosdaqDate': kosdaqDate, 'kosdaqConclusion': kosdaqConclusion, 'kosdaqVolume': kosdaqVolume,
                        'kosdaqTradeValue': kosdaqTradeValue}

                data.append(dict)

            except AttributeError:  # None 은 그냥 넘어가
                continue
    return data

# kosdaq_data_list = kosdaq()
# for d in kosdaq_data_list:
#     print(d['kosdaqDate'], d['kosdaqConclusion'], d['kosdaqVolume'], d['kosdaqTradeValue'])

if __name__== '__main__':
     kosdaq_data_list = kosdaq()
     for d in kosdaq_data_list:
         Kosdaq(kosdaq_date=d['kosdaqDate'], conclusion=d['kosdaqConclusion'], volume=d['kosdaqVolume'], trade_value=d['kosdaqTradeValue']).save()


