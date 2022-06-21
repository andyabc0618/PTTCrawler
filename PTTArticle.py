# -*- coding: UTF-8 -*-
import requests
from requests_html import HTML
from datetime import datetime

import Functions



def parse_lastpage(html):
    anchor = html.find("a",containing="‹ 上頁")[0]
    url    = list(anchor.links)
    url    = 'https://www.ptt.cc/'+url[0]

    return url

def parse_entries(html):
    # 傳入網頁內容，利用 requests_html 取出 div.r-ent 的元素內容並回傳'
    post_entries = html.find('div.r-ent')

    return post_entries


def filter_meta( entryies, keyword):
    data_list = []
    for entry in entryies:
        meta = parse_meta(entry)
        if keyword in meta['title'].lower() :
            print(meta['title'])
            data_list.append(meta)
    
    min_date = datetime.now()
    for i in range( 0, len(data_list), 1):
        date     = data_list[i]['date']
        min_date = min( min_date, date)


    return data_list, min_date


def parse_meta(entry):
    meta = {
        'title': entry.find('div.title', first=True).text,
        'push' : entry.find('div.nrec', first=True).text,
        'date' : entry.find('div.date', first=True).text
    }
    meta['date'] = datetime.strptime(meta['date'],'%m/%d')
    meta['date'] = Functions.date_compare(meta['date'])
    try:
        meta['author'] = entry.find('div.author', first=True).text
        meta['link'] = 'https://www.ptt.cc/'+entry.find('div.title > a', first=True).attrs['href']
    except AttributeError:
        meta['author'] = '[Deleted]'
        meta['link'] = '[Deleted]'

    return meta


