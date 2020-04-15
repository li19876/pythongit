import sys
import os
from PIL import ImageGrab ,Image
from PyQt5.QtCore import QThread, pyqtSignal

if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from aip import AipOcr
from PyQt5.QtWidgets import QApplication, QMainWindow
from baidu.ocr import *
import time

class worker(QThread):
    finished = pyqtSignal(dict)
    err = pyqtSignal(str)
    """ 你的 APPID AK SK """
    APP_ID = '17219475'
    API_KEY = 'wunGv6RtkjGbexAyh9yIKRjf'
    SECRET_KEY = 'izG1oSuj1EBQ21A6YosKkLmv6aPcrXra'
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)  # 配置百度接口

    def get_file_content(self,filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    def run(self):
        image = ImageGrab.grabclipboard()
        if image:
            image.save("cutimg.jpg")
            image = self.get_file_content('cutimg.jpg')
            # print(image)
            """ 调用通用文字识别, 图片参数为本地图片 """
            res = self.client.basicAccurate(image)
            self.finished.emit(res)
        else:
            self.err.emit('未获取到剪贴板截图,请重新截图尝试')


class MyWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.thread=worker()
        self.setupUi(self)
        self.thread.finished.connect(self.write)
        self.thread.err.connect(self.error)

    """ 读取图片 """
    def keyPressEvent(self,evt):
        # print(evt.key())
        if evt.key() == 16777268:
            self.run()

    def error(self,res):
        self.textEdit.setPlainText(res)

    def write(self,res):
        self.textEdit.setPlainText('')
        if res:
            for i in res["words_result"]:
                self.textEdit.append(i["words"])

    def run2(self):

        self.thread.start()
        self.textEdit.setPlainText('识别中....')




if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.setWindowTitle('OCR文字识别')
    myWin.show()
    sys.exit(app.exec_())









