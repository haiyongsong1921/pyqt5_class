# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/sunhaiyang/PycharmProjects/pyqt5/lesson9/formLayout.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormMainWindow(object):
    def setupUi(self, FormMainWindow):
        FormMainWindow.setObjectName("FormMainWindow")
        FormMainWindow.resize(342, 192)
        self.centralwidget = QtWidgets.QWidget(FormMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(9, 9, 321, 111))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.pushButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.pushButton_2)
        FormMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FormMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 342, 24))
        self.menubar.setObjectName("menubar")
        FormMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FormMainWindow)
        self.statusbar.setObjectName("statusbar")
        FormMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(FormMainWindow)
        QtCore.QMetaObject.connectSlotsByName(FormMainWindow)

    def retranslateUi(self, FormMainWindow):
        _translate = QtCore.QCoreApplication.translate
        FormMainWindow.setWindowTitle(_translate("FormMainWindow", "MainWindow"))
        self.label.setText(_translate("FormMainWindow", "用户名"))
        self.label_2.setText(_translate("FormMainWindow", "密码"))
        self.pushButton.setText(_translate("FormMainWindow", "确定"))
        self.pushButton_2.setText(_translate("FormMainWindow", "取消"))