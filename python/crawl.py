import json
import requests
import telepot
from bs4 import BeautifulSoup

result = []

# KOSPI 마지막 페이지 가져오기
def getLastPage():
    url = "https://finance.naver.com/sise/sise_index_day.nhn?code=KOSPI&page=1"
    data = requests.get(url)
    bsObj = BeautifulSoup(data.content, "html.parser")
    box_type_m = bsObj.find("div", {"class":"box_type_m"})
    pgRR = box_type_m.find("td", {"class":"pgRR"})
    lastLink = pgRR.a.attrs['href']
    lastPage = lastLink[41:len(lastLink)]
    return lastPage

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
    
lastPage = getLastPage()
    
for page in range(1, int(lastPage) +1):
    list = getKospi(page)
    result += list

file = open("./kospi.json", "w+")
file.write(json.dumps(result))
