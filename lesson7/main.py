import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from lesson7 import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets


class MyTextControlLearn(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.addTab)
        self.init_comboBox()
        self.init_listWidget()

    def show_selected_list_item(self, item):
        if item.isSelected():
            QMessageBox.information(self, "提示", "选择的是：" + item.text(), QMessageBox.Ok)

    def init_listWidget(self):
        from collections import OrderedDict
        order_dict = OrderedDict({'/c第一名': '?c2021年剧情喜剧《腿》',
                                  '第二名': '2021年科幻动作《永恒族/永恒神族',
                                  '第三名': '2021年喜剧悬疑《不速来客》',
                                  '第四名': '2021年喜剧《亚当斯一家2》',
                                  '第五名': '2022年纪录片《哈利·波特20周年：回到霍格沃茨》',
                                  '第六名': '2021年历史战争《执行/逃出奥斯威辛》',
                                  '第七名': '2021年奇幻喜剧《超能敢死队》',
                                  '第八名': '2020年动作灾难《紧急救援》'
                                  })
        for key, value in order_dict.items():
            self.item = QtWidgets.QListWidgetItem(self.listWidget)
            self.item.setText(key + " : " + value)
            self.item.setToolTip(value)
        self.listWidget.itemClicked.connect(self.show_selected_list_item)

    def addTab(self):
        self.newTab = QtWidgets.QWidget()
        tabObjectName = "tab_" + str(self.tabWidget.count() + 1)
        tabDisplayName = "Tab " + str(self.tabWidget.count() + 1)
        self.newTab.setObjectName(tabObjectName)
        self.tabWidget.addTab(self.newTab, tabDisplayName)

    def showInfo(self):
        self.label_2.setText(self.comboBox.currentText())

    def init_comboBox(self):
        list = ["Tesla", "腾讯", "亚马逊", "Google", "12306"]
        self.comboBox.addItems(list)
        self.comboBox.currentTextChanged.connect(self.showInfo)
        self.label_2.setText(self.comboBox.currentText())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mWidget = MyTextControlLearn()
    mWidget.show()

    sys.exit(app.exec())
