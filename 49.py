import requests
from bs4 import BeautifulSoup
import pymysql
import re

url = "http://www.qzrc.com/area.aspx?pn=220&a=350500&p=1"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64); AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
    'host': 'www.qzrc.com'
    }
for i in range(5):
    print("\nthis is "+ str(i+1)+ " pages")
    i = str(i)
    r = requests.get(url+i, headers = headers)
    soup = BeautifulSoup(r.text, 'lxml')
    souplist = soup.find_all(href = re.compile("CompanyDetail"))
    for x in souplist:
        href = x['href']
        print(href)
        companyname = x.string.strip()
        print(companyname)


