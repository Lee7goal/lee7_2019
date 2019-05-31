# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/31 16:37'
__author__ = 'lee7goal'
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from douban_book_mainWindow import Ui_MainWindow as UIM

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UIM()
    ui.setupUi(MainWindow)
    ui.setupFunction()
    MainWindow.show()
    sys.exit(app.exec_())