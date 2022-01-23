import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from vLayout import Ui_MainWindow
from gridLayout import Ui_GridMainWindow
from formLayout import Ui_FormMainWindow

class MyLayoutWrapper(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class MyGridLayoutWrapper(QMainWindow, Ui_GridMainWindow):
    def __init__(self):
        super(MyGridLayoutWrapper, self).__init__()
        self.setupUi(self)

class MyFormLayoutWrapper(QMainWindow, Ui_FormMainWindow):
    def __init__(self):
        super(MyFormLayoutWrapper,  self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    layout = MyFormLayoutWrapper()
    layout.show()

    sys.exit(app.exec())
