import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from Form.MainWindow import Ui_MainWindow
import sqlite3
import base64
from RegisterDialogWrapper import RegisterWindow

class UserInfo:
    def __init__(self, username, password, realname, studentid):
        self.username = username
        self.password = password
        self.studentid = studentid
        self.realname = realname
        self.admin = False

def creatSQLiteDataBase(dbName):
    connection = sqlite3.connect(dbName)
    return connection

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, connection):
        super().__init__()
        self.setupUi(self)
        self.connection = connection
        self.init_Tabs()

        self.user_info_table = "user_info"
        self.book_info_table = "book_info"
        self.borrow_record_table = "borrow_record"
        self.init_database(connection)



    def init_database(self, connection):
        #1. create user table
        cursor = connection.cursor()
        sql = "CREATE TABLE IF NOT EXISTS {0} (id INTEGER NOT NULL UNIQUE,username varchar(20) UNIQUE," \
              "password varchar(20),studentid varchar(20),name varchar(20)" \
              ",admin INTEGER, PRIMARY KEY(id AUTOINCREMENT))".format(self.user_info_table)
        cursor.execute(sql)
        sql = "CREATE TABLE IF NOT EXISTS {0} (id INTEGER NOT NULL UNIQUE,studentid varchar(20)," \
              "bookindex TEXT,bookname TEXT,borrowtime datetime default current_timestamp" \
              ",returntime datetime default current_timestamp, PRIMARY KEY(id AUTOINCREMENT))".format(self.borrow_record_table)
        cursor.execute(sql)
        #2. create borrow_record table

        return cursor


    def init_Tabs(self):
        self.__init_Main_Tab()
        self.__init_Search_Tab()
        self.__init_Return_Tab()
        self.__init_User_Manage_Tab()



    def __init_Main_Tab(self):
        # 主页背景图
        self.lb_main_bk.setPixmap(QtGui.QPixmap("./img/main_bk_ground.png"))
        self.label_Title.setText("阅己")
        # 主页登录按钮
        self.pb_login.clicked.connect(self.login)
        self.pb_register.clicked.connect(self.register)

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

    def __init_User_Manage_Tab(self):
        # 用户管理页背景图
        self.lb_user_bk.setScaledContents(True)
        self.lb_user_bk.setPixmap(QtGui.QPixmap("./img/user_man.png"))

    def return_book(self):
        bookNo = self.le_return_bookid.text()
        pass


    def search_book(self):
        search_keywords = self.le_search_keyword.text()
        pass

    def login(self):
        userName = self.le_user.text()
        pwd = self.le_pwd.text()
        if not userName:
            QMessageBox.information(self, "提示",
                                    "用户名不能为空", QMessageBox.Ok)
            return
        if self.__login_success(userName, pwd):
            self.le_user.hide()
            self.le_pwd.hide()
            self.lb_main_user.hide()
            self.lb_main_pwd.hide()
            self.label_main_slogon.setStyleSheet("color:rgb(0, 255, 0)")
            self.label_main_slogon.setText("登录成功")
        else:
            QMessageBox.information(self, "提示",
                                    "用户名或密码错误，请重新输入", QMessageBox.Ok)
            return
    def register(self):
        registerDialog = RegisterWindow(self)
        registerDialog.exec()

        username = registerDialog.username
        password = registerDialog.password
        password = str(base64.b64encode(password.encode("utf-8")))
        password_length = len(password)
        password = password[2:password_length-1] #加密后格式为b'加密字符'， 要去掉b和首尾的'

        studentid = registerDialog.studentid

        realname = registerDialog.realname
        if (not username) or (not studentid) or (not realname):
            QMessageBox.information(self, "提示",
                                    "用户名,学号和真实姓名不能为空", QMessageBox.Ok)
            return
        user = UserInfo(username, password, realname, studentid)
        try:
            self.__register_to_database(user)
        except Exception:
            QMessageBox.information(self, "提示",
                                    "注册失败！请重新注册", QMessageBox.Ok)
        else:
            QMessageBox.information(self, "提示",
                                    "注册成功！", QMessageBox.Ok)



        '''
        userName = self.le_user.text()
        if not userName:
            QMessageBox.information(self, "提示",
                                    "用户名不能为空", QMessageBox.Ok)
            return
        
        pwd = self.le_pwd.text()
        #encrypt_pwd = base64.encodestring('hell')
        encrypt_pwd = base64.b64encode(pwd.encode("utf-8"))
        decrypt_pwd = base64.b64decode(encrypt_pwd.decode("utf-8"))

        if self.__login_success(userName, pwd):
            self.le_user.hide()
            self.le_pwd.hide()
            self.lb_main_user.hide()
            self.lb_main_pwd.hide()
            self.label_main_slogon.setStyleSheet("color:rgb(0, 255, 0)")
            self.label_main_slogon.setText("注册成功")
        '''
    def __register_to_database(self, user_info):
        cursor = self.connection.cursor()
        record_count = cursor.execute("select count(*) from user_info")
        result = cursor.fetchone()[0]
        if not result:  #注册第一个用户，默认为管理员
            sql = "INSERT INTO user_info VALUES(NULL,'{0}','{1}','{2}','{3}',1)".format(user_info.username,
                                                                                          user_info.password,
                                                                                          user_info.studentid,
                                                                                          user_info.realname)
        else:
            sql = "INSERT INTO user_info VALUES(NULL,'{0}','{1}','{2}','{3}',0)".format(user_info.username,
                                                                                          user_info.password,
                                                                                          user_info.studentid,
                                                                                          user_info.realname)
        cursor.execute(sql)
        self.connection.commit()
        cursor.close()


    def __login_success(self, user, pwd):
        cursor = self.connection.cursor()
        sql = "select password from user_info where username='{0}'".format(user)
        cursor.execute(sql)
        result = cursor.fetchall()
        pwd_db = result[0]
        pwd_decode = base64.b64decode(str(pwd_db)).decode("utf-8")
        if pwd_decode == pwd:
            return True
        else:
            return False


DATABASE_NAME = "School_library.db"
if __name__ == '__main__':
    connection = creatSQLiteDataBase(DATABASE_NAME)
    app = QApplication(sys.argv)
    messageBox = MyMainWindow(connection)
    messageBox.show()

    sys.exit(app.exec())