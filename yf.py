import requests 
from bs4 import BeautifulSoup 
import csv 
import pandas as pd 
import urllib
from io import StringIO
import os


class YahooFinanceHistory_60days:
  _url = 'https://hk.finance.yahoo.com/quote/%s.HK/history?p=%s.HK'
  
    
    
    
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
