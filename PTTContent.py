# -*- coding: UTF-8 -*-
import requests
from requests_html import HTML
from bs4 import BeautifulSoup


def content_search(url):
    resp = fetch(url) # 取得網頁內容
    soup = BeautifulSoup(resp.text, 'lxml')


    print(soup.prettify())


def fetch(url):
    # 傳入網址，向 PTT 回答已經滿 18 歲，回傳網頁內容
    response = requests.get(url, cookies={'over18':'1'})
    return response


url = 'https://www.ptt.cc/bbs/Gossiping/M.1640891667.A.86A.html'
content_search(url)