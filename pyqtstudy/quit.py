import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton,QWidget,QHBoxLayout

class Quitapp(QMainWindow):
    def __init__(self):
        super(Quitapp,self).__init__()
        self.pushbutton = QPushButton('退出')

        self.pushbutton.clicked.connect(self.quiter)
        layout = QHBoxLayout()
        layout.addWidget(self.pushbutton)

        frame = QWidget()
        frame.setLayout(layout)
        self.setCentralWidget(frame)
    def quiter(self):
        a = QApplication.instance()
        a.quit()

if __name__=='__main__':
    app = QApplication(sys.argv)
    w = Quitapp()
    w.resize(500,200)
    w.show()
    sys.exit(app.exec_())