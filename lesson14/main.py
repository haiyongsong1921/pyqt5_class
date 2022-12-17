import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from messagebox import Ui_MainWindow


class MyMessageBox(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_info.clicked.connect(self.messageBox_info_click);
        self.pushButton_warn.clicked.connect(self.messageBox_warn_click);
        self.pushButton_question.clicked.connect(self.messageBox_question_click);
        self.pushButton_error.clicked.connect(self.messageBox_critical_click);
        self.pushButton_about.clicked.connect(self.messageBox_about_click);


    def messageBox_info_click(self):
        QtWidgets.QMessageBox.information(self, "信息", '信息对话框', QMessageBox.Ok)

    def messageBox_warn_click(self):
        QtWidgets.QMessageBox.warning(self, "警告", '警告对话框', QMessageBox.Ok | QMessageBox.Ignore)

    def messageBox_question_click(self):
        select = QtWidgets.QMessageBox.question(self, "问题", '问题对话框', QMessageBox.Yes | QMessageBox.No)
        if select == QMessageBox.Yes:
            QMessageBox.information(None, '响应', '点击了 yes 按钮')
        elif select == QMessageBox.No:
            QMessageBox.information(None, '响应', '点击了 no 按钮')

    def messageBox_critical_click(self):
        QtWidgets.QMessageBox.critical(self, "错误", '错误对话框', QtWidgets.QMessageBox.Close)

    def messageBox_about_click(self):
        QtWidgets.QMessageBox.about(self, "关于", '关于对话框')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    messageBox = MyMessageBox()
    messageBox.show()

    sys.exit(app.exec())