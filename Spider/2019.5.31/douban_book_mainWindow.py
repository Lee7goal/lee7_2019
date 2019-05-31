# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'douban_book_mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import requests

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(337, 538)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 131, 16))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 10, 31, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 40, 31, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_name.setGeometry(QtCore.QRect(180, 10, 151, 20))
        self.lineEdit_name.setReadOnly(True)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.lineEdit_author = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_author.setGeometry(QtCore.QRect(180, 40, 151, 20))
        self.lineEdit_author.setReadOnly(True)
        self.lineEdit_author.setObjectName("lineEdit_author")
        self.textEdit_content = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_content.setGeometry(QtCore.QRect(150, 70, 181, 131))
        self.textEdit_content.setReadOnly(True)
        self.textEdit_content.setObjectName("textEdit_content")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 210, 331, 231))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(3, 190, 131, 20))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.pushButton_getvalue = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_getvalue.setGeometry(QtCore.QRect(40, 450, 91, 41))
        self.pushButton_getvalue.setObjectName("pushButton_getvalue")
        self.label_pic = QtWidgets.QLabel(self.centralwidget)
        self.label_pic.setGeometry(QtCore.QRect(10, 20, 121, 169))
        self.label_pic.setText("")
        self.label_pic.setObjectName("label_pic")
        self.pushButton_quit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_quit.setGeometry(QtCore.QRect(200, 450, 91, 41))
        self.pushButton_quit.setObjectName("pushButton_quit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 337, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "书籍图片"))
        self.label_2.setText(_translate("MainWindow", "书名"))
        self.label_3.setText(_translate("MainWindow", "作者"))
        self.label_10.setText(_translate("MainWindow", "精选评论"))
        self.pushButton_getvalue.setText(_translate("MainWindow", "手气不错"))
        self.pushButton_quit.setText(_translate("MainWindow", "退出"))

    def setupFunction(self):
        self.pushButton_getvalue.clicked.connect(self.get_value)
        self.pushButton_quit.clicked.connect(self.pb_quit)

    def get_value(self):
        name = '123'
        author = '123'
        content = '123'
        link = 'https://img3.doubanio.com/view/subject/m/public/s3563113.jpg'
        self.lineEdit_name.setText(name)
        self.lineEdit_author.setText(author)
        self.textEdit_content.setText(content)
        self.label_pic.setPixmap(QtGui.QPixmap('1.jpg'))
        self.label_pic.setScaledContents(True)

    def pb_quit(self):
        quit()