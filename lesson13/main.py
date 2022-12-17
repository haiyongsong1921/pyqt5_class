import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from treeWidget import Ui_MainWindow


class EmployeeInfo:
    def __init__(self, name, department, company):
        self.name = name
        self.department = department
        self.company = company

class MyTreeWidgetWrapper(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.treeWidget.setHeaderLabels(['公司', '部门', '姓名'])
        root = QTreeWidgetItem(self.treeWidget)
        root.setText(0,"组织列表")
        emp1 = EmployeeInfo("Andy", "市场", "Tesla")
        emp2 = EmployeeInfo("Vincent", "人事", "Tesla")
        emp3 = EmployeeInfo("Jack", "市场", "Google")
        emp4 = EmployeeInfo("Shawn", "财务", "Google")
        emp5 = EmployeeInfo("Shawn", "财务", "Microsoft")
        employeeList = [emp1, emp2, emp3, emp4, emp5]
        for employ in employeeList:
            child = QTreeWidgetItem(root)
            if(employ.company == "Tesla"):
                child.setIcon(0,QtGui.QIcon('img/Tesla.jpeg'))
            elif(employ.company == "Google"):
                child.setIcon(0, QtGui.QIcon('img/Google.jpeg'))
            elif(employ.company == "Microsoft"):
                child.setIcon(0, QtGui.QIcon('img/micro.jpeg'))
            child.setText(0, employ.company)
            child.setText(1, employ.department)
            child.setText(2, employ.name)
            child.setCheckState(0, QtCore.Qt.Checked)
        self.treeWidget.addTopLevelItem(root)
        self.treeWidget.expandAll()
        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.clicked.connect(self.click_tree_item)

    def click_tree_item(self, index):
        item = self.treeWidget.currentItem()
        QtWidgets.QMessageBox.information(self, "提示", '选中：%s' % item.text(2), QtWidgets.QMessageBox.Ok)

        '''
        model = QtGui.QStandardItemModel()
        model.setHorizontalHeaderLabels(["公司", "部门", "姓名"])
        emp1 = EmployeeInfo("Andy", "市场", "Tesla")
        emp2 = EmployeeInfo("Vincent", "人事", "Tesla")
        emp3 = EmployeeInfo("Jack", "市场", "Google")
        emp4 = EmployeeInfo("Shawn", "财务", "Google")
        emp5 = EmployeeInfo("Shawn", "财务", "微软")
        employeeList = [emp1, emp2, emp3, emp4, emp5]
        companyLevel = ""、`
        for employee in employeeList:
            if employee.company != companyLevel:
                companyLevel = employee.company
                company = QtGui.QStandardItem(employee.company)
                model.appendRow(company)
            company.appendRow([QtGui.QStandardItem(""), QtGui.QStandardItem(employee.department), QtGui.QStandardItem(employee.name)])
        self.treeView.setModel(model)
'''

if __name__ == '__main__':
    app = QApplication(sys.argv)
    treeWidget = MyTreeWidgetWrapper()
    treeWidget.show()

    sys.exit(app.exec())