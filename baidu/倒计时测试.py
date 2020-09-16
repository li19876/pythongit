from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow
import sys
from baidu.daotime import Ui_MainWindow

class Myw(QMainWindow,Ui_MainWindow):
    def _init_(self):
        super(Myw, self).__init__()
        self.setupUi(self)
        self.label.setText("123")


app=QApplication(sys.argv)
w=Myw()
w.show()
sys.exit(app.exec_())
