import json
import requests
import telepot
from bs4 import BeautifulSoup

result = []

def getKospi():
    url = "https://finance.naver.com/sise/sise_index_day.nhn?code=KOSPI&page=1"
    data = requests.get(url)
    bsObj = BeautifulSoup(data.content, "html.parser")
    box_type_m = bsObj.find("div", {"class":"box_type_m"})
    type_1 = box_type_m.find("table", {"class":"type_1"})
    trs = type_1.findAll("tr")
    day_row = tds = trs[2].findAll("td")
    date = day_row[0].text
    index = day_row[1].text
    point_updn = day_row[2].text
    rate_updn = day_row[3].textt
    trde_qty = day_row[4].textt
    trde_amt = day_row[5].text
    
    print(date)
    print(index)
    print(point_updn)
    print(rate_updn)
    print(trde_qty)
    print(trde_amt)
    return 1

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

  
getKospi()
