import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from tableWidget import Ui_MainWindow
import sqlite3

class MyTableWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.resultList = self.load_data_from_database()
        self.init_tableWidget(self.resultList)

    def load_data_from_database(self):
        connection = sqlite3.connect("STEAM.db")
        cursor = connection.cursor()
        cursor.execute("select * from student")
        results = cursor.fetchall()
        cursor.close()
        connection.close()
        return results

    def init_tableWidget(self, resultList):
        headers = ['ID', '姓名', '班级', '学校']
        self.tableWidget.setHorizontalHeaderLabels(headers)
        self.tableWidget.setRowCount(len(self.resultList))
        for result in resultList:
            rowIndex = resultList.index(result)
            for colIndex in range(4):
                if colIndex == 2:
                    comboBox = QComboBox()
                    comboBox.addItems(["三年一班", "三年二班", "三年三班"])
                    comboBox.setCurrentIndex(0)
                    self.tableWidget.setCellWidget(rowIndex, 2, comboBox)
                else:
                    item = QTableWidgetItem(str(result[colIndex]))
                    self.tableWidget.setItem(rowIndex, colIndex, item)
        self.tableWidget.sortItems(1, QtCore.Qt.AscendingOrder)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tableWidget = MyTableWidget()
    tableWidget.show()

    sys.exit(app.exec())