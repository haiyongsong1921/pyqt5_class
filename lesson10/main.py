import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from menu import Ui_MainWindow


class MyMenuWrapper(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyMenuWrapper,  self).__init__()
        self.setupUi(self)
        self.menu.triggered.connect(self.open_file)

    def open_file(self, menuItem):
        QMessageBox.information(self, "提示", "点击了菜单：" + menuItem.text(), QMessageBox.Ok)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    menuWindow = MyMenuWrapper()
    menuWindow.show()

    sys.exit(app.exec())