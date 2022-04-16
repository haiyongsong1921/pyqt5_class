import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from Form.MainWindow import Ui_MainWindow
import sqlite3
import base64
from Form.ChangePwdDialog import Ui_Change_pwd_dialog
from Form.RegisterDialog import Ui_RegisterDialog

class RegisterWindow(QDialog, Ui_RegisterDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.buttonBox.button(QtWidgets.QDial1ogButtonBox.Ok).clicked.connect(self.Click_OK)
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

class ChangePwdWindow(QDialog, Ui_Change_pwd_dialog):
    def __init__(self, old_pwd, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).clicked.connect(self.Click_OK)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Cancel).clicked.connect(self.Click_Cancel)
        self.old_pwd = old_pwd


    def Click_OK(self):
        old_pwd = self.le_old_pwd.text()
        new_pwd = self.le_new_pwd.text()
        confirm_pwd = self.le_confirm_pwd.text()

        if not old_pwd:
            QMessageBox.information(self, "提示",
                                    "请填写旧密码", QMessageBox.Ok)
        if old_pwd != self.old_pwd:
            QMessageBox.information(self, "提示",
                                    "密码错误", QMessageBox.Ok)
        if new_pwd != confirm_pwd:
            QMessageBox.information(self, "提示",
                                    "两次密码不一致", QMessageBox.Ok)
            self.le_confirm_pwd.setText("")
            self.le_new_pwd.setText("")
        else:
            password = new_pwd
            password = str(base64.b64encode(password.encode("utf-8")))
            password_length = len(password)
            password = password[2:password_length - 1]  # 加密后格式为b'加密字符'， 要去掉b和首尾的'
            self.new_password = password

    def Click_Cancel(self):
        self.hide()