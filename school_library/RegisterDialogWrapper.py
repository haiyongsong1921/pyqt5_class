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
        self.setupUi(self)
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

    def Click_Cancel(self):
        self.hide()