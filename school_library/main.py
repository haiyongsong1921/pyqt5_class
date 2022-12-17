import sys
from datetime import datetime, timedelta, date

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from Form.MainWindow import Ui_MainWindow
import sqlite3
import base64
from RegisterDialogWrapper import RegisterWindow, ChangePwdWindow, BorrowHistoyDialog

class UserInfo:
    def __init__(self, username, password, realname, studentid):
        self.username = username
        self.password = password
        self.studentid = studentid
        self.realname = realname
        self.admin = False

class BookAdditionInfo:
    def __init__(self):
        self.isbn = ""
        self.price = ""
        self.language = ""
        self.pages = ""
        self.overview = ""

class BookInfo:
    def __init__(self, name, author, publisher, publish_date, search_index):
        self.name = name
        self.writer = author
        self.publisher = publisher
        self.publish_date = publish_date
        self.search_index = search_index
        self.addtionalInfo = BookAdditionInfo()

    def __str__(self):
        return self. name + "," + self.writer+"," + self.publisher+"," + self.publish_date+"," + self.search_index

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
              ",returntime datetime default current_timestamp,bookstatus INTEGER default 0" \
              ", PRIMARY KEY(id AUTOINCREMENT))".format(self.borrow_record_table)
        cursor.execute(sql)
        #2. create borrow_record table

        return cursor

    def __enable_tabs(self, visable):
        self.tabWidget.setTabVisible(1, visable)
        self.tabWidget.setTabVisible(2, visable)
        self.tabWidget.setTabVisible(3, visable)

    def init_Tabs(self):
        self.__init_Main_Tab()
        self.__init_Search_Tab()
        self.__init_Return_Tab()
        self.__init_User_Manage_Tab()
        #启动程序时，只显示登录界面，登录成功后，才可访问其它功能
        self.__enable_tabs(False)

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
        self.lb_search_bk.setPixmap(QtGui.QPixmap("./img/search_book.jpeg"))
        # 查询按钮
        self.pb_search.clicked.connect(self.search_book)
        # 添加数据到查询方式comboBox
        search_options = ["按照书名查找", "按照作者查找", "按照书号查找"]
        self.cb_search_option.addItems(search_options)
        # 设置结果表头
        headers = ["序号", "书名", "作者", "出版商", "发行日期", "图书编号", "页码", "图书状态"]
        self.tw_search_result.setHorizontalHeaderLabels(headers)
        self.tw_search_result.setColumnCount(8)

    def __init_Return_Tab(self):
        # 图书搜索页背景图
        self.lb_book_return_bk.setScaledContents(True)
        self.lb_book_return_bk.setPixmap(QtGui.QPixmap("./img/return_bk.jpeg"))
        # 按钮
        self.pb_return_search.clicked.connect(self.return_search)
        self.pb_return_b.clicked.connect(self.borrow_book)
        self.pb_return_r.clicked.connect(self.return_book)
        # 初始状态，隐藏标签
        self.label_bookname.hide()
        self.label_author.hide()
        self.label_status.hide()

    def __init_User_Manage_Tab(self):
        # 用户管理页背景图
        self.lb_user_bk.setScaledContents(True)
        self.lb_user_bk.setPixmap(QtGui.QPixmap("./img/user_man.png"))
        self.pb_change_info.clicked.connect(self.change_pwd)
        self.pb_logout.clicked.connect(self.logout)
        self.pb_history.clicked.connect(self.borrow_history)

    def change_pwd(self):
        changePwdDialog = ChangePwdWindow(self.currentUser_pwd)
        changePwdDialog.exec()#弹出密码修改对话框
        if changePwdDialog.new_password:
            new_pwd = changePwdDialog.new_password
            sql = '''update user_info set password=? where studentid=?'''
            tuple_value = (new_pwd, self.currentUser)
            cursor = self.connection.cursor()
            cursor.execute(sql, tuple_value)
            self.connection.commit()
            cursor.close()
            QMessageBox.information(self, "提示",
                                    "密码修改成功", QMessageBox.Ok)

    def borrow_history(self):
        sql = '''select bookname,bookindex,borrowtime,returntime from borrow_record where studentid=?'''
        tuple_value = (self.currentUser,)
        cursor = self.connection.cursor()
        cursor.execute(sql, tuple_value)
        result = cursor.fetchall()
        borrowDialog = BorrowHistoyDialog(self)
        borrowDialog.fill_data_to_tableWidget(result)
        borrowDialog.exec()

    def logout(self):
        self.__enable_tabs(False)
        self.le_user.show()
        self.le_pwd.show()
        self.lb_main_user.show()
        self.lb_main_pwd.show()
        self.label_main_slogon.setText("")


    def return_search(self):
        bookNo = self.le_return_bookid.text()
        if len(bookNo)>0:
            sql = '''select name,writer from book_info where search_index="{0}"'''.format(bookNo)
            cursor = self.connection.cursor()
            cursor.execute(sql)
            result = cursor.fetchone()
            if not result:
                self.label_bookname.setText("未找到")
                self.label_author.setText("无")
                self.label_status.setText("无")
            else:
                self.label_bookname.setText(result[0])
                self.label_author.setText(result[1])
                self.searchedBook = result[0]
                if self.__is_book_in_library(bookNo):
                    contentStatus = "在馆"
                else:
                    contentStatus = "借出"
                self.label_status.setText(contentStatus)
                self.label_bookname.show()
                self.label_author.show()
                self.label_status.show()
        else:
            QMessageBox.information(self, "提示",
                                    "请输入书号", QMessageBox.Ok)
    def borrow_book(self):
        bookNo = self.le_return_bookid.text()
        if len(bookNo)>0:
            sql = '''select bookname from borrow_record where bookindex="{0}"'''.format(bookNo)
            cursor = self.connection.cursor()
            cursor.execute(sql)
            result = cursor.fetchone()
            if not result: #没有记录，表示之前没有过借出的记录，此时增加一条借阅记录到borrow_record表中
                sql = '''insert into borrow_record values(NULL,?,?,?,?,?,?)'''
                tupleValue = (self.currentUser,bookNo,self.searchedBook, datetime.now(),
                              datetime.now() + timedelta(days=14), 1)
            else:#有记录，之前被借过,怎更新标志位为1，表示被借出
                sql = '''update borrow_record set bookstatus=1 where bookindex=?'''
                tupleValue =(bookNo,)

            cursor.execute(sql,tupleValue)
            self.connection.commit()
            self.label_status.setText("借出")
            cursor.close()
            return_date = datetime.today()+timedelta(days=14)
            str_return_date = return_date.strftime("%Y-%m-%d")

            QMessageBox.information(self, "提示",
                                    "请于" + str_return_date + "之前归还本书!", QMessageBox.Ok)
        else:
            QMessageBox.information(self, "提示",
                                    "请输入书号", QMessageBox.Ok)

    def return_book(self):
        bookNo = self.le_return_bookid.text()
        sql = '''update borrow_record set bookstatus=0 where bookindex=?'''
        tupleValue = (bookNo,)
        cursor = self.connection.cursor()
        cursor.execute(sql, tupleValue)
        self.connection.commit()
        self.label_status.setText("在馆")
        cursor.close()
        QMessageBox.information(self, "提示",
                                    "图书归还成功！", QMessageBox.Ok)

    def search_book(self):
        search_keywords = self.le_search_keyword.text()
        filter_index = self.cb_search_option.currentIndex()
        if filter_index==0:
            filter_key = "name"
        elif filter_index==1:
            filter_key = "writer"
        elif filter_index==2:
            filter_key = "search_index"

        sql = '''select name,writer,publisher,publish_date,search_index,pages from book_info 
        where {0} like "%{1}%"'''.format(filter_key, search_keywords)
        cursor = self.connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        if len(result) > 0:
            self.fill_data_tableWidget(result)

    def fill_data_tableWidget(self, result):
        rowCount = len(result)
        colCount = len(result[0])
        self.tw_search_result.setRowCount(rowCount)
        for row in range(rowCount):
            contentId = str(row+1)
            tw_item = QTableWidgetItem(contentId)
            tw_item.setTextAlignment(Qt.AlignCenter)
            self.tw_search_result.setItem(row, 0, tw_item)
            if self.__is_book_in_library(result[row][4]):
                contentStatus = "在馆"
            else:
                contentStatus = "借出"
            tw_item = QTableWidgetItem(contentStatus)
            self.tw_search_result.setItem(row, 7, tw_item)
            for col in range(colCount):
                content = str(result[row][col])
                tw_item = QTableWidgetItem(content)
                self.tw_search_result.setItem(row, col+1, tw_item)
        self.tw_search_result.resizeColumnsToContents()
        self.tw_search_result.setAlternatingRowColors(True)

    def __is_book_in_library(self, book_index):
        sql = '''select bookstatus from borrow_record where bookindex="{0}"'''.format(book_index)
        cursor = self.connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchone()
        if not result:  #没有该书记录，则说明该书没有被借出过，在馆
            return True
        elif result[0]>0: #有记录，且状态>0， 表示借出
            return False
        else:
            return True # bookstatus==0， 表示在馆

    def login(self):
        userName = self.le_user.text()
        pwd = self.le_pwd.text()
        if not userName:
            QMessageBox.information(self, "提示",
                                    "用户名不能为空", QMessageBox.Ok)
            return
        if self.__login_success(userName, pwd):
            self.currentUser_pwd = pwd
            self.le_user.hide()
            self.le_pwd.hide()
            self.lb_main_user.hide()
            self.lb_main_pwd.hide()
            self.label_main_slogon.setStyleSheet("color:rgb(0, 255, 0)")
            self.label_main_slogon.setText("登录成功")
            self.__enable_tabs(True)

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
        sql = "select password,studentid from user_info where username='{0}'".format(user)
        cursor.execute(sql)
        result = cursor.fetchall()
        pwd_db = result[0][0]
        pwd_decode = base64.b64decode(str(pwd_db)).decode("utf-8")
        if pwd_decode == pwd:
            self.currentUser = result[0][1]
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