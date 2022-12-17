import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
#from testDialog import *
from test import *



class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.turn_on_off)
        self.turn_off = QPixmap("./img/light_off.png")
        self.turn_on = QPixmap("./img/light_on.png")
        self.label.setPixmap(self.turn_off)
        self.click_time = 0

    def turn_on_off(self):
        self.click_time += 1
        if self.click_time % 2 == 0:
            self.label.setPixmap(self.turn_off)
            self.pushButton.setText("开")
        else:
            self.label.setPixmap(self.turn_on)
            self.pushButton.setText("关")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mro = MyMainWindow.__mro__
    print(mro)

   # mainWindow = QMainWindow()
    #ui = Ui_MainWindow()
   # ui.setupUi(mainWindow)
    #mainWindow.show()
    myMainWindow = MyMainWindow()
    myMainWindow.show()
    sys.exit(app.exec())
