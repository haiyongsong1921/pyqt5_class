import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from progressBar import Ui_MainWindow



class MyProgressBarWrapper(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(0)
        self.pushButton.clicked.connect(self.button_clicked)
        self.progressStep = 0
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.timeout_slot)

    def timeout_slot(self):
        if self.progressStep < 100:
            self.progressStep += 1
            self.progressBar_2.setValue(self.progressStep)
            self.progressBar_3.setValue(self.progressStep)
        else:
            self.timer.stop()
            self.pushButton.setText("重置")

    def button_clicked(self):
        self.gifProgress = QtGui.QMovie('img/progress.gif')
        self.label.setMovie(self.gifProgress)
        self.gifProgress.start()
        '''
        if self.timer.isActive():
            self.timer.stop()
            self.pushButton.setText("开始")
        else:
            if self.progressStep >= 100:
                self.progressStep = 0
            self.timer.start(50)
            self.pushButton.setText("暂停")
        '''


if __name__ == '__main__':
    app = QApplication(sys.argv)
    progressBarWindow = MyProgressBarWrapper()
    progressBarWindow.show()

    sys.exit(app.exec())