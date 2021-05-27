import json
import requests
from bs4 import BeautifulSoup

result = []

def crawl(url):
    data = requests.get(url)
    return data.content

def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    box_type_m = bsObj.find("div", {"class":"box_type_m"})
    type_1 = box_type_m.find("table", {"class":"type_1"})
    trs = type_1.findAll("tr")
    dayIndexs = []
    for tr in trs:
        try:
            dayIndex = getDayIndex(tr)
            dayIndexs.append(dayIndex)
        except Exception as e:
            print("error")
            pass
    return dayIndexs

def getDayIndex(tr):
    tds = tr.findAll("td")
    date = tds[0].text
    index = tds[1].text
    volume = tds[4].text
    payTrade = tds[5].text
    return {"date":date, "index":index, "volume":volume, "payTrade":payTrade}

def getKospi(page):
    url = "https://finance.naver.com/sise/sise_index_day.nhn?code=KOSPI&page={}".format(page)
    pageString = crawl(url)
    list = parse(pageString)
    return list

def getKosdaq(page):
    url = "https://finance.naver.com/sise/sise_index_day.nhn?code=KOSDAQ&page={}".format(page)
    pageString = crawl(url)
    list = parse(pageString)
    return list

def getFut(page):
    url = "https://finance.naver.com/sise/sise_index_day.nhn?code=FUT&page={}".format(page)
    pageString = crawl(url)
    list = parse(pageString)
    return list

def getKpi200(page):
    url = "https://finance.naver.com/sise/sise_index_day.nhn?code=KPI200&page={}".format(page)
    pageString = crawl(url)
    list = parse(pageString)
    return list
'''
코스피200 편입종목 상위 순
https://finance.naver.com/sise/entryJongmok.nhn?&page=1
'''
    
for page in range(1, 3 +1):
    list = getKospi(page)
    result += list

file = open("./kospi.json", "w+")
file.write(json.dumps(result))
