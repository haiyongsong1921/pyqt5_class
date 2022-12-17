import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from lesson8.DateTime import Ui_MainWindow

class MyDateTime(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.calendarWidget.selectionChanged.connect(self.showSelectData)

    def showSelectData(self):
        date = QtCore.QDate(self.calendarWidget.selectedDate())
        year = date.year()
        month = date.month()
        day = date.day()
        QMessageBox.information(self, "提示", str(year)+"-"+str(month)+"-"+str(day), QMessageBox.Ok)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dateTime = MyDateTime()
    dateTime.show()

    sys.exit(app.exec())
