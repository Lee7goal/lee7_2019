# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from calc_main_window import Ui_MainWindow as UIM



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UIM()
    ui.setupUi(MainWindow)
    ui.setupFunction()
    MainWindow.show()
    sys.exit(app.exec_())