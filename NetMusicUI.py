#!/usr/bin/env python
# coding:utf-8

from PyQt5.QtCore import QThread, pyqtSignal, QDateTime, QObject
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
import download
import sys
import os
import traceback
import GetMusic
import time
import threading

class Work(QThread):
    trigger = QtCore.pyqtSignal(str)

    def run(self):
        sec = 0
        while 1:
            self.trigger.emit('正在下载....已进行' + str(sec) + '秒')
            time.sleep(1)
            sec += 1

class NetMusicUI(download.Ui_DownloadMusic):
    def __init__(self, DownloadMusic):
        super(download.Ui_DownloadMusic,self).__init__()
        super().setupUi(DownloadMusic)
        super().retranslateUi(DownloadMusic)
        self.cwd = os.getcwd()
        self.timer = QTimer()
        self.loopNum = True

        self.btn_export_dir.clicked.connect(self.btnExportDir)
        self.btn_start.clicked.connect(self.downMusicStart)
        self.btn_close.clicked.connect(QCoreApplication.instance().quit)
        self.listurl = self.line_list.text()

    def btnExportDir(self):
        try:
            savedir = QFileDialog.getExistingDirectory(self, '导出目录', self.cwd)
            self.savedir = savedir
            # print(savedir)
            self.text_export_dir.setText(savedir)
        except Exception:
            traceback.print_exc()

    def downMusicStart(self):
        try:
            down = GetMusic.GetMusicNet(self.listurl, self.savedir)
            down.DownMusic()
            # runtime = False
        except Exception:
            traceback.print_exc()

        self.backlog = Work()
        self.backlog.trigger.connect(self.LoadLog)
        self.thread = QThread()
        self.backlog.moveToThread(self.thread)
        self.thread.started.connect(self.backlog.run)
        self.backlog.start()

    def LoadLog(self, sec):
        self.text_export_log.setText(sec)

app = QtWidgets.QApplication(sys.argv)
MainUiWindow = QtWidgets.QMainWindow()
ui = NetMusicUI(MainUiWindow)
MainUiWindow.show()
sys.exit(app.exec_())