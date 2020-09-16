# coding=utf-8
"""
Author:song
"""
import json
import os

import sys

if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PIL import Image, ImageCms
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from picture_synthesis.parseui import *


class worker(QThread):
    finished = pyqtSignal(str)

    def run(self):
        self.zhuaxian=MyWindow()
        fileName=self.zhuaxian.lineEdit.text()
        lx=self.zhuaxian.lineEdit_3.text()
        ly=self.zhuaxian.lineEdit_4.text()
        rx = self.zhuaxian.lineEdit_5.text()
        ry = self.zhuaxian.lineEdit_6.text()
        dirname = self.zhuaxian.lineEdit_2.text()

        filenames = os.walk(dirname)

        files = []
        filelist = []
        for file in filenames:
            files = file
        for f in files[2]:
            filelist.append(files[0] + os.sep + f)

        box = (int(lx), int(ly), int(rx), int(ry))
        for i in filelist:
            print(i)
            self.hec(fileName, i, box)

    def hec(self, bgimg, fimg, box):
        iscmyk = self.zhuaxian.radioButton_2.isChecked()
        base_img = Image.open(bgimg)
        resdir = os.path.dirname(bgimg) + '/' + os.path.basename(bgimg)[:-4]
        isExists = os.path.exists(resdir)
        if not isExists:
            os.mkdir(resdir)
            os.chdir(resdir)
        else:
            os.chdir(resdir)

        # 加载需要P上去的图片
        tmp_img = Image.open(fimg)
        fimgname = os.path.basename(fimg)
        self.finished.emit(fimgname)
        # 这里可以选择一块区域或者整张图片
        # region = tmp_img.crop((0,0,304,546)) #选择一块区域
        # 或者使用整张图片
        region = tmp_img

        region = region.resize((box[2] - box[0], box[3] - box[1]))
        base_img.paste(region, box)
        if iscmyk:
            base_img = ImageCms.profileToProfile(base_img, 'sRGB IEC61966-21.icc','Japan Color 2001 Coated.icc',renderingIntent=0, outputMode='CMYK')
            # base_img = ImageCms.profileToProfile(base_img, 'USWebCoatedSWOP.icc', 'sRGB Color Space Profile.icm',renderingIntent=0, outputMode='RGB')
            # base_img=base_img.convert('CMYK')
        # print(base_img.format)
        base_img.save(fimgname,quality=100)  # 保存图片


class MyWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.thread = worker()
        self.thread.finished.connect(self.write)
        self.setupUi(self)
        with open('coordinate.ini','r') as param:
            res=param.read()
            if res:
                fparam=json.loads(res)
                self.lineEdit_3.setText(fparam['lx'])
                self.lineEdit_4.setText(fparam['ly'])
                self.lineEdit_5.setText(fparam['rx'])
                self.lineEdit_6.setText(fparam['ry'])
                self.lineEdit.setText(fparam['img'])
                self.lineEdit_2.setText(fparam['dirname'])

    def write(self, res):
        self.textEdit.append(res)

    def chooseimg(self):
        fileName, fileType = QtWidgets.QFileDialog.getOpenFileName(self, "选取底图", os.getcwd(),
                                                                   'Image Files(*.jpg;*.png)')

        # print(fileName)
        # print(type(fileName))
        self.lineEdit.setText(fileName)

    def choosedir(self):
        dirname = QtWidgets.QFileDialog.getExistingDirectory(self, "选取二维码文件夹", os.getcwd())
        # print(dirname)

        self.lineEdit_2.setText(dirname)

    def run(self):

        iscmyk=self.radioButton_2.isChecked()
        lx = self.lineEdit_3.text()
        ly = self.lineEdit_4.text()
        rx = self.lineEdit_5.text()
        ry = self.lineEdit_6.text()
        img = self.lineEdit.text()
        dirname = self.lineEdit_2.text()
        if lx and ly and rx and ry and img and dirname:
            if lx.isdigit() and ly.isdigit() and rx.isdigit() and ry.isdigit():
                self.thread.start()
                with open('coordinate.ini','w') as f:
                    f.write(json.dumps({'lx':lx,'ly':ly,'rx':rx,'ry':ry,'img':img,'dirname':dirname}))
            else:
                QMessageBox.warning(self, "警告", "坐标只能是数字！", QMessageBox.Yes)
        else:
            QMessageBox.warning(self, "警告", "请填写好所有参数后提交！", QMessageBox.Yes)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.setWindowTitle('图片合成(By:李延松)')
    myWin.show()
    sys.exit(app.exec_())
