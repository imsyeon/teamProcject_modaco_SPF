#1.라이브러리 호출
import requests
from bs4 import BeautifulSoup as bs
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "teamProcject_modaco_SPF.settings")
import django
django.setup()
from stock.models import Report

data=[]
dict={}
#2. 데이터 요청
def report():
    for page in range(1, 3):
        req = requests.get(f"https://finance.naver.com/research/company_list.nhn?&page={page}")
        html = req.text
        soup = bs(html, "lxml")

    #3.데이터 파싱
        reportContents = soup.select("#contentarea_left > div.box_type_m > table.type_1 > tr")
        for rc in reportContents:
            try:
                reportStock = rc.select_one("td:nth-child(1) > a").text
                reportTitle = rc.select_one("td:nth-child(2) > a").text
                reportPublisher = rc.select_one("td:nth-child(3)").text
                reportDate = rc.select_one("td:nth-child(5)").text
                reportLink = rc.select_one("td.file > a")["href"]
                # print(reportStock, reportTitle, reportPublisher, reportDate, reportLink)

                dict = {'reportStock': reportStock, 'reportTitle': reportTitle, 'reportPublisher': reportPublisher,
                        'reportDate': reportDate, 'reportLink':reportLink}

                data.append(dict)

            except AttributeError:
                continue

    return data

if __name__== '__main__':
    report_list=report()
    for d in report_list:
        Report(report_stock=d['reportStock'], report_title=d['reportTitle'], report_publisher=d['reportPublisher'], report_date=d['reportDate'], report_link=d['reportLink']).save()
