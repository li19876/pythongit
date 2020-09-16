import sys
from PyQt5.QtWidgets import QMainWindow,QApplication

class FirstMainWin(QMainWindow):
    def __init__(self):
        super(FirstMainWin,self).__init__()
        self.setWindowTitle("一个窗口")
        status = self.statusBar()
        status.showMessage('只存在5s的消息',5000)

if __name__=='__main__':
    app = QApplication(sys.argv)
    w = FirstMainWin()
    w.resize(500,500)
    w.show()

    sys.exit(app.exec_())