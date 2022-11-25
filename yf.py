import requests 
from bs4 import BeautifulSoup 
import csv 
import pandas as pd 


class YahooFinanceHistory_60days:
  _url = 'https://hk.finance.yahoo.com/quote/{code}.HK/history?p={}.HK'
  
  def get_data(self, code):
    
