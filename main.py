# -*- coding: UTF-8 -*-
from datetime import datetime
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys

import PTT
import Functions
import GUI

class MainWindow( QMainWindow, GUI.Ui_MainWindow):
    def __init__(self):
        super().__init__() 
        self.setupUi(self) # Ui_MainWindow.setupUi()

        self.lineEdit_itemname.setText('momo')
        self.lineEdit_year.setText('2022')
        self.lineEdit_month.setText('01')
        self.lineEdit_day.setText('01')

        self.pushButton_search.clicked.connect(self.search)

    def search(self):
        keyword = self.lineEdit_itemname.text() 
        if len(keyword) > 0:
            year_  = self.lineEdit_year.text()
            month_ = self.lineEdit_month.text()
            day_   = self.lineEdit_day.text()
            date_start = f'{year_}/{month_}/{day_}'
            date_start = datetime.strptime( date_start, '%Y/%m/%d')

            base_url = 'https://www.ptt.cc/bbs/Lifeismoney/index.html'
            entry_list = PTT.ptt_search( base_url, keyword, date_start)

            if len(entry_list) == 0:
                QMessageBox.information(None, '訊息', '查無相關資料!')
            else:
                attributes = {'push':'推文數','title':'標題','author':'發文者','date':'日期','link':'網址'}
                df = Functions.dictlist_to_dataframe( entry_list, attributes)
                PTT.showtable_Article( self, df)




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv) 
    window = MainWindow() 
    window.show()
    app.exec_() # GUI keep showing

    # URL        = 'https://www.ptt.cc/bbs/Lifeismoney/index.html'
    # KEYWORD    = 'momo'
    # date_start = '2021/11/01'
    # date_end   = '2022/01/11'
    # date_start = datetime.strptime( date_start, '%Y/%m/%d')
    # date_end   = datetime.strptime( date_end, '%Y/%m/%d')
    # PTT.ptt_alert(URL, KEYWORD, date_start) # 開始執行


    # try:
            
    # except Exception as e:
    #     print('[%s] 執行期間錯誤：%s' %(datetime.now(), e))