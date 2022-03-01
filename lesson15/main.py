import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from dialog import Ui_MainWindow


class MyFileDialog(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.open_file_dialog)
        self.pushButton_font.clicked.connect(self.open_font_dialog)
        self.pushButton_color.clicked.connect(self.open_color_dialog)
        self.textEdit.setText("科技少年")

    def open_font_dialog(self):
        dialog = QFontDialog()
        font, select = dialog.getFont()
        if select:
            self.textEdit.setFont(font)

    def open_color_dialog(self):
        dialog = QColorDialog
        color = dialog.getColor()
        if color.isValid():
            self.textEdit.setTextColor(color)


    def open_file_dialog(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.ExistingFiles)
        dialog.setDirectory('./')
        dialog.setNameFilter(('*.py'))
        if dialog.exec():
            fileName = dialog.selectedFiles()
            self.lineEdit.setText(fileName[0])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    fileDialog = MyFileDialog()
    fileDialog.show()

    sys.exit(app.exec())