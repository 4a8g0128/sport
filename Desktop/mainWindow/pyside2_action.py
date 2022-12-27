import sys
import cv2
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QToolButton

import page1
from page1 import Ui_MainWindow_page1
from page3_1 import Ui_MainWindow_page3_1 
from page4_1 import Ui_MainWindow_page4_1 
from action1 import Ui_MainWindow_action1
from action2 import Ui_MainWindow_action2
from action3 import Ui_MainWindow_action3
from action4 import Ui_MainWindow_action4
from action5 import Ui_MainWindow_action5
from action6 import Ui_MainWindow_action6
from action7 import Ui_MainWindow_action7
from action8 import Ui_MainWindow_action8
e=0
class MainWindow1(QMainWindow):
    def __init__(self):
        super(MainWindow1, self).__init__()
        self.ui = Ui_MainWindow_page1()
        self.ui.setupUi(self)
        self.ui.toolButton.clicked.connect(self.jumptoaction1)
        self.ui.toolButton_2.clicked.connect(self.jumptoaction2)
        self.ui.toolButton_3.clicked.connect(self.jumptoaction3)
        self.ui.toolButton_4.clicked.connect(self.jumptoaction4)
        self.ui.toolButton_5.clicked.connect(self.jumptoaction5)
        self.ui.toolButton_6.clicked.connect(self.jumptoaction6)
        self.ui.toolButton_7.clicked.connect(self.jumptoaction7)
        self.ui.toolButton_8.clicked.connect(self.jumptoaction8)
    def jumptoaction1(self):

        window1.close()
        window1_1.show()
    def jumptoaction2(self):

        window1.close()
        window1_2.show()
    def jumptoaction3(self):

        window1.close()
        window1_3.show()
    def jumptoaction4(self):

        window1.close()
        window1_4.show()

    def jumptoaction5(self):

        window1.close()
        window1_5.show()
    def jumptoaction6(self):

        window1.close()
        window1_6.show()
    def jumptoaction7(self):

        window1.close()
        window1_7.show()
    def jumptoaction8(self):

        window1.close()
        window1_8.show()

class MainWindow3_1(QMainWindow):
    def __init__(self):
     super(MainWindow3_1, self).__init__()
    def MW3_1(self,name,pose_sample_folder,img):
        global e
        if e == 1:
            self.ui = Ui_MainWindow_page3_1(window4_1,window3_1,window1,name,pose_sample_folder,img)
            self.ui.setupUi(self)
           #self.ui.pushButton_3.clicked.connect(self.jumptoaction1)
            self.ui.pushButton_2.clicked.connect(self.jumptoaction2)   

    #def jumptoaction1(self):
        # window1.close()
        #window3.close()
        #window1.show()

    def jumptoaction2(self):
        # window1.close()
        window3_1.close()
        global e
        e-=1
        window4_1.show()
        window4_1.MW4_1()

class MainWindow4_1(QMainWindow):
    def __init__(self):
        super(MainWindow4_1, self).__init__()
    def MW4_1(self):
        self.ui = Ui_MainWindow_page4_1()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.jumptoaction1)
        poseLandmarks4=Ui_MainWindow_page3_1.poseLandmarks4_1()
        Ui_MainWindow_page4_1.poseLandmarks(self.ui,poseLandmarks4)
        Ui_MainWindow_page3_1.stop3_1()

    def jumptoaction1(self):
        Ui_MainWindow_page3_1.restop()
        window4_1.close()
        window1.show()

        

class MainWindow1_1(QMainWindow):
    def __init__(self):
        super(MainWindow1_1, self).__init__()
        self.ui = Ui_MainWindow_action1()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.jumptoaction1)
        self.ui.pushButton_2.clicked.connect(self.jumptoaction2)
        Ui_MainWindow_page3_1.restop()

    def jumptoaction1(self):

        window1_1.close()
        window1.show()
    def jumptoaction2(self):

        #window1.close()
        window1_1.close()
        global e
        e+=1       
        name="下肢肌力訓練"
        pose_sample_folder='/Users/xushuyu/Desktop/mainWindow/pos_csvs'
        img="./Image/1.1.jpg"
        Ui_MainWindow_page4_1.get_img(self,img)
        window3_1.show()
        window3_1.MW3_1(name,pose_sample_folder,img)


class MainWindow1_2(QMainWindow):
    def __init__(self):
        super(MainWindow1_2, self).__init__()
        self.ui = Ui_MainWindow_action2()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.jumptoaction1)
        self.ui.pushButton_2.clicked.connect(self.jumptoaction2)
    def jumptoaction1(self):

        window1_2.close()
        window1.show()
    def jumptoaction2(self):

        #window1.close()
        window1_2.close()
        global e
        e+=1       
        name="雙手平舉"
        pose_sample_folder='/Users/xushuyu/Desktop/mainWindow/pos_csvs'
        img="./Image/2.jpg"
        Ui_MainWindow_page4_1.get_img(self,img)
        window3_1.show()
        window3_1.MW3_1(name,pose_sample_folder,img)


