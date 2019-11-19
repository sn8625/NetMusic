# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'download.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DownloadMusic(QtWidgets.QMainWindow):
    def setupUi(self, DownloadMusic):
        DownloadMusic.setObjectName("DownloadMusic")
        DownloadMusic.resize(550, 387)
        self.lab_list = QtWidgets.QLabel(DownloadMusic)
        self.lab_list.setGeometry(QtCore.QRect(20, 20, 54, 12))
        self.lab_list.setObjectName("lab_list")
        self.lab_export_dir = QtWidgets.QLabel(DownloadMusic)
        self.lab_export_dir.setGeometry(QtCore.QRect(20, 80, 71, 16))
        self.lab_export_dir.setObjectName("lab_export_dir")
        self.text_export_dir = QtWidgets.QTextBrowser(DownloadMusic)
        self.text_export_dir.setGeometry(QtCore.QRect(100, 60, 361, 51))
        self.text_export_dir.setObjectName("text_export_dir")
        self.btn_export_dir = QtWidgets.QPushButton(DownloadMusic)
        self.btn_export_dir.setGeometry(QtCore.QRect(470, 70, 75, 23))
        self.btn_export_dir.setObjectName("btn_export_dir")
        self.btn_close = QtWidgets.QPushButton(DownloadMusic)
        self.btn_close.setGeometry(QtCore.QRect(380, 350, 75, 23))
        self.btn_close.setObjectName("btn_close")
        self.line_list = QtWidgets.QLineEdit(DownloadMusic)
        self.line_list.setGeometry(QtCore.QRect(100, 10, 361, 31))
        self.line_list.setObjectName("line_list")
        self.btn_start = QtWidgets.QPushButton(DownloadMusic)
        self.btn_start.setGeometry(QtCore.QRect(100, 350, 75, 23))
        self.btn_start.setObjectName("btn_start")
        self.text_export_log = QtWidgets.QTextEdit(DownloadMusic)
        self.text_export_log.setGeometry(QtCore.QRect(100, 130, 361, 211))
        self.text_export_log.setObjectName("text_export_log")
        self.btn_look_log = QtWidgets.QPushButton(DownloadMusic)
        self.btn_look_log.setGeometry(QtCore.QRect(240, 350, 75, 23))
        self.btn_look_log.setObjectName("btn_look_log")

        self.retranslateUi(DownloadMusic)
        QtCore.QMetaObject.connectSlotsByName(DownloadMusic)

    def retranslateUi(self, DownloadMusic):
        _translate = QtCore.QCoreApplication.translate
        DownloadMusic.setWindowTitle(_translate("DownloadMusic", "Dialog"))
        self.lab_list.setText(_translate("DownloadMusic", "歌单地址："))
        self.lab_export_dir.setText(_translate("DownloadMusic", "导出文件夹："))
        self.btn_export_dir.setText(_translate("DownloadMusic", "选择"))
        self.btn_close.setText(_translate("DownloadMusic", "关闭"))
        self.btn_start.setText(_translate("DownloadMusic", "开始下载"))
        self.btn_look_log.setText(_translate("DownloadMusic", "查看日志"))
