# -*- coding: UTF-8 -*-
import requests
from requests_html import HTML
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QBrush, QColor

from datetime import datetime

import PTTArticle

def ptt_search(url, keyword, date_start):
    resp = fetch(url) # 取得網頁內容
    html = HTML( html = resp.text )
    print('[%s] 連線成功，開始搜尋目標「%s」\n' %(datetime.now(), keyword))

    url_last    = ''
    bool_exceed = False
    entry_list  = []
    while bool_exceed == False:
        if len(url_last) > 0:
            resp = fetch(url_last) # 取得網頁內容
            html = HTML( html = resp.text )
        url_last            = PTTArticle.parse_lastpage(html)
        post_entries        = PTTArticle.parse_entries(html) # 取得各列標題
        data_list, min_date = PTTArticle.filter_meta( post_entries, keyword)
        entry_list          = entry_list + data_list

        if date_start >= min_date:
            print(f'DateEnd = {date_start} >= {min_date}')
            bool_exceed = True

    return entry_list


def fetch(url):
    # 向 PTT 回答已經滿 18 歲，回傳網頁內容
    response = requests.get(url, cookies={'over18':'1'})
    return response


def showtable_Article( gui, df):
    keys  = list(df)
    table = gui.tableWidget
    table.setColumnCount(len(keys))
    table.setRowCount(len(df[keys[0]])+1)
    table.setColumnWidth(0,80)
    table.setColumnWidth(1,700)
    table.setColumnWidth(2,200)
    table.setColumnWidth(3,200)
    table.setColumnWidth(4,800)
    table.setHorizontalHeaderLabels(keys)
    
    df_key = list(df)
    df_array = df.values
    for i in range( 0, df.shape[0], 1):
        for j in range( 0, df.shape[1], 1):
            key_ = df_key[j]
            if key_ == '日期':
                value = df_array[i,j].strftime('%Y-%m-%d')
            else:
                value = str(df_array[i,j])
            item = QTableWidgetItem(value)
            if key_ in ['推文數','發文者','日期']:
                item.setTextAlignment(QtCore.Qt.AlignHCenter)
            elif key_ == '標題':
                item.setForeground(QBrush(QColor(0,0,255)))

            table.setItem( i, j, item)


