# import requests
# from bs4 import BeautifulSoup
# req = requests.get("http://www.hani.co.kr/arti/politics/home01.html")
# html=req.text
# soup = BeautifulSoup(html, 'html.parser')
# # my_list =soup.select('div.list')
# # print(my_list)
# print(soup.get_text().encode('utf-8').decode('utf-8'))
import requests
from bs4 import BeautifulSoup
import json
import os
import chardet

#script의 인코딩 문제 수정
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
##################

# python파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


#파이썬 인코딩 해결
from bs4.dammit import EncodingDetector
url ='http://www.hani.co.kr/arti/politics/home01.html'
resp = requests.get(url)
http_encoding = resp.encoding if 'charset' in resp.headers.get('content-type', '').lower() else None
html_encoding = EncodingDetector.find_declared_encoding(resp.content, is_html=True)
encoding = html_encoding or http_encoding
soup = BeautifulSoup(resp.content, 'lxml', from_encoding=encoding)
##########
a=soup.find(class_="section-list-area").find_all(class_="list")
for article in a:
    print(article.find("h4").get_text())
    print(article.find("p").find("a").get_text())
    print(article.find("p").find("span").get_text())
    photo = article.find(class_="article-photo").find("img")
    if photo is None:
        pass
    else:
        print(photo.get("src"))
#시간 파싱 쉽게 하는것 찾기
#Print를 정식 변수명으로
#Mysql 설치 및 Mysql 파이썬 연동법 찾기

    # print(get("src"))
# print(a)
#
# for i in a:
#     x=i.find("h4").a
#     print(x)
