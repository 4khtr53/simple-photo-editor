
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from PIL import ImageFilter
from PIL.ImageFilter import *
from PIL import Image
from PIL.Image import *


import os


width = 500
height = 500
app = QApplication([])
screen = QWidget()
screen.resize(width,height) #ganti ukuran
screen.setWindowTitle("Photo Editor")


lb_image = QLabel('Image')

list_files = QListWidget()

btn_upload = QPushButton('Upload folder')


btn_bnw = QPushButton('Black and White')
btn_Rleft = QPushButton('Rotate left')
btn_Rright = QPushButton('Rotate right')
btn_flip = QPushButton('Flip')
btn_mirror = QPushButton('Mirror')
btn_sharpen = QPushButton('Sharpen')
btn_blur = QPushButton('Blur')



main_layout = QHBoxLayout()


col_1 = QVBoxLayout()

col_1.addWidget(list_files)
col_1.addWidget(btn_upload)


layout_btn = QHBoxLayout()

layout_btn.addWidget(btn_Rleft)
layout_btn.addWidget(btn_Rleft)
layout_btn.addWidget(btn_flip)
layout_btn.addWidget(btn_mirror)
layout_btn.addWidget(btn_bnw)
layout_btn.addWidget(btn_blur)
layout_btn.addWidget(btn_sharpen)


col_2 = QVBoxLayout()

col_2.addWidget(lb_image, 95)
col_2.addLayout(layout_btn, 5)


main_layout.addLayout(col_1, 30)
main_layout.addLayout(col_2, 70)


screen.setLayout(main_layout)

screen.show()



workdir = ''

def chooseworkdir():
    global workdir

    workdir = QFileDialog.getExistingDirectory()


def filter(files, extension):
    result = list()

    for filename in files:
        for ext in extension:
            if filename.endswith(ext):
                result.append(filename)
    
    return result


def showfilenamelist():
    extension = ['.jpg', '.png', '.pdf', '.jpeg', '.pnp']

    chooseworkdir()
    files = os.listdir(workdir)
    filenames = filter(files, extension)

    list_files.clear()

    for filename in filenames:
        list_files.addItem(filename)


class imageprocessor():
    def __init__(self):
        self.filename = None
        self.dir = None
        self.image = None
        self.save_dir = 'Modified/'

    
    def loadimage(self, filename, dir):
        self.dir = dir
        self.filename = filename
        image_path = os.path.join(dir, filename)

        self.image = image.open(image_path)
        

    def saveimage(self):
        path = os.path.join(self.dir, self.save_dir)

        if not(os.path.exists(path)) or os.path.isdir(path):
            os.mkdir(path)
        
        image_path = os.path.join(path, self.filename)
        self.image.save(image_path)
    

    def showimage(self):
        lb_image.hide()
        pixmapimage = QPixmap(path)

        w, h = lb_image.width(), lb_image.height()
    
    pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
    lb_image.setPixmap(pixmapimage)

    lb_image.show()


    def do_bw(self):
        self.image = self.image.convert('L')
        self.saveimage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showimage()
    

    def do_blur(self):
        self.image = self.image.filter(ImageFilter.BLUR) #cara untuk blur in
        self.saveimage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showimage()
    
    
    def rotate_left(self):
        self.image = self.image.transpose(Image.ROTATE_90) #Rotasi ke kiri sbyk 90 degree
        self.saveimage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showimage()
    

    def rotate_right(self):
        self.image = self.image.transpose(Image.ROTATE_270) #Rotasi ke kanan sbyk 270 degree
        self.saveimage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showimage()


    def do_flip(self):
        self.image = self.image.transpose(Image.ROTATE_180) #Rotasi kebawah sbyk 180 degree
        self.saveimage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showimage()


    def do_mirror(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveimage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showimage()


    def do_sharpen(self):
        self.image = self.image.filter(SHARPEN)
        self.saveimage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showimage()



def showchosenimage():
    if list_files.currentRow() >= 0:
        filename = list_files.currentItem().text()
        workimage.loadImage(workdir,filename)
        #set file path
        image_path = os.path.join(workimage.dir, workimage.filename)
        #tampilin
        workimage.showimage(image_path)


workimage = imageprocessor()

list_files.currentRowChanged.connect(showchosenimage)


#koneksiin btn
btn_bnw.clicked.connect(workimage.do_bw)
btn_blur.clicked.connect(workimage.do_blur)
btn_Rleft.clicked.connect(workimage.rotate_left)
btn_Rright.clicked.connect(workimage.rotate_right)
btn_flip.clicked.connect(workimage.do_flip)
btn_mirror.clicked.connect(workimage.do_mirror)
btn_sharpen.clicked.connect(workimage.do_sharpen)

btn_upload.clicked.connect(showfilenamelist)


#run
app.exec()














