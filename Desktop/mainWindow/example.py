import sys

from PySide2.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from win1_ui import Ui_MainWindow as Win1_ui
from win3_ui import Ui_MainWindow as Win3_ui
from win4_ui import Ui_MainWindow as Win4_ui
from win1_1_ui import Ui_MainWindow as Win1_1_ui
from win1_2_ui import Ui_MainWindow as Win1_2_ui
from win1_3_ui import Ui_MainWindow as Win1_3_ui
from win1_4_ui import Ui_MainWindow as Win1_4_ui
from win1_5_ui import Ui_MainWindow as Win1_5_ui
from win2_ui import Ui_MainWindow as Win2_ui
from win1_7_ui import Ui_MainWindow as Win1_7_ui
from win1_8_ui import Ui_MainWindow as Win1_8_ui


class Win1ui(QtWidgets.QMainWindow, Win1_ui):
    def __init__(self):
        super(Win1ui, self).__init__()
        self.setupUi(self)


class Win2ui(QtWidgets.QMainWindow, Win2_ui):
    def __init__(self):
        super(Win2ui, self).__init__()
        self.setupUi(self)


class Win3ui(QtWidgets.QMainWindow, Win3_ui):
    def __init__(self):
        super(Win3ui, self).__init__()
        self.setupUi(self)


class Win4ui(QtWidgets.QMainWindow, Win4_ui):
    def __init__(self):
        super(Win4ui, self).__init__()
        self.setupUi(self)


class Win1_1ui(QtWidgets.QMainWindow, Win1_1_ui):
    def __init__(self):
        super(Win1_1ui, self).__init__()
        self.setupUi(self)
        self.win3 = Win3ui()
        self.win1 = Win1ui()
        self.win3.pushButton_3.clicked.connect(
           lambda: {win1.close(), win3.close(), win1_1.show()}
         )


class Win1_2ui(QtWidgets.QMainWindow, Win1_2_ui):
    def __init__(self):
        super(Win1_2ui, self).__init__()
        self.setupUi(self)


class Win1_3ui(QtWidgets.QMainWindow, Win1_3_ui):
    def __init__(self):
        super(Win1_3ui, self).__init__()
        self.setupUi(self)


class Win1_4ui(QtWidgets.QMainWindow, Win1_4_ui):
    def __init__(self):
        super(Win1_4ui, self).__init__()
        self.setupUi(self)


class Win1_5ui(QtWidgets.QMainWindow, Win1_5_ui):
    def __init__(self):
        super(Win1_5ui, self).__init__()
        self.setupUi(self)


class Win1_7ui(QtWidgets.QMainWindow, Win1_7_ui):
    def __init__(self):
        super(Win1_7ui, self).__init__()
        self.setupUi(self)


