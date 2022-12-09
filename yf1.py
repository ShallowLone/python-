import requests 
from bs4 import BeautifulSoup 
import csv 
import pandas as pd 
import os
import datetime 
import time

class YahooFinanceHistory_60days:
  _url = 'https://hk.finance.yahoo.com/quote/{code}.HK/history?p={code}.HK'

  def get_data(self, code):
    url = _url.format(code = code)
    web = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15(KHTML, like Gecko) Version/14.1.2 Safari/605.1.15'})
    web.raise_for_status()
    soup = BeautifulSoup(web.text,"lxml")
    table = soup.find("div", {"id":"Main"}).find("table", {"History": "historical-prices"})
    data = []
    trs = table.find_all("tr")
    for tr in trs:
      cells = tr.find_all(["th", "td"])
      row = []
      for cell in cells:
        row.append(cell.text.strip("*", ""))
      data.append(row)
    
    df = pd.DataFrame(data[1:61], columns = data[0])
    df = df.set_index(keys="日期")
    
    return df
