import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QDesktopWidget

class Center(QMainWindow):
    def __init__(self):
        super(Center,self).__init__()
        self.setWindowTitle("一个窗口")
        status = self.statusBar()
        status.showMessage('只存在5s的消息',5000)

    # def centershow(self):
    #     screen = QDesktopWidget().screenGeometry()
    #     window = self.geometry()
    #     newleft = (screen.width() - window.width()) / 2
    #     newtop = (screen.height() - window.height()) / 2
    #     self.move(newleft,newtop)

if __name__=='__main__':
    app = QApplication(sys.argv)
    w = Center()
    # w.move(0,0)
    # w.centershow()
    w.resize(500,500)
    w.show()

    sys.exit(app.exec_())