#1.라이브러리 호출
import requests
from bs4 import BeautifulSoup as bs
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "teamProcject_modaco_SPF.settings")
import django
django.setup()

from stock.models import Kospicap
#from stock.models import Capitalzation


#2. 데이터 요청
dict = {}
data = []

    # 2.데이터 요청 단계
def capitalzation():
    for page in range(1, 36):
        req = requests.get(f"https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page={page}") #코스피

        # req = requests.get(f"https://finance.naver.com/sise/sise_market_sum.nhn?sosok=1&page={page}") #코스닥
        html = req.text
        soup = bs(html, "lxml")

        # 3. 데이터 추출(파싱)단계

        stockContents = soup.select("#contentarea > div.box_type_l > table.type_2 > tbody > tr")
        for sc in stockContents:
            try:
                stockRank = sc.select_one("td.no").text
                stockName = sc.select_one("td:nth-child(2) > a").text
                tmp=sc.select_one("td:nth-child(3)").text
                stockPrice = tmp.replace(",", "")
                tmp1=sc.select_one("td:nth-child(7)").text
                stockCap = tmp1.replace(",", "")  # market capitalization
                tmp2 = sc.select_one("td:nth-child(10)").text
                stockVolume = tmp2.replace(",", "")

                dict = {'stockRank': stockRank, 'stockName': stockName, 'stockPrice': stockPrice,
                        'stockCap': stockCap, 'stockVolume': stockVolume}

                data.append(dict)
            except AttributeError:  # None 은 그냥 넘어가
                continue

    return data

if __name__== '__main__':
    capitalzation_list = capitalzation()
    for d in capitalzation_list:
        Kospicap(stockRank=d['stockRank'], stockName=d['stockName'], stockPrice=d['stockPrice'], stockCap=d['stockCap'], stockVolume=d['stockVolume']).save()

        # Capitalzation(stockRank=d['stockRank'], stockName=d['stockName'], stockPrice=d['stockPrice'],
        #        stockCap=d['stockCap'], stockVolume=d['stockVolume']).save()
