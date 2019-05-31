# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc_main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(204, 341)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 40, 111, 31))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit_Adder1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Adder1.setGeometry(QtCore.QRect(30, 100, 61, 31))
        self.lineEdit_Adder1.setObjectName("lineEdit_Adder1")
        self.lineEdit_Adder2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Adder2.setGeometry(QtCore.QRect(30, 180, 61, 31))
        self.lineEdit_Adder2.setObjectName("lineEdit_Adder2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 150, 21, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 150, 31, 16))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.lineEdit_sum = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_sum.setGeometry(QtCore.QRect(130, 140, 51, 31))
        self.lineEdit_sum.setReadOnly(True)
        self.lineEdit_sum.setObjectName("lineEdit_sum")
        self.pushButton_calc = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_calc.setGeometry(QtCore.QRect(30, 240, 61, 31))
        self.pushButton_calc.setObjectName("pushButton_calc")
        self.pushButton_Quit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Quit.setGeometry(QtCore.QRect(120, 240, 61, 31))
        self.pushButton_Quit.setObjectName("pushButton_Quit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 204, 23))
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
        self.label.setText(_translate("MainWindow", "简易加法计算器"))
        self.label_2.setText(_translate("MainWindow", "+"))
        self.label_3.setText(_translate("MainWindow", "="))
        self.pushButton_calc.setText(_translate("MainWindow", "计算"))
        self.pushButton_Quit.setText(_translate("MainWindow", "退出"))

    def setupFunction(self):
        self.pushButton_calc.clicked.connect(self.get_sum)

    def get_sum(self):
        adder1 = self.lineEdit_Adder1.text()  # 获取第一个文本框中的内容存入adder1
        adder2 = self.lineEdit_Adder2.text()  # 获取第二个文本框中的内容存入adder2
        sum = int(adder1) + int(adder2)  # 将adder1和adder2强制转换为整形，计算出两数之和存入sum
        self.lineEdit_sum.setText(str(sum))  # 将sum强制转换为字符串，填入lineEdit_sum

