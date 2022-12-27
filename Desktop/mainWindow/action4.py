# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'win1-4.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys

class Ui_MainWindow_action4(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(50, 150, 361, 261))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(440, 70, 291, 391))
        self.label_2.setAutoFillBackground(True)
        self.label_2.setPixmap(QPixmap(u"./Image/10.jpg"))
        self.label_2.setScaledContents(True)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 10, 51, 41))
        icon = QIcon()
        icon.addFile(u"./Image/zTXe8gRac.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(50, 150))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 90, 111, 51))
        font = QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 10, 81, 41))
        font1 = QFont()
        font1.setPointSize(13)
        self.label.setFont(font1)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(190, 440, 161, 51))
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_6.setFont(font2)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(540, 490, 111, 41))
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
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'PMingLiU'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u5fae\u8edf\u6b63\u9ed1\u9ad4,\u860b\u679c\u5137\u9ed1\u9ad4,\u65b0\u7d30\u660e\u9ad4,Verdana,sans-serif'; font-size:14pt; color:#2a2a2a; background-color:#ffffff;\">1. \u8eab\u9ad4\u7ad9\u76f4\uff0c\u8173\u6253\u958b\u8207\u80a9\u540c\u5bec\uff0c\u8173\u8dbe\u7a0d\u5fae\u671d\u5916\uff0c\u624b\u81c2\u5411\u524d\u5e73\u8209\u3002 </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u5fae\u8edf\u6b63\u9ed1\u9ad4,\u860b\u679c"
                        "\u5137\u9ed1\u9ad4,\u65b0\u7d30\u660e\u9ad4,Verdana,sans-serif'; font-size:14pt; color:#2a2a2a; background-color:#ffffff;\">2. \u8170\u6253\u76f4\uff0c\u819d\u84cb\u9806\u8457\u8173\u8dbe\u65b9\u5411\u5fae\u958b\u7136\u5f8c\u5c41\u80a1\u6162\u6162\u5750\u4e0b\uff0c\u81c0\u90e8\u7684\u9ad8\u5ea6\u6700\u597d\u6bd4\u819d\u84cb\u66f4\u4f4e\u3002 </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u5fae\u8edf\u6b63\u9ed1\u9ad4,\u860b\u679c\u5137\u9ed1\u9ad4,\u65b0\u7d30\u660e\u9ad4,Verdana,sans-serif'; font-size:14pt; color:#2a2a2a; background-color:#ffffff;\">3. \u7ad9\u8d77\u4f86\u6642\u96d9\u624b\u5f80\u5f8c\u62c9\uff0c\u80cc\u7528\u529b\u6536\u7dca\u3002</span></p></body></html>", None))
        self.label_2.setText("")
        self.pushButton.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u52d5\u4f5c\u8aaa\u660e:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u56de\u4e3b\u9801", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u8170", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u958b\u59cb", None))
    # retranslateUi
class MainWindow(QMainWindow):
        def __init__(self):
            super(MainWindow, self).__init__()
            self.ui = Ui_MainWindow_action4()
            self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
