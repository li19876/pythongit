from PyQt5.QtWidgets import QApplication,QWidget
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QWidget()
    win.setWindowTitle("第一个程序")
    win.resize(500,500)
    win.move(500,300)
    win.show()
    sys.exit(app.exec_())
