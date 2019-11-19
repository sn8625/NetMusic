#!/usr/bin/env python
# coding:utf-8

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication
from PyQt5.Qt import *
import download
import sys
import os
import traceback
import GetMusic
import time
import threading

class NetMusicUI(download.Ui_DownloadMusic):
    def __init__(self, DownloadMusic):
        super(download.Ui_DownloadMusic,self).__init__()
        super().setupUi(DownloadMusic)
        super().retranslateUi(DownloadMusic)
        self.cwd = os.getcwd()
        self.loopNum = True

        self.btn_export_dir.clicked.connect(self.btnExportDir)
        self.btn_start.clicked.connect(self.btnStart)
        self.btn_close.clicked.connect(QCoreApplication.instance().quit)

    def btnExportDir(self):
        try:
            savedir = QFileDialog.getExistingDirectory(self, '导出目录', self.cwd)
            self.savedir = savedir
            # print(savedir)
            self.text_export_dir.setText(savedir)
        except Exception:
            traceback.print_exc()

    def downMusicStart(self):
        self.listurl = self.line_list.text()
        self.loopNum = True
        try:
            down = GetMusic.GetMusicNet(self.listurl, self.savedir)
            down.DownMusic()
        except Exception:
            traceback.print_exc()
        self.loopNum = False

    def LoadLog(self):
        text_s = 0
        while self.loopNum:
            with open(self.savedir + '/log.txt') as f:
                text = f.readlines()
                text_l = len(text)
                text_e = text_l
                if text_e > text_s:
                    text_r = text[text_s:text_e]
                    for i in range(text_e):
                        # self.text_export_log.setText(text_r[i])
                        print(text_r[i])
                    text_s += 1
                f.close()
                time.sleep(1)

    def btnStart(self):
        os.system('cls')
        try:
            # t1 = threading.Thread(target=self.downMusicStart)
            t2 = threading.Thread(target=self.LoadLog)
            # t1.start()
            t2.start()
        except Exception:
            traceback.print_exc()

app = QtWidgets.QApplication(sys.argv)
MainUiWindow = QtWidgets.QMainWindow()
ui = NetMusicUI(MainUiWindow)
MainUiWindow.show()
sys.exit(app.exec_())