class MainWindow1_3(QMainWindow):
    def __init__(self):
        super(MainWindow1_3, self).__init__()
        self.ui = Ui_MainWindow_action3()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.jumptoaction1)
        self.ui.pushButton_2.clicked.connect(self.jumptoaction2)

    def jumptoaction1(self):
        window1_3.close()
        window1.show()

    def jumptoaction2(self):
        #window1.close()
        window1_3.close()
        global e
        e+=1       
        name="手"
        pose_sample_folder='/Users/xushuyu/Desktop/mainWindow/pos_csvs'
        img="./Image/3.png"
        Ui_MainWindow_page4_1.get_img(self,img)
        window3_1.show()
        window3_1.MW3_1(name,pose_sample_folder,img)

class MainWindow1_4(QMainWindow):
    def __init__(self):
        super(MainWindow1_4, self).__init__()
        self.ui = Ui_MainWindow_action4()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.jumptoaction1)
        self.ui.pushButton_2.clicked.connect(self.jumptoaction2)

    def jumptoaction1(self):
        window1_4.close()
        window1.show()

    def jumptoaction2(self):
        # window1.close()
        window1_4.close()
        global e
        e+=1       
        name="腰"
        pose_sample_folder='/Users/xushuyu/Desktop/mainWindow/pos_csvs'
        img="./Image/10.jpg"
        Ui_MainWindow_page4_1.get_img(self,img)
        window3_1.show()
        window3_1.MW3_1(name,pose_sample_folder,img)



class MainWindow1_5(QMainWindow):
    def __init__(self):
        super(MainWindow1_5, self).__init__()
        self.ui = Ui_MainWindow_action5()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.jumptoaction1)
        self.ui.pushButton_2.clicked.connect(self.jumptoaction2)

    def jumptoaction1(self):
        window1_5.close()
        window1.show()

    def jumptoaction2(self):
        # window1.close()
        window1_5.close()
        global e
        e+=1       
        name="手臂彎曲"
        pose_sample_folder='/Users/xushuyu/Desktop/mainWindow/pos_csvs'
        img="./Image/5.jpg"
        Ui_MainWindow_page4_1.get_img(self,img)
        window3_1.show()
        window3_1.MW3_1(name,pose_sample_folder,img)


class MainWindow1_6(QMainWindow):
    def __init__(self):
        super(MainWindow1_6, self).__init__()
        self.ui = Ui_MainWindow_action6()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.jumptoaction1)
        self.ui.pushButton_2.clicked.connect(self.jumptoaction2)

    def jumptoaction1(self):
        window1_6.close()
        window1.show()

    def jumptoaction2(self):
        # window1.close()
        window1_6.close()
        global e
        e+=1       
        name="半蹲"
        pose_sample_folder='/Users/xushuyu/Desktop/mainWindow/pos_csvs'
        img="./Image/12.jpg"
        Ui_MainWindow_page4_1.get_img(self,img)
        window3_1.show()
        window3_1.MW3_1(name,pose_sample_folder,img)      



class MainWindow1_7(QMainWindow):
    def __init__(self):
        super(MainWindow1_7, self).__init__()
        self.ui = Ui_MainWindow_action7()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.jumptoaction1)
        self.ui.pushButton_2.clicked.connect(self.jumptoaction2)

    def jumptoaction1(self):
        window1_7.close()
        window1.show()

    def jumptoaction2(self):
        # window1.close()
        window1_7.close()
        global e
        e+=1       
        name="抬腿"
        pose_sample_folder='/Users/xushuyu/Desktop/mainWindow/pos_csvs'
        img="./Image/11.jpg"
        Ui_MainWindow_page4_1.get_img(self,img)
        window3_1.show()
        window3_1.MW3_1(name,pose_sample_folder,img)


class MainWindow1_8(QMainWindow):
    def __init__(self):
        super(MainWindow1_8, self).__init__()
        self.ui = Ui_MainWindow_action8()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.jumptoaction1)
        self.ui.pushButton_2.clicked.connect(self.jumptoaction2)

    def jumptoaction1(self):
        window1_8.close()
        window1.show()

    def jumptoaction2(self):
        # window1.close()
        window1_8.close()
        global e
        e+=1       
        name="手臂上舉"
        pose_sample_folder='/Users/xushuyu/Desktop/mainWindow/pos_csvs'
        img="./Image/9.jpg"
        Ui_MainWindow_page4_1.get_img(self,img)
        window3_1.show()
        window3_1.MW3_1(name,pose_sample_folder,img)

def op1():
    window1_1.show()
    window1.close()
if __name__ == "__main__":

    app = QApplication(sys.argv)
    #button = page1.op1()
    window1 = MainWindow1()
    window1.show()

    window1_1 = MainWindow1_1()
    #window1_1.show()
    #button.clicked.connect(window1.close(), window1_1.show())
   # button.clicked.connect(
    #    lambda: {window1.close(), window1_1.show()}
   # )


    window1_2 = MainWindow1_2()
  #  window1_2.show()
    
    window1_3 = MainWindow1_3()
    
  #  window1_3.show()
    
    window1_4 = MainWindow1_4()
  #  window1_4.show()

    window1_5 = MainWindow1_5()
   # window1_5.show()

    window1_6 = MainWindow1_6()
   # window1_6.show()

    window1_7 = MainWindow1_7()
   # window1_7.show()

    window1_8 = MainWindow1_8()
    #**
    window3_1 = MainWindow3_1()
  #  window3.show()

    window4_1 = MainWindow4_1()
   # window4.show()
    sys.exit(app.exec_())