import sys
from Lesson5ui import Ui_MainWindow
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MyTextControlLearn(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None) -> object:
        super().__init__(parent)
        self.setupUi(self)
        self.textEdit.setTextColor(QColor(0, 0, 200))
        self.textEdit.setPlainText("欢迎来到我乐自我高的pyqt编程世界，希望你们能够学到自己想学的东西，欢迎关注我的视频教学课程")
        self.btLogin.clicked.connect(self.login)
        self.btClose.clicked.connect(self.close_Window)
        self.rbtn_admin.toggled.connect(self.rbtn_select)
        self.cbSavePwd.stateChanged.connect(self.savePwd)

    def savePwd(self):
        if self.cbSavePwd.isChecked():
            QMessageBox.information(self, "提示", "登录会保存密码", QMessageBox.Ok)

    def rbtn_select(self):
        if self.rbtn_admin.isChecked():
            QMessageBox.information(self, "提示",
                                    "选则的管理员登录", QMessageBox.Ok)
        elif self.rbtn_normal.isChecked():
            QMessageBox.information(self, "提示",
                                    "选则的普通用户登录", QMessageBox.Ok)

    def login(self):
        QMessageBox.information(self, "登录信息",
                                "用户名：" + self.ledit_userName.text()
                                + "  密码：" + self.ledit_pwd.text(), QMessageBox.Ok)

    def close_Window(self):
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    textControl = MyTextControlLearn()
    #textControl.label.setText("<a href='http://www.baidu.com'>百度主页</a>")
    #textControl.label.setOpenExternalLinks(True)
    textControl.show()
    sys.exit(app.exec())