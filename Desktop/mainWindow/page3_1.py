# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'win3_1.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys
import time
import cv2
import os
import numpy as np
import mediapipe as mp
from creatcsv import creatcsv
from poseSample import poencsv
from poselandmarks import FullBodyPoseEmbedder
import qtmodern.styles
import qtmodern.windows

mp_drawing = mp.solutions.drawing_utils          # mediapipe 繪圖方法
mp_drawing_styles = mp.solutions.drawing_styles  # mediapipe 繪圖樣式
mp_pose = mp.solutions.pose                      # mediapipe 姿勢偵測
stop = 0
poseLandmarks4 =""


class Ui_MainWindow_page3_1(object):

    def __init__(self,window4_1,window3_1,window1,name,pose_sample_folder,get_img):
        
        print(123)
        self.fullbody =  FullBodyPoseEmbedder()
        self.pose_samples_folder=pose_sample_folder
        self.pose_open=poencsv(self.pose_samples_folder,
                fullbody=self.fullbody)
        npw_time=time.time()
        local_time=time.localtime(npw_time)
        self.mk_time=time.mktime(local_time)
        self.thirty_seconds_after=self.mk_time+30
        self.window3_1=window3_1
        self.window4_1=window4_1
        self.window1=window1
        self.name=name
        self.poseLandmarks4=""
        self.get_img=get_img 

    def stop3_1():
        global stop 
        stop = 1
    def restop():
        global stop
        stop = 0
    def setup_camera(self,video_size_width,video_size_height):
        """Initialize camera.、、
        """
        global stop
        if stop == 0:
            self.capture = cv2.VideoCapture(0)
            if not  self.capture.isOpened():
                print("Cannot open camera")
                exit()
            self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, video_size_width)
            self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, video_size_height)

            self.timer = QTimer()
            self.timer.timeout.connect(self.display_video_stream)
            self.timer.start(30)
  
    def display_video_stream(self):
        """Read frame from camera and repaint QLabel widget.
        """
        global stop
        # 啟用姿勢偵測
        if stop == 0:
            with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
                ret, img = self.capture.read()

                #倒數30秒 
                now_time=time.time()
                local_time=time.localtime(now_time)
                mk_time=time.mktime(local_time)
                x=0
                second=round(self.thirty_seconds_after-mk_time)
                if second is x :
                    #關閉攝影機
                    #30秒後跳到window4
                    print('Finish')
                    self.capture.release()
                    self.window3_1.close()
                    self.window4_1.show()
                    self.window4_1.MW4_1()
                    return
                    
                      
                   
                if not ret:
                    print("Cannot receive frame")
                    return
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)   # 將 BGR 轉換成 RGB
                results = pose.process(img)                  # 取得姿勢偵測結果
                # 根據姿勢偵測結果，標記身體節點和骨架
                mp_drawing.draw_landmarks(
                    img,
                    results.pose_landmarks,
                    mp_pose.POSE_CONNECTIONS,
                    landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
                img = cv2.flip(img, 1)
                #把影像調整到標簽QLabel一樣大
                image = QImage(img, img.shape[1], img.shape[0],  img.strides[0], QImage.Format_RGB888)
                myScaledPixmap = QPixmap.fromImage(image).scaled( self.label_2.size(), Qt.KeepAspectRatio)
                self.label_2.setPixmap(myScaledPixmap)
            
            # 取得landmarks 
            pose_landmarks = results.pose_landmarks
            if pose_landmarks is not None:
                frame_height, frame_width = img.shape[0], img.shape[1]
                pose_landmarks = np.array([[lmk.x * frame_width, lmk.y * frame_height, lmk.z * frame_width]
                                        for lmk in pose_landmarks.landmark], dtype=np.float32)
                assert pose_landmarks.shape == (33, 3), 'Unexpected landmarks shape: {}'.format(pose_landmarks.shape)
           
            #紀錄User_landmarks 
            csvinputfolder ='landmarks_Save'
            posename=self.name
            csv=creatcsv(landmarks = pose_landmarks ,csvs_out_folder=csvinputfolder,pose_name=posename)
            csv.creat()

            #比對姿勢  
            self.pose_open=poencsv(self.pose_samples_folder,fullbody=self.fullbody)
            poseLandmarks=self.pose_open.__cell__(pose_landmarks)

            #輸出秒數/相識度
            self.textEdit_3.setText(str(second))
            print(0)
            self.textEdit.setText(str(poseLandmarks))
            self.poseLandmarks4=str(poseLandmarks)
            global poseLandmarks4
            poseLandmarks4=str(self.poseLandmarks4)
        if stop == 1:
            #關閉攝影機
           self.capture.release()
           print(1)

    def poseLandmarks4_1():
        global poseLandmarks4
        return poseLandmarks4  

    def setupUi(self,MainWindow):

        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(450, 50, 61, 31))
        font = QFont()
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(680, 40, 71, 51))
        font1 = QFont()
        font1.setPointSize(32)
        self.label_3.setFont(font1)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 110, 371, 391))
        self.label_7.setAutoFillBackground(True)
        self.label_7.setPixmap(QPixmap(self.get_img))
        self.label_7.setScaledContents(True)
        self.textEdit_3 = QTextEdit(self.centralwidget)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(600, 40, 81, 51))
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(360, 40, 81, 51))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(410, 110, 371, 391))
        font2 = QFont()
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        self.label_2.setFont(font2)
        self.label_2.setMouseTracking(False)
        self.label_2.setTabletTracking(False)
        self.label_2.setAcceptDrops(False)
        self.label_2.setAutoFillBackground(True)
        global stop
        if stop == 0:
            self.label_2.setPixmap (self.setup_camera(video_size_width=1000,video_size_height=1000))
        #self.label_2.setScaledContents(True)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(750, 50, 58, 41))
        font3 = QFont()
        font3.setPointSize(17)
        self.label_8.setFont(font3)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(540, 60, 61, 31))
        font4 = QFont()
        font4.setPointSize(13)
        self.label_4.setFont(font4)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(520, 510, 111, 41))
        self.pushButton_2.setFont(font4)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(280, 40, 81, 51))
        self.label_5.setFont(font4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 25))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

        

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"/30", None))
        self.label_7.setText("")
        self.textEdit_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'PMingLiU'; font-size:50pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:50pt;\">10</span></p></body></html>", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'PMingLiU'; font-size:50pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:50pt;\">35</span></p></body></html>", None))
        self.label_2.setText('')
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u79d2", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u79d2\u6578:", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u7d50\u675f", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u76f8\u4f3c\u5ea6:", None))
    # retranslateUi
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow_page3_1()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