class Win1_8ui(QtWidgets.QMainWindow, Win1_8_ui):
    def __init__(self):
        super(Win1_8ui, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win1 = Win1ui()
    win1.show()
    #首頁換第2畫面
    # 第2畫面換首頁畫面
    #1_1
    win1_1 = Win1_1ui()
    # 1-1首頁換第2畫面
    win1.toolButton.clicked.connect(
        lambda: {win1.close(), win1_1.show()}
    )
    # 第2畫面換首頁畫面
    win1_1.pushButton.clicked.connect(
        lambda: {win1_1.close(), win1.show()}
    )
    win3 = Win3ui()
    # 第2畫面換第3畫面
    win1_1.pushButton_2.clicked.connect(
        lambda: {win1.close(), win1_1.close(), win3.show()}
    )
    # 第3畫面換第2畫面
    #win3.pushButton_3.clicked.connect(
    #    lambda: {win1.close(), win3.close(), win1_1.show()}
    #)
    #1_2
    win1_2 = Win1_2ui()
    #1-2 首頁換第2畫面
    win1.toolButton_2.clicked.connect(
        lambda: {win1.close(), win1_1.close(), win1_2.show()}
    )
    # 第2畫面換首頁畫面
    win1_2.pushButton.clicked.connect(
        lambda: {win1_1.close(), win1_2.close(), win1.show()}
    )
    # 第2畫面換第3畫面
    win1_2.pushButton_2.clicked.connect(
        lambda: {win1_1.close(), win1_2.close(), win1.close(), win3.show()}
    )
    # 第3畫面換第2畫面
   # win3.pushButton_2.clicked.connect(
   #     lambda: {win1_1.close(), win3.close(), win1.close(), win1_2.show()}
   # )

    #1_3
    win1_3 = Win1_3ui()
    #1-3 首頁換第2畫面
    win1.toolButton_3.clicked.connect(
        lambda: {win1.close(), win1_1.close(), win1_2.close(), win1_3.show()}
    )
    # 第2畫面換首頁畫面
    win1_3.pushButton.clicked.connect(
        lambda: {win1_3.close(), win1_1.close(), win1_2.close(), win1.show()}
    )
    # 第2畫面換第3畫面
    win1_3.pushButton_2.clicked.connect(
        lambda: {win1_1.close(), win1_2.close(), win1.close(), win1_3.close(), win3.show()}
    )
    #1_4
    win1_4 = Win1_4ui()
    #1-4 首頁換第2畫面
    win1.toolButton_4.clicked.connect(
        lambda: {win1.close(), win1_1.close(), win1_2.close(),win1_3.close(), win1_4.show()}
    )
    # 第2畫面換首頁畫面
    win1_4.pushButton.clicked.connect(
        lambda: {win1_4.close(), win1_1.close(), win1_2.close(), win1_3.close(), win1.show()}
    )
    # 第2畫面換第3畫面
    win1_4.pushButton_2.clicked.connect(
        lambda: {win1_1.close(), win1_2.close(), win1.close(), win1_3.close(), win1_4.close(),  win3.show()}
    )
    #1_5
    win1_5 = Win1_5ui()
    #1-5首頁換第2畫面
    win1.toolButton_5.clicked.connect(
        lambda: {win1.close(), win1_1.close(), win1_2.close(), win1_3.close(), win1_4.close(), win1_5.show()}
    )
    # 第2畫面換首頁畫面
    win1_5.pushButton.clicked.connect(
        lambda: {win1_5.close(), win1_1.close(), win1_2.close(), win1_3.close(), win1_4.close(), win1.show()}
    )
    # 第2畫面換第3畫面
    win1_5.pushButton_2.clicked.connect(
        lambda: {win1_1.close(), win1_2.close(), win1.close(), win1_3.close(), win1_4.close(), win1_5.close(), win3.show()}
    )
    #1_6
    win2 = Win2ui()
    #1-6 首頁換第2畫面
    win1.toolButton_6.clicked.connect(
        lambda: {win1.close(), win1_1.close(), win1_2.close(), win1_3.close(), win1_4.close(), win1_5.close(), win2.show()}
    )
    # 第2畫面換首頁畫面
    win2.pushButton.clicked.connect(
        lambda: {win2.close(), win1_1.close(), win1_2.close(), win1_3.close(), win1_4.close(), win1_5.close(),
                 win1.show()}
    )
    # 第2畫面換第3畫面
    win2.pushButton_2.clicked.connect(
        lambda: {win1_1.close(), win1_2.close(), win1.close(), win1_3.close(), win1_4.close(), win1_5.close(),
                 win2.close(), win3.show()}
    )
    #1_7
    win1_7 = Win1_7ui()
    #1-7 首頁換第2畫面
    win1.toolButton_7.clicked.connect(
        lambda: {win1.close(), win1_1.close(), win1_2.close(), win1_3.close(), win1_4.close(), win1_5.close(),
                 win2.close(), win1_7.show()}
    )
    # 第2畫面換首頁畫面
    win1_7.pushButton.clicked.connect(
        lambda: {win1_7.close(), win1_1.close(), win1_2.close(), win1_3.close(), win1_4.close(), win1_5.close(),
                 win2.close(), win1.show()}
    )
    # 第2畫面換第3畫面
    win1_7.pushButton_2.clicked.connect(
        lambda: {win1_1.close(), win1_2.close(), win1.close(), win1_3.close(), win1_4.close(), win1_5.close(),
                 win2.close(), win1_7.close(), win3.show()}
    )
    #1_8
    win1_8 = Win1_8ui()
    #1-8 首頁換第2畫面
    win1.toolButton_8.clicked.connect(
        lambda: {win1.close(), win1_1.close(), win1_2.close(), win1_3.close(), win1_4.close(), win1_5.close(),
                 win2.close(), win1_7.close(), win1_8.show()}
    )
    # 第2畫面換首頁畫面
    win1_8.pushButton.clicked.connect(
        lambda: {win1_8.close(), win1_1.close(), win1_2.close(), win1_3.close(), win1_4.close(), win1_5.close(),
                 win2.close(), win1_7.close(), win1.show()}
    )
    # 第2畫面換第3畫面
    win1_8.pushButton_2.clicked.connect(
        lambda: {win1_1.close(), win1_2.close(), win1.close(), win1_3.close(), win1_4.close(), win1_5.close(),
                 win2.close(), win1_7.close(), win1_8.close(), win3.show()}
    )



    # 第2畫面換第3畫面
    #win3 = Win3ui()
    #win2.pushButton_2.clicked.connect(
     #   lambda: {win1.close(), win2.close(), win3.show()}
    #)

    # 第3畫面換第2畫面
   # win3.pushButton_3.clicked.connect(
    #    lambda: {win1.close(), win3.close(), win2.show()}
    #)

    # 第3畫面換第4畫面
    win4 = Win4ui()
    win3.pushButton_2.clicked.connect(
        lambda: {win1.close(), win2.close(), win3.close(), win4.show()}
    )

    # 第4畫面換第2畫面
    win4.pushButton_3.clicked.connect(
        lambda: {win1.close(), win3.close(), win4.close(), win2.show()}
    )

    # 第4畫面換第1畫面
    win4.pushButton_2.clicked.connect(
        lambda: {win2.close(), win3.close(), win4.close(), win1.show()}
    )



    sys.exit(app.exec_())
