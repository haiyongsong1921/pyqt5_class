import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from Form.MainWindow import Ui_MainWindow
import sqlite3
import base64
from Form.RegisterWindow import Ui_RegisterWindow
from Form.RegisterDialog import Ui_RegisterDialog

class RegisterWindow(QDialog, Ui_RegisterDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        #super().__init__()
        self.setupUi(self)
        #self.pb_reg_ok.clicked.connect(self.Click_OK)
        #self.pb_reg_cancel.clicked.connect(self.Click_Cancel)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).clicked.connect(self.Click_OK)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Cancel).clicked.connect(self.Click_Cancel)

        self.username = ""
        self.password = ""
        self.realname = ""
        self.studentid = ""

    def Click_OK(self):
        self.username = self.le_reg_username.text()
        self.password = self.le_reg_password.text()
        self.realname = self.le_reg_realname.text()
        self.studentid = self.le_reg_studentid.text()
        if (not self.username) or (not self.studentid) or (not self.realname):
            QMessageBox.information(self, "提示",
                                    "用户名,学号和真实姓名不能为空", QMessageBox.Ok)
        else:
            pass

    def Click_Cancel(self):
        self.hide()