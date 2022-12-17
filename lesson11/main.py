import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from ToolStatusBar import Ui_MainWindow

class MyToolStatusBarWrapper(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyToolStatusBarWrapper,  self).__init__()
        self.setupUi(self)
        self.toolBar.addAction(QtGui.QIcon("resource/open.ico"), "打开")
        self.toolBar.addAction(QtGui.QIcon("resource/edit.ico"), "编辑")
        self.toolBar.addAction(QtGui.QIcon("resource/setting.ico"), "设置")
        self.toolBar.addAction(QtGui.QIcon("resource/delete.ico"), "删除")
        self.comboBox = QtWidgets.QComboBox()
        listMovie = ["钢铁侠", "蜘蛛侠", "绿灯侠", "蝙蝠侠"]
        self.comboBox.addItems(listMovie)
        self.toolBar.addWidget(self.comboBox)
        self.toolBar.actionTriggered.connect(self.click_toolBar)

        self.statusLabel = QtWidgets.QLabel()
        self.statusLabel.setText("我可自我高：PyQt5教学视频")
        self.statusBar.addPermanentWidget(self.statusLabel)

        self.statusBar.showMessage("状态栏临时信息")

    def click_toolBar(self, button):
        QMessageBox.information(self, "提示", "点击了 '" + button.text() + "' 工具按钮", QMessageBox.Ok)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    toolBar = MyToolStatusBarWrapper()
    toolBar.show()
    sys.exit(app.exec())