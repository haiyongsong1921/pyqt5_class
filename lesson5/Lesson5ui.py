# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/sunhaiyang/PycharmProjects/pyqt5/lesson5/Lesson5ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(425, 235)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lab_userName = QtWidgets.QLabel(self.centralwidget)
        self.lab_userName.setGeometry(QtCore.QRect(40, 20, 61, 21))
        self.lab_userName.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lab_userName.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.lab_userName.setObjectName("lab_userName")
        self.lab_pwd = QtWidgets.QLabel(self.centralwidget)
        self.lab_pwd.setGeometry(QtCore.QRect(40, 70, 61, 21))
        self.lab_pwd.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lab_pwd.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.lab_pwd.setObjectName("lab_pwd")
        self.ledit_userName = QtWidgets.QLineEdit(self.centralwidget)
        self.ledit_userName.setGeometry(QtCore.QRect(120, 20, 141, 31))
        self.ledit_userName.setMaxLength(32)
        self.ledit_userName.setObjectName("ledit_userName")
        self.ledit_pwd = QtWidgets.QLineEdit(self.centralwidget)
        self.ledit_pwd.setGeometry(QtCore.QRect(120, 70, 141, 31))
        self.ledit_pwd.setMaxLength(8)
        self.ledit_pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ledit_pwd.setObjectName("ledit_pwd")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(290, 20, 121, 81))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.btLogin = QtWidgets.QPushButton(self.centralwidget)
        self.btLogin.setGeometry(QtCore.QRect(110, 140, 91, 32))
        self.btLogin.setObjectName("btLogin")
        self.btClose = QtWidgets.QPushButton(self.centralwidget)
        self.btClose.setGeometry(QtCore.QRect(210, 140, 91, 32))
        self.btClose.setObjectName("btClose")
        self.rbtn_admin = QtWidgets.QRadioButton(self.centralwidget)
        self.rbtn_admin.setGeometry(QtCore.QRect(50, 110, 81, 21))
        self.rbtn_admin.setChecked(True)
        self.rbtn_admin.setObjectName("rbtn_admin")
        self.rbtn_normal = QtWidgets.QRadioButton(self.centralwidget)
        self.rbtn_normal.setGeometry(QtCore.QRect(150, 110, 81, 20))
        self.rbtn_normal.setChecked(False)
        self.rbtn_normal.setObjectName("rbtn_normal")
        self.cbSavePwd = QtWidgets.QCheckBox(self.centralwidget)
        self.cbSavePwd.setGeometry(QtCore.QRect(280, 110, 86, 20))
        self.cbSavePwd.setObjectName("cbSavePwd")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 425, 24))
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
        self.lab_userName.setText(_translate("MainWindow", "用户名："))
        self.lab_pwd.setText(_translate("MainWindow", "密码："))
        self.btLogin.setText(_translate("MainWindow", "登录"))
        self.btClose.setText(_translate("MainWindow", "取消"))
        self.rbtn_admin.setText(_translate("MainWindow", "管理员"))
        self.rbtn_normal.setText(_translate("MainWindow", "普通用户"))
        self.cbSavePwd.setText(_translate("MainWindow", "记住密码"))
