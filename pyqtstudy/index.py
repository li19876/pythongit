from login import Ui_MainWindow  # 导入uitestPyQt5.ui转换为uitestPyQt5.py中的类

from PyQt5 import QtWidgets
import sys


class Mywindow(QtWidgets.QMainWindow, Ui_MainWindow):
    # 建立的是Main Window项目，故此处导入的是QMainWindow
    # 参考博客中建立的是Widget项目，因此哪里导入的是QWidget
    def __init__(self):
        super(Mywindow, self).__init__()
        self.setupUi(self)

    def alert(self):  # 定义槽函数btn_click(),也可以理解为重载类Ui_MainWindow中的槽函数btn_click()
        self.lineEdit.setText("hi,PyQt5~")
        self.label.setStyleSheet("color:rgb(175,233,221,250)")


app = QtWidgets.QApplication(sys.argv)
window = Mywindow()
window.show()
sys.exit(app.exec_())