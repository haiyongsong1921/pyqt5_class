import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from Form.MainWindow import Ui_MainWindow



class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_Tabs()


    def init_Tabs(self):
        self.__init_Main_Tab()
        self.__init_Search_Tab()
        self.__init_Return_Tab()
        #用户管理页背景图
        self.lb_user_bk.setScaledContents(True)
        self.lb_user_bk.setPixmap(QtGui.QPixmap("./img/user_man.png"))


    def __init_Main_Tab(self):
        # 主页背景图
        self.lb_main_bk.setPixmap(QtGui.QPixmap("./img/main_bk_ground.png"))
        self.label_Title.setText("阅己")
        # 主页登录按钮
        self.pb_login.clicked.connect(self.login)

    def __init_Search_Tab(self):
        # 图书搜索页背景图
        self.lb_search_bk.setScaledContents(True)
        self.lb_search_bk.setPixmap(QtGui.QPixmap("./img/search.jpeg"))
        # 主页登录按钮
        self.pb_search.clicked.connect(self.search_book)
        # 添加数据到查询方式comboBox
        search_options = ["按照书名查找", "按照作者查找", "按照书号查找", "按照出版年份查找"]
        self.cb_search_option.addItems(search_options)

    def __init_Return_Tab(self):
        # 图书搜索页背景图
        self.lb_book_return_bk.setScaledContents(True)
        self.lb_book_return_bk.setPixmap(QtGui.QPixmap("./img/return_bk.jpeg"))
        # 主页登录按钮
        self.pb_return_search.clicked.connect(self.return_book)

    def return_book(self):
        bookNo = self.le_return_bookid.text()
        pass


    def search_book(self):
        search_keywords = self.le_search_keyword.text()
        pass

    def login(self):
        userName = self.le_user.text()
        pwd = self.le_pwd.text()
        if self.__login_success(userName, pwd):
            self.le_user.hide()
            self.le_pwd.hide()
            self.lb_main_user.hide()
            self.lb_main_pwd.hide()
            self.label_main_slogon.setStyleSheet("color:rgb(0, 255, 0)")
            self.label_main_slogon.setText("登录成功")

    def __login_success(self, user, pwd):
        return True

if __name__ == '__main__':
    st = "aberw,sdf"
    st_list = st.split("#")
    app = QApplication(sys.argv)
    messageBox = MyMainWindow()
    messageBox.show()

    sys.exit(app.exec())