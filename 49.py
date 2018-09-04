from urllib.request import urlopen
from bs4 import BeautifulSoup


x = "http://www.qzrc.com/area.aspx?pn=220&a=350500&p="
for i in range(51):
    i = str(i)
    html = urlopen(x+i)
    bsObj = BeautifulSoup(html, 'lxml')
    address = bsObj.findAll("a", {"class":{"cymc"}})
    for i in address:
        print(i)